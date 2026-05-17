import streamlit as st

CI_BADGE = (
    '<a href="https://github.com/jfan4926/E-Commerce-Analytics/actions" target="_blank">'
    '<img src="https://github.com/jfan4926/E-Commerce-Analytics/actions/workflows/'
    'ci.yml/badge.svg?branch=streamlit-deploy" style="vertical-align:middle;"/>'
    '</a>'
)

def render():
    st.markdown("""
    <div style="margin-bottom:1.5rem;">
        <div style="font-size:1.1rem; font-weight:600; margin-bottom:0.3rem;">Architecture</div>
        <div style="font-size:0.88rem; color:#6b7280;">
            Medallion pattern — raw ingestion through to BI-ready Star Schema on Azure.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Pipeline steps
    steps = [
        ("Raw Layer",    "Azure Blob Storage", "9 CSV tables from Kaggle ingested as data lake foundation"),
        ("Transform",    "Python / Pandas",    "Cleaning, feature engineering, Star Schema modeling"),
        ("Warehouse",    "Azure SQL Database", "1 fact table + 4 dimension tables via SQLAlchemy"),
        ("Presentation", "Power BI + Tableau", "Interactive dashboards with DAX measures"),
    ]

    cols = st.columns(4)
    for col, (label, title, desc) in zip(cols, steps):
        col.markdown(f"""
        <div style="padding:1.2rem 1rem; background:#f9fafb; border:1px solid #e5e7eb;
                    border-radius:4px; height:100%;">
            <div style="font-family:monospace; font-size:0.65rem; color:#9ca3af;
                        letter-spacing:0.08em; text-transform:uppercase; margin-bottom:0.4rem;">
                {label}
            </div>
            <div style="font-size:0.85rem; font-weight:600; margin-bottom:0.3rem;">{title}</div>
            <div style="font-size:0.78rem; color:#6b7280; line-height:1.5;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/>**Planned additions**", unsafe_allow_html=True)

    roadmap = [
        {
            "title":  "dbt Core",
            "desc":   "Version-controlled SQL models with staging → marts layer and automated tests.",
            "color":  "#2563eb",
            "status": "In Progress",
            "badge":  "",
        },
        {
            "title":  "GitHub Actions CI",
            "desc":   "Automated pytest runs on every push — 5 unit tests validate the Bayesian A/B testing engine.",
            "color":  "#16a34a",
            "status": "Live ✅",
            "badge":  CI_BADGE,
        },
        {
            "title":  "Text-to-SQL Agent",
            "desc":   "Ask questions in plain English, get SQL results + plain-English explanations.",
            "color":  "#2563eb",
            "status": "In Progress",
            "badge":  "",
        },
        {
            "title":  "A/B Testing",
            "desc":   "Bayesian experiment framework — significance testing and posterior plots.",
            "color":  "#16a34a",
            "status": "Live ✅",
            "badge":  "",
        },
    ]

    c1, c2 = st.columns(2)
    for i, item in enumerate(roadmap):
        col    = c1 if i % 2 == 0 else c2
        color  = item["color"]
        status = item["status"]
        title  = item["title"]
        desc   = item["desc"]
        badge  = item["badge"]

        if color == "#16a34a":
            bg, tc, bc = "#f0fdf4", "#166534", "#bbf7d0"
        elif color == "#2563eb":
            bg, tc, bc = "#eff6ff", "#1d4ed8", "#bfdbfe"
        else:
            bg, tc, bc = "#f3f4f6", "#6b7280", "#e5e7eb"

        status_row = (
                f'<span style="font-family:monospace; font-size:0.65rem; padding:0.2rem 0.5rem;'
                f'border-radius:2px; display:inline-block;'
                f'background:{bg}; color:{tc}; border:1px solid {bc};">'
                f'{status}</span>'
            )
        if badge:
            status_row += '&nbsp;&nbsp;' + badge

        col.markdown(
            f'<div style="padding:1.2rem 1.4rem; border:1px solid #e5e7eb;'
            f'border-top:3px solid {color}; border-radius:0 0 4px 4px; margin-bottom:1rem;">'
            f'<div style="display:flex; align-items:center; margin-bottom:0.6rem;">{status_row}</div>'
            f'<div style="font-size:0.9rem; font-weight:600; margin-bottom:0.4rem;">{title}</div>'
            f'<div style="font-size:0.82rem; color:#4b5563; line-height:1.6;">{desc}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    col.markdown("<div style='margin-bottom:0.8rem;'></div>", unsafe_allow_html=True)

    # Star Schema
    st.markdown("<br/>**Star Schema**", unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:4px;
                padding:1.5rem; font-family:monospace; font-size:0.82rem;
                color:#6b7280; line-height:2.2; text-align:center;">
        dim_customers<br/>│<br/>
        dim_sellers ──── <strong style="color:#1a1a1a;">fact_orders</strong> ──── dim_products<br/>
        │<br/>dim_date
    </div>
    """, unsafe_allow_html=True)