"""Analyze PPI series data - compute signals, momentum, and generate investment notes."""

import pandas as pd
import numpy as np


def compute_metrics(values: dict) -> dict | None:
    """Compute MOM, 3M, YOY, momentum, and peak comparison from a time series."""
    if not values or len(values) < 13:
        return None

    series = pd.Series(values, dtype=float)
    series.index = pd.to_datetime(series.index)
    series = series.sort_index()

    latest = series.iloc[-1]
    prev_1m = series.iloc[-2] if len(series) >= 2 else latest
    prev_3m = series.iloc[-4] if len(series) >= 4 else latest
    prev_12m = series.iloc[-13] if len(series) >= 13 else latest
    peak = series.max()
    peak_date = series.idxmax()
    trough = series.min()
    trough_date = series.idxmin()

    mom = ((latest / prev_1m) - 1) * 100 if prev_1m != 0 else 0
    three_m = ((latest / prev_3m) - 1) * 100 if prev_3m != 0 else 0
    yoy = ((latest / prev_12m) - 1) * 100 if prev_12m != 0 else 0
    from_peak = ((latest / peak) - 1) * 100 if peak != 0 else 0

    mom_prev = ((prev_1m / series.iloc[-3]) - 1) * 100 if len(series) >= 3 and series.iloc[-3] != 0 else 0
    acceleration = mom - mom_prev
    momentum = mom * 0.4 + three_m * 0.35 + yoy * 0.25

    return {
        "latest_value": round(latest, 2),
        "latest_date": str(series.index[-1].date()),
        "mom": round(mom, 1),
        "three_m": round(three_m, 1),
        "yoy": round(yoy, 1),
        "momentum": round(momentum, 1),
        "from_peak": round(from_peak, 1),
        "acceleration": round(acceleration, 1),
        "peak_value": round(peak, 3),
        "peak_date": str(peak_date.date()),
        "trough_value": round(trough, 1),
        "trough_date": str(trough_date.date()),
    }


def classify_signal(metrics: dict) -> str:
    mom = metrics["mom"]
    three_m = metrics["three_m"]
    yoy = metrics["yoy"]
    accel = metrics["acceleration"]

    if yoy > 5 and three_m > 3:
        return "Strong Uptrend"
    if yoy > 2 and mom >= 0:
        return "Moderate Uptrend"
    if mom > 1 and yoy < 0:
        return "Reversal"
    if accel > 1 and mom > 0.5:
        return "Momentum"
    if yoy > 2 and mom <= 0:
        return "Cooling After Rise"
    if abs(yoy) <= 2 and abs(mom) <= 0.5:
        return "Flat"
    if yoy < -2 and yoy >= -5:
        return "Mild Decline"
    if yoy < -5:
        return "Deep Decline"
    return "Flat"


def generate_investment_note(name: str, metrics: dict, signal: str) -> str:
    mom = metrics["mom"]
    yoy = metrics["yoy"]
    accel = metrics["acceleration"]

    parts = []
    if signal in ("Strong Uptrend", "Moderate Uptrend"):
        parts.append(f"YoY {yoy:+.1f}% 상승 중")
        if accel > 0:
            parts.append("가속 구간 진입")
        else:
            parts.append("추세 전환 여부 모니터링")
    elif signal == "Reversal":
        parts.append(f"MoM {mom:+.1f}% 반등, YoY는 아직 {yoy:+.1f}%")
        parts.append("초기 반전 시그널 확인 필요")
    elif signal == "Momentum":
        parts.append(f"모멘텀 가속 중 (가속도 {accel:+.1f}%)")
    elif signal == "Cooling After Rise":
        parts.append(f"YoY {yoy:+.1f}% 상승했으나 MoM {mom:+.1f}%로 둔화")
        parts.append("조정 가능성 주시")
    elif signal in ("Mild Decline", "Deep Decline"):
        parts.append(f"YoY {yoy:+.1f}% 하락 중")
        if accel > 0:
            parts.append("하락 둔화 조짐")
        else:
            parts.append("추가 하락 리스크")
    else:
        parts.append(f"YoY {yoy:+.1f}%, 완만한 상승. 추세 전환 여부 모니터링.")

    return ", ".join(parts) + "."


def analyze_all(raw_data: dict) -> list[dict]:
    results = []
    for series_id, info in raw_data.items():
        metrics = compute_metrics(info["values"])
        if metrics is None:
            continue
        signal = classify_signal(metrics)
        note = generate_investment_note(info["name"], metrics, signal)
        results.append({
            "series_id": series_id,
            "category": info["category"],
            "name": info["name"],
            "kr_stocks": info["kr_stocks"],
            "drivers": info.get("drivers", ""),
            "risks": info.get("risks", ""),
            "signal": signal,
            "note": note,
            **metrics,
        })
    return results
