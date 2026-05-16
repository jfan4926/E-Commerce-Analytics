import streamlit as st

def render():
    st.markdown("""
    <div style="margin-bottom:1.5rem;">
        <div style="font-size:1.1rem; font-weight:600; margin-bottom:0.3rem;">Architecture</div>
        <div style="font-size:0.88rem; color:#6b7280;">
            Medallion pattern — raw ingestion through to BI-ready Star Schema on Azure.
        </div>
    </div>
    """, unsafe_allow_html=True)

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
        ("dbt Core",          "Version-controlled SQL models with staging → marts layer and automated tests.", "#2563eb", "In Progress"),
        ("GitHub Actions",    "CI/CD: runs `dbt build` + `pytest` on every PR automatically.",                "#2563eb", "In Progress"),
        ("Text-to-SQL Agent", "Ask questions in plain English, get SQL results + plain-English explanations.", "#9ca3af", "Planned"),
        ("A/B Testing",       "Bayesian experiment framework — significance testing and posterior plots.",      "#9ca3af", "Planned"),
    ]

    c1, c2 = st.columns(2)
    for i, (title, desc, color, status) in enumerate(roadmap):
        col = c1 if i % 2 == 0 else c2
        bg = "#eff6ff" if color == "#2563eb" else "#f3f4f6"
        tc = "#1d4ed8" if color == "#2563eb" else "#6b7280"
        bc = "#bfdbfe" if color == "#2563eb" else "#e5e7eb"
        col.markdown(f"""
        <div style="padding:1.2rem 1.4rem; border:1px solid #e5e7eb;
                    border-top:3px solid {color}; border-radius:0 0 4px 4px; margin-bottom:1rem;">
            <span style="font-family:monospace; font-size:0.65rem; padding:0.2rem 0.5rem;
                         border-radius:2px; display:inline-block; margin-bottom:0.6rem;
                         background:{bg}; color:{tc}; border:1px solid {bc};">
                {status}
            </span>
            <div style="font-size:0.9rem; font-weight:600; margin-bottom:0.4rem;">{title}</div>
            <div style="font-size:0.82rem; color:#4b5563; line-height:1.6;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("**Star Schema**")
    st.markdown("""
    <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:4px;
                padding:1.5rem; font-family:monospace; font-size:0.82rem;
                color:#6b7280; line-height:2.2; text-align:center;">
        dim_customers<br/>│<br/>
        dim_sellers ──── <strong style="color:#1a1a1a;">fact_orders</strong> ──── dim_products<br/>
        │<br/>dim_date
    </div>
    """, unsafe_allow_html=True)