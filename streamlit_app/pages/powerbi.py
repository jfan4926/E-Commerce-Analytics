import streamlit as st

POWERBI_PAGES = [
    {
        "img": "powerbi_page1.png",
        "title": "Executive Overview",
        "desc": "$15.42M GMV, 96K orders, monthly trend showing 2017 5x growth and a $1.55M Black Friday peak. Top 10 categories by GMV and review score side by side.",
    },
    {
        "img": "powerbi_page2.png",
        "title": "Delivery & Satisfaction",
        "desc": "Orders delayed 3+ days see 1-star rates jump from 19% to 54%. Northern states (RR, AP, AM) average 25+ days vs the 12-day national average.",
    },
    {
        "img": "powerbi_page3.png",
        "title": "AI-Powered Insights",
        "desc": "Claude API classifies 4,556 Portuguese reviews. Wrong/missing items (37%) surpass delivery delays as the top complaint — only discoverable through text analysis.",
    },
]

def render():
    st.markdown("""
    <div style="margin-bottom:1.2rem;">
        <div style="font-size:1.1rem; font-weight:600; margin-bottom:0.3rem;">Power BI Dashboards</div>
        <div style="font-size:0.88rem; color:#6b7280;">
            Three pages, each answering a distinct business question.
        </div>
    </div>
    """, unsafe_allow_html=True)

    for page in POWERBI_PAGES:
        st.markdown(f"""
        <div style="border:1px solid #e5e7eb; border-radius:4px; overflow:hidden; margin-bottom:0.5rem;">
            <div style="padding:1rem 1.2rem; display:flex; justify-content:space-between;
                        align-items:center; border-bottom:1px solid #e5e7eb;">
                <div>
                    <div style="font-size:0.95rem; font-weight:600; margin-bottom:0.2rem;">{page['title']}</div>
                    <div style="font-size:0.82rem; color:#4b5563; line-height:1.6;">{page['desc']}</div>
                </div>
                <span style="font-family:monospace; font-size:0.65rem; padding:0.2rem 0.5rem;
                             border-radius:2px; background:#fef3c7; color:#92400e;
                             border:1px solid #fde68a; white-space:nowrap; margin-left:1rem;">
                    Power BI
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.image(page["img"], use_container_width=True)