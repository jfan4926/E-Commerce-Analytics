import streamlit as st
import streamlit.components.v1 as components

TABLEAU_URL = (
    "https://public.tableau.com/views/"
    "eCommerceAnalysis_17784694679280/OlistE-CommerceAnalytics"
)

def render():
    st.markdown("""
    <div style="margin-bottom:1.2rem;">
        <div style="font-size:1.1rem; font-weight:600; margin-bottom:0.3rem;">
            Tableau — Geospatial & AI Analytics
        </div>
        <div style="font-size:0.88rem; color:#6b7280;">
            Customer satisfaction across all 27 Brazilian states — live and interactive.
        </div>
    </div>
    """, unsafe_allow_html=True)

    components.html(
        f"""
        <script type="module"
            src="https://public.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js">
        </script>
        <tableau-viz
            id="tableauViz"
            src="{TABLEAU_URL}"
            width="100%"
            height="720"
            toolbar="bottom">
        </tableau-viz>
        """,
        height=740,
    )