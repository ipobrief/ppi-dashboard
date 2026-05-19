"""PPI Market Sensing Dashboard - Streamlit App."""

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from config import CATEGORIES, SIGNAL_COLORS, SIGNAL_LABELS_KR, STOCK_CODES
from fred_fetcher import fetch_all_series, load_cached_data
from analyzer import analyze_all
import json
import os
import datetime

st.set_page_config(page_title="PPI Market Sensing Dashboard", layout="wide", page_icon="📊")


def linkify_kr_stocks(kr_stocks_str):
    """Convert comma-separated stock names to Toss Securities links."""
    if not kr_stocks_str:
        return ""
    parts = [s.strip() for s in kr_stocks_str.split(",")]
    linked = []
    for name in parts:
        code = STOCK_CODES.get(name)
        if code:
            linked.append(f'<a href="https://tossinvest.com/stocks/{code}/order" target="_blank" style="color:#4fc3f7;text-decoration:none;border-bottom:1px dotted #4fc3f7">{name}</a>')
        else:
            linked.append(name)
    return ", ".join(linked)


# --- Dark theme CSS ---
st.markdown("""
<style>
    .stApp { background-color: #0e1117; }
    .metric-card {
        background: #1a1d23;
        border-radius: 10px;
        padding: 15px;
        margin: 5px 0;
        border: 1px solid #2d2d2d;
    }
    .signal-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 13px;
        font-weight: 600;
        color: white;
    }
    .header-title {
        font-size: 28px;
        font-weight: 700;
        color: #e0e0e0;
        margin-bottom: 5px;
    }
    .header-sub {
        font-size: 14px;
        color: #888;
        margin-bottom: 20px;
    }
    .stat-label { color: #888; font-size: 12px; }
    .stat-value { color: #e0e0e0; font-size: 20px; font-weight: 700; }
    .stat-value.positive { color: #ff4444; }
    .stat-value.negative { color: #4488ff; }
    .note-box {
        background: #1e1e2e;
        border-left: 3px solid #ff8c00;
        padding: 12px;
        border-radius: 6px;
        margin-top: 10px;
        color: #d0d0d0;
        font-size: 14px;
    }
    .kr-box {
        background: #1e1e2e;
        border-left: 3px solid #6644cc;
        padding: 12px;
        border-radius: 6px;
        margin-top: 8px;
        color: #d0d0d0;
        font-size: 14px;
    }
    .drivers-box {
        background: #1a2e1a;
        border-left: 3px solid #44cc44;
        padding: 12px;
        border-radius: 6px;
        margin-top: 8px;
        color: #d0d0d0;
        font-size: 14px;
    }
    .risks-box {
        background: #2e1a1a;
        border-left: 3px solid #ff4444;
        padding: 12px;
        border-radius: 6px;
        margin-top: 8px;
        color: #d0d0d0;
        font-size: 14px;
    }
    div[data-testid="stHorizontalBlock"] > div { padding: 0 2px; }
    .category-chip {
        display: inline-block;
        padding: 6px 14px;
        border-radius: 16px;
        margin: 3px;
        font-size: 13px;
        cursor: pointer;
        border: 1px solid #444;
        color: #ccc;
        background: #1a1d23;
    }
    .category-chip.active {
        background: #ff8c00;
        color: white;
        border-color: #ff8c00;
    }
    .summary-badge {
        display: inline-block;
        padding: 8px 16px;
        border-radius: 8px;
        margin: 4px;
        font-size: 14px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)


def color_class(val):
    if val > 0:
        return "positive"
    elif val < 0:
        return "negative"
    return ""


def render_signal_badge(signal):
    color = SIGNAL_COLORS.get(signal, "#666")
    return f'<span class="signal-badge" style="background:{color}">{signal}</span>'


@st.cache_data(ttl=3600)
def load_and_analyze():
    raw = load_cached_data()
    if raw is None:
        raw = fetch_all_series(force=True)
    return analyze_all(raw), raw


def main():
    # --- Header ---
    st.markdown('<div class="header-title">📊 PPI Market Sensing Dashboard</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="header-sub">FRED Producer Price Index 기반 산업별 투자 기회 조기 감지 시스템 | {datetime.date.today()} | v1.0</div>',
        unsafe_allow_html=True,
    )

    # Check data
    try:
        results, raw_data = load_and_analyze()
    except ValueError as e:
        st.error(str(e))
        st.info("1. https://fred.stlouisfed.org/docs/api/api_key.html 에서 API Key 발급\n2. .env 파일 생성 후 FRED_API_KEY=your_key 입력\n3. 페이지 새로고침")
        return
    except Exception:
        st.warning("캐시된 데이터가 없습니다. 사이드바에서 '데이터 새로고침'을 클릭하세요.")
        with st.sidebar:
            if st.button("🔄 데이터 새로고침 (FRED API)"):
                with st.spinner("FRED에서 데이터를 가져오는 중..."):
                    raw = fetch_all_series(force=True)
                    st.rerun()
        return

    df = pd.DataFrame(results)
    if df.empty:
        st.warning("분석 가능한 데이터가 없습니다.")
        return

    # --- Sidebar ---
    with st.sidebar:
        st.markdown("### ⚙️ 설정")
        if st.button("🔄 데이터 새로고침"):
            with st.spinner("FRED에서 데이터를 가져오는 중..."):
                fetch_all_series(force=True)
                st.cache_data.clear()
                st.rerun()

        meta_path = os.path.join("data", "fetch_meta.json")
        if os.path.exists(meta_path):
            with open(meta_path) as f:
                meta = json.load(f)
            st.caption(f"마지막 업데이트: {meta['last_fetch'][:16]}")
            if meta.get("errors"):
                with st.expander(f"⚠️ 오류 {len(meta['errors'])}건"):
                    for err in meta["errors"]:
                        st.caption(err)

    # --- Summary badges ---
    signal_counts = df["signal"].value_counts().to_dict()
    total = len(df)
    categories_count = df["category"].nunique()

    opp_count = len(df[df["signal"].isin(["Strong Uptrend", "Moderate Uptrend", "Reversal", "Momentum"])])
    change_count = len(df[df["mom"].abs() > 0.5])

    components.html(f"""
    <style>
        body {{ margin: 0; padding: 0; background: transparent; font-family: 'Source Sans Pro', sans-serif; }}
        .badge-row {{ display: flex; gap: 12px; flex-wrap: wrap; }}
        .badge {{
            display: inline-block;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.15s, box-shadow 0.15s;
        }}
        .badge:hover {{ transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.4); }}
    </style>
    <div class="badge-row">
        <div class="badge" style="background:#1a3a5c;color:#4488ff;" onclick="clickTab(0)">🏭 카테고리 {categories_count}</div>
        <div class="badge" style="background:#1a3a2a;color:#44cc88;" onclick="clickTab(2)">📊 시리즈 {total}</div>
        <div class="badge" style="background:#3a2a1a;color:#ff8c00;" onclick="clickTab(1)">🎯 기회 탐지 {opp_count}건</div>
        <div class="badge" style="background:#2a1a3a;color:#cc88ff;" onclick="clickTab(3)">📋 시그널 변화 {change_count}건</div>
    </div>
    <script>
    function clickTab(idx) {{
        const tabs = window.parent.document.querySelectorAll('[data-baseweb="tab"]');
        if (tabs && tabs[idx]) {{
            tabs[idx].click();
            tabs[idx].scrollIntoView({{ behavior: 'smooth' }});
        }}
    }}
    </script>
    """, height=60)

    st.divider()

    # --- Tabs ---
    tab_overview, tab_opportunities, tab_signals, tab_weekly, tab_compare = st.tabs(
        ["🏭 Overview", "🎯 기회 탐지", "📊 전체 시그널", "📅 주간 변화", "📊 카테고리 비교"]
    )

    # ===== TAB: Overview =====
    with tab_overview:
        st.subheader("시그널 분포")
        signal_order = ["Strong Uptrend", "Moderate Uptrend", "Reversal", "Momentum", "Cooling After Rise", "Flat", "Mild Decline", "Deep Decline"]
        dist_cols = st.columns(len(signal_order))
        for i, sig in enumerate(signal_order):
            cnt = signal_counts.get(sig, 0)
            color = SIGNAL_COLORS.get(sig, "#666")
            dist_cols[i].markdown(
                f'<div style="text-align:center;padding:8px;border-radius:8px;border:1px solid {color}">'
                f'<div style="color:{color};font-size:20px;font-weight:700">{cnt}</div>'
                f'<div style="color:#999;font-size:11px">{sig}</div></div>',
                unsafe_allow_html=True,
            )

        st.subheader("카테고리별 평균 YoY 변동률")
        cat_avg = df.groupby("category")["yoy"].mean().sort_values(ascending=False).reset_index()
        fig = go.Figure(go.Bar(
            x=cat_avg["yoy"],
            y=cat_avg["category"],
            orientation="h",
            marker_color=[("#ff4444" if v > 0 else "#4488ff") for v in cat_avg["yoy"]],
        ))
        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="#0e1117",
            plot_bgcolor="#0e1117",
            height=500,
            margin=dict(l=0, r=20, t=20, b=20),
            xaxis_title="YoY %",
            yaxis=dict(autorange="reversed"),
        )
        st.plotly_chart(fig, use_container_width=True)

        st.caption("👆 카테고리를 클릭하면 전체 시그널 탭에서 해당 카테고리를 필터링합니다.")
        chip_cols = st.columns(min(len(cat_avg), 6))
        for i, row_cat in cat_avg.iterrows():
            col = chip_cols[i % min(len(cat_avg), 6)]
            if col.button(f"{row_cat['category']} ({row_cat['yoy']:+.1f}%)", key=f"ov_cat_{i}", use_container_width=True):
                st.query_params["cat"] = row_cat["category"]
                st.query_params["tab"] = "signals"
                st.rerun()

    # ===== TAB: Opportunities =====
    with tab_opportunities:
        opp_df = df[df["signal"].isin(["Strong Uptrend", "Moderate Uptrend", "Reversal", "Momentum"])].sort_values("yoy", ascending=False)
        st.subheader(f"🎯 투자 기회 탐지 ({len(opp_df)}건)")

        for _, row in opp_df.iterrows():
            with st.container():
                cols = st.columns([3, 2, 1, 1, 1, 1, 1])
                cols[0].markdown(f"**{row['name']}**<br><span style='color:#888;font-size:12px'>{row['category']}</span>", unsafe_allow_html=True)
                cols[1].markdown(render_signal_badge(row["signal"]), unsafe_allow_html=True)
                cols[2].metric("MOM", f"{row['mom']:+.1f}%")
                cols[3].metric("3M", f"{row['three_m']:+.1f}%")
                cols[4].metric("YOY", f"{row['yoy']:+.1f}%")
                cols[5].metric("모멘텀", f"{row['momentum']:+.1f}%")
                cols[6].metric("고점대비", f"{row['from_peak']:+.1f}%")

                note_cols = st.columns([1, 1])
                note_cols[0].markdown(f'<div class="note-box">📋 투자 노트: {row["note"]}</div>', unsafe_allow_html=True)
                note_cols[1].markdown(f'<div class="kr-box">🇰🇷 한국 연결: {linkify_kr_stocks(row["kr_stocks"])}</div>', unsafe_allow_html=True)

                ctx_cols = st.columns([1, 1])
                if row.get("drivers", ""):
                    ctx_cols[0].markdown(f'<div class="drivers-box">📈 상승 이유: {row["drivers"]}</div>', unsafe_allow_html=True)
                if row.get("risks", ""):
                    ctx_cols[1].markdown(f'<div class="risks-box">⚠️ 리스크: {row["risks"]}</div>', unsafe_allow_html=True)
                st.divider()

    # ===== TAB: All Signals =====
    with tab_signals:
        # Signal filter
        st.subheader("시그널 필터")
        all_signals = ["전체"] + [f"{s} ({signal_counts.get(s, 0)})" for s in ["Strong Uptrend", "Moderate Uptrend", "Reversal", "Momentum", "Cooling After Rise", "Flat", "Mild Decline", "Deep Decline"]]
        selected_signal_label = st.radio("", all_signals, horizontal=True, label_visibility="collapsed")

        if selected_signal_label == "전체":
            filtered_df = df
        else:
            sig_name = selected_signal_label.split(" (")[0]
            filtered_df = df[df["signal"] == sig_name]

        # Category filter
        all_cats = ["전체"] + sorted(df["category"].unique().tolist())
        default_cat = st.query_params.get("cat", "전체")
        default_cat_idx = all_cats.index(default_cat) if default_cat in all_cats else 0
        selected_cat = st.radio("카테고리", all_cats, index=default_cat_idx, horizontal=True, label_visibility="collapsed")
        if selected_cat != "전체":
            filtered_df = filtered_df[filtered_df["category"] == selected_cat]

        # Search
        search = st.text_input("시리즈명, 카테고리, 한국 투자 연결 검색...", placeholder="시리즈명, 카테고리, 한국 투자 연결 검색...")
        if search:
            mask = (
                filtered_df["name"].str.contains(search, case=False, na=False)
                | filtered_df["category"].str.contains(search, case=False, na=False)
                | filtered_df["kr_stocks"].str.contains(search, case=False, na=False)
            )
            filtered_df = filtered_df[mask]

        st.caption(f"전체 ({len(filtered_df)})")

        # Table + detail panel
        if not filtered_df.empty:
            left, right = st.columns([3, 2])

            with left:
                for idx, row in filtered_df.iterrows():
                    col1, col2, col3, col4, col5, col6, col7 = st.columns([2.5, 2, 1, 1, 1, 1, 1])
                    col1.markdown(f"<span style='color:#888;font-size:11px'>{row['category']}</span><br>**{row['name']}**<br><span style='color:#666;font-size:11px'>{linkify_kr_stocks(row['kr_stocks'])}</span>", unsafe_allow_html=True)
                    col2.markdown(render_signal_badge(row["signal"]), unsafe_allow_html=True)
                    col3.markdown(f"<span style='color:{'#ff4444' if row['mom']>0 else '#4488ff'}'>{row['mom']:+.1f}%</span>", unsafe_allow_html=True)
                    col4.markdown(f"<span style='color:{'#ff4444' if row['three_m']>0 else '#4488ff'}'>{row['three_m']:+.1f}%</span>", unsafe_allow_html=True)
                    col5.markdown(f"<span style='color:{'#ff4444' if row['yoy']>0 else '#4488ff'}'>{row['yoy']:+.1f}%</span>", unsafe_allow_html=True)
                    col6.markdown(f"<span style='color:{'#ff4444' if row['momentum']>0 else '#4488ff'}'>{row['momentum']:+.1f}%</span>", unsafe_allow_html=True)
                    col7.markdown(f"<span style='color:{'#ff4444' if row['from_peak']>0 else '#4488ff'}'>{row['from_peak']:+.1f}%</span>", unsafe_allow_html=True)

            with right:
                selected_name = st.selectbox("상세 보기", filtered_df["name"].tolist(), label_visibility="collapsed")
                sel = filtered_df[filtered_df["name"] == selected_name].iloc[0]

                st.markdown(f"### {sel['name']}")
                st.markdown(render_signal_badge(sel["signal"]), unsafe_allow_html=True)

                m1, m2 = st.columns(2)
                m1.markdown(f'<div class="metric-card"><div class="stat-label">YOY</div><div class="stat-value {color_class(sel["yoy"])}">{sel["yoy"]:+.1f}%</div></div>', unsafe_allow_html=True)
                m2.markdown(f'<div class="metric-card"><div class="stat-label">MOM</div><div class="stat-value {color_class(sel["mom"])}">{sel["mom"]:+.1f}%</div></div>', unsafe_allow_html=True)

                m3, m4 = st.columns(2)
                m3.markdown(f'<div class="metric-card"><div class="stat-label">가속도</div><div class="stat-value {color_class(sel["acceleration"])}">{sel["acceleration"]:+.1f}%</div></div>', unsafe_allow_html=True)
                m4.markdown(f'<div class="metric-card"><div class="stat-label">고점대비</div><div class="stat-value {color_class(sel["from_peak"])}">{sel["from_peak"]:+.1f}%</div></div>', unsafe_allow_html=True)

                m5, m6 = st.columns(2)
                m5.markdown(f'<div class="metric-card"><div class="stat-label">고점</div><div class="stat-value">{sel["peak_value"]} ({sel["peak_date"]})</div></div>', unsafe_allow_html=True)
                m6.markdown(f'<div class="metric-card"><div class="stat-label">저점</div><div class="stat-value">{sel["trough_value"]} ({sel["trough_date"]})</div></div>', unsafe_allow_html=True)

                st.markdown(f'<div class="note-box">📋 투자 노트: {sel["note"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="kr-box">🇰🇷 한국 연결: {linkify_kr_stocks(sel["kr_stocks"])}</div>', unsafe_allow_html=True)

                if sel.get("drivers"):
                    st.markdown(f'<div class="drivers-box">📈 상승 이유: {sel["drivers"]}</div>', unsafe_allow_html=True)
                if sel.get("risks"):
                    st.markdown(f'<div class="risks-box">⚠️ 리스크: {sel["risks"]}</div>', unsafe_allow_html=True)

                # Price chart
                series_id = sel["series_id"]
                if raw_data and series_id in raw_data:
                    vals = raw_data[series_id]["values"]
                    chart_df = pd.DataFrame(list(vals.items()), columns=["date", "value"])
                    chart_df["date"] = pd.to_datetime(chart_df["date"])
                    chart_df = chart_df.sort_values("date").tail(60)

                    fig = go.Figure(go.Scatter(
                        x=chart_df["date"], y=chart_df["value"],
                        mode="lines",
                        line=dict(color="#ff8c00", width=2),
                        fill="tozeroy",
                        fillcolor="rgba(255,140,0,0.1)",
                    ))
                    fig.update_layout(
                        template="plotly_dark",
                        paper_bgcolor="#1a1d23",
                        plot_bgcolor="#1a1d23",
                        height=250,
                        margin=dict(l=0, r=0, t=10, b=30),
                        xaxis=dict(showgrid=False),
                        yaxis=dict(showgrid=True, gridcolor="#2d2d2d"),
                    )
                    st.plotly_chart(fig, use_container_width=True)

    # ===== TAB: Weekly Changes =====
    with tab_weekly:
        st.subheader("📅 주간 주요 변화")
        changes = df[df["mom"].abs() > 0.5].sort_values("mom", ascending=False)

        if changes.empty:
            st.info("이번 달 유의미한 변동이 없습니다.")
        else:
            for _, row in changes.iterrows():
                direction = "🔺" if row["mom"] > 0 else "🔻"
                kr_links = f" | {linkify_kr_stocks(row['kr_stocks'])}" if row.get("kr_stocks") else ""
                st.markdown(
                    f"{direction} **{row['name']}** ({row['category']}) — MOM {row['mom']:+.1f}%, "
                    f"Signal: {render_signal_badge(row['signal'])}{kr_links}",
                    unsafe_allow_html=True,
                )

    # ===== TAB: Category Compare =====
    with tab_compare:
        st.subheader("📊 카테고리 비교")
        cat_metrics = df.groupby("category").agg(
            avg_yoy=("yoy", "mean"),
            avg_mom=("mom", "mean"),
            avg_momentum=("momentum", "mean"),
            count=("name", "count"),
        ).sort_values("avg_yoy", ascending=False).reset_index()

        fig = go.Figure()
        fig.add_trace(go.Bar(name="YOY %", x=cat_metrics["category"], y=cat_metrics["avg_yoy"],
                             marker_color="#ff4444"))
        fig.add_trace(go.Bar(name="MOM %", x=cat_metrics["category"], y=cat_metrics["avg_mom"],
                             marker_color="#ff8c00"))
        fig.add_trace(go.Bar(name="모멘텀", x=cat_metrics["category"], y=cat_metrics["avg_momentum"],
                             marker_color="#44cc88"))
        fig.update_layout(
            barmode="group",
            template="plotly_dark",
            paper_bgcolor="#0e1117",
            plot_bgcolor="#0e1117",
            height=500,
            margin=dict(l=0, r=20, t=20, b=100),
            xaxis_tickangle=-45,
        )
        st.plotly_chart(fig, use_container_width=True)

        st.dataframe(
            cat_metrics.style.format({"avg_yoy": "{:+.1f}%", "avg_mom": "{:+.1f}%", "avg_momentum": "{:+.1f}%"}),
            use_container_width=True,
        )


if __name__ == "__main__":
    main()
