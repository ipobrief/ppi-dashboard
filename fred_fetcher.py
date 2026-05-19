"""Fetch PPI data from FRED API and cache locally."""

import os
import json
import datetime
import pandas as pd
from fredapi import Fred
from dotenv import load_dotenv
from config import CATEGORIES

load_dotenv()

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)


def get_fred():
    api_key = os.getenv("FRED_API_KEY")
    # Streamlit Cloud secrets support
    if not api_key or api_key == "your_fred_api_key_here":
        try:
            import streamlit as st
            api_key = st.secrets.get("FRED_API_KEY", None)
        except Exception:
            pass
    if not api_key or api_key == "your_fred_api_key_here":
        raise ValueError("FRED_API_KEY가 설정되지 않았습니다. .env 파일에 API 키를 입력하세요.")
    return Fred(api_key=api_key)


def fetch_all_series(force=False):
    """Fetch all PPI series from FRED. Uses cache unless force=True or cache is stale."""
    cache_path = os.path.join(DATA_DIR, "ppi_data.json")
    meta_path = os.path.join(DATA_DIR, "fetch_meta.json")

    if not force and os.path.exists(meta_path):
        with open(meta_path, "r") as f:
            meta = json.load(f)
        last_fetch = datetime.datetime.fromisoformat(meta["last_fetch"])
        if (datetime.datetime.now() - last_fetch).days < 7:
            if os.path.exists(cache_path):
                return load_cached_data()

    fred = get_fred()
    all_data = {}
    errors = []

    for cat_name, cat_info in CATEGORIES.items():
        for series_name, series_info in cat_info["series"].items():
            series_id = series_info["id"]
            try:
                data = fred.get_series(series_id, observation_start="2015-01-01")
                if data is not None and len(data) > 0:
                    all_data[series_id] = {
                        "category": cat_name,
                        "name": series_name,
                        "kr_stocks": series_info["kr_stocks"],
                        "drivers": series_info.get("drivers", ""),
                        "risks": series_info.get("risks", ""),
                        "values": {str(k.date()): float(v) for k, v in data.dropna().items()},
                    }
            except Exception as e:
                errors.append(f"{series_id} ({series_name}): {e}")

    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

    with open(meta_path, "w") as f:
        json.dump({"last_fetch": datetime.datetime.now().isoformat(), "errors": errors}, f, indent=2)

    return all_data


def load_cached_data():
    cache_path = os.path.join(DATA_DIR, "ppi_data.json")
    if not os.path.exists(cache_path):
        return None
    with open(cache_path, "r", encoding="utf-8") as f:
        return json.load(f)
