import streamlit as st

st.set_page_config(
    page_title="E-Commerce Analytics",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');
html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; padding-left: 3rem; padding-right: 3rem; }.stTabs [data-baseweb="tab-list"] { gap: 0; border-bottom: 1px solid #e5e7eb; }
.stTabs [data-baseweb="tab"] {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.78rem;
    padding: 0.6rem 1.2rem; color: #6b7280;
    border-bottom: 2px solid transparent;
}
.stTabs [aria-selected="true"] { color: #1a1a1a; border-bottom: 2px solid #1a1a1a; }
[data-testid="metric-container"] {
    background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 4px; padding: 1rem;
}
.chip {
    display: inline-block; font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem; padding: 0.2rem 0.55rem; border-radius: 3px;
    background: #f3f4f6; color: #374151; border: 1px solid #e5e7eb; margin: 0.15rem;
}
.chip-blue { background: #eff6ff; color: #1d4ed8; border-color: #bfdbfe; }
[data-testid="stSidebar"] { display: none; }
[data-testid="collapsedControl"] { display: none; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style="border-bottom:1px solid #e5e7eb; padding-bottom:1rem; margin-bottom:2rem;
            display:flex; justify-content:space-between; align-items:center;">
    <span style="font-family:'IBM Plex Mono',monospace; font-size:0.85rem; color:#6b7280;">
        ecommerce-analytics
    </span>
    <span style="font-size:0.85rem;">
        <a href="https://public.tableau.com/app/profile/jo.f5042/viz/eCommerceAnalysis_17784694679280/OlistE-CommerceAnalytics"
           target="_blank" style="color:#2563eb; text-decoration:none; margin-right:1.5rem;">
           Live Dashboard
        </a>
        <a href="https://github.com/jfan4926/E-Commerce-Analytics"
           target="_blank" style="color:#2563eb; text-decoration:none;">
           GitHub
        </a>
    </span>
</div>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<p style="font-family:'IBM Plex Mono',monospace; font-size:0.75rem; color:#6b7280;
          letter-spacing:0.08em; text-transform:uppercase; margin-bottom:0.8rem;">
    Personal Project · Data Analytics
</p>
<h1 style="font-size:2.2rem; font-weight:600; letter-spacing:-0.02em; line-height:1.15; margin-bottom:0.8rem;">
    E-Commerce Analytics<br/>Platform
</h1>
<p style="font-size:1rem; color:#4b5563; max-width:580px; font-weight:300; margin-bottom:1.5rem;">
    End-to-end analytics pipeline on 100K+ real orders from Brazil's largest
    e-commerce platform — cloud data warehouse, interactive dashboards, and
    AI-powered review classification.
</p>
<div style="margin-bottom:2rem;">
    <span class="chip">Python</span>
    <span class="chip">Azure SQL</span>
    <span class="chip">Star Schema</span>
    <span class="chip">Power BI</span>
    <span class="chip">Tableau Public</span>
    <span class="chip">Claude API</span>
    <span class="chip">Pandas</span>
    <span class="chip chip-blue">dbt · in progress</span>
    <span class="chip chip-blue">AI Agent · coming</span>
    <span class="chip chip-blue">A/B Testing · coming</span>
</div>
""", unsafe_allow_html=True)

# Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total GMV", "$15.4M")
col2.metric("Orders Analyzed", "96,500")
col3.metric("Reviews via AI", "4,556")
col4.metric("Delay Rate", "7.57%")

st.markdown("<br/>", unsafe_allow_html=True)

# Tabs
tab_powerbi, tab_tableau, tab_sentiment, tab_agent, tab_abtest, tab_arch = st.tabs([
    "📊  Power BI",
    "📈  Tableau",
    "🤖  AI Sentiment",
    "💬  AI Agent",
    "🧪  A/B Testing",
    "🏗  Architecture",
])

with tab_powerbi:
    from pages.powerbi import render
    render()

with tab_tableau:
    from pages.tableau import render
    render()

with tab_sentiment:
    from pages.sentiment import render
    render()

with tab_agent:
    from pages.agent import render
    render()

with tab_abtest:
    from pages.ab_test import render
    render()

with tab_arch:
    from pages.architecture import render
    render()

    # ── Footer ───────────────────────────────────────────────────────────────────
st.markdown("<br/><br/>", unsafe_allow_html=True)
st.markdown("""
<div style="border-top:1px solid #e5e7eb; padding-top:1.2rem; margin-top:1rem;
            font-family:'IBM Plex Mono',monospace; font-size:0.72rem; color:#9ca3af;
            display:flex; justify-content:space-between; align-items:center;">
    <span>
        Data: <a href="https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce"
               target="_blank" style="color:#9ca3af; text-decoration:underline;">
               Olist Brazilian E-Commerce (Kaggle)</a>
        &nbsp;·&nbsp;
        For portfolio demonstration purposes only
    </span>
    <a href="https://github.com/jfan4926/E-Commerce-Analytics"
       target="_blank" style="color:#9ca3af; text-decoration:underline;">
        github.com/jfan4926
    </a>
</div>
""", unsafe_allow_html=True)