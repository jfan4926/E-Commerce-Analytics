import streamlit as st
import pandas as pd

COMPLAINT_DATA = {
    "Category": [
        "Wrong / Missing Item",
        "Delivery Delay",
        "Product Quality",
        "No Response",
        "Damaged Item",
        "Other",
    ],
    "Pct": [36.7, 33.3, 15.6, 6.3, 4.5, 3.6],
    "Color": ["#2563eb", "#16a34a", "#d97706", "#dc2626", "#7c3aed", "#9ca3af"],
}

INTENSITY_DATA = {
    "Score": [1, 2, 3, 4, 5],
    "Label": ["Very negative", "Negative", "Neutral", "Positive", "Very positive"],
    "Count": [1820, 1102, 634, 621, 379],
}

def render():
    st.markdown("""
    <div style="margin-bottom:1.5rem;">
        <div style="font-size:1.1rem; font-weight:600; margin-bottom:0.3rem;">
            AI-Powered Review Classification
        </div>
        <div style="font-size:0.88rem; color:#6b7280; max-width:620px;">
            4,556 Portuguese reviews classified by Claude API using structured JSON prompts —
            complaint category, sentiment intensity (1–5), and seller fault attribution.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="padding:0.9rem 1.2rem; background:#eff6ff; border-left:3px solid #2563eb;
                border-radius:0 4px 4px 0; font-size:0.82rem; color:#1e40af; margin-bottom:1.5rem;">
        <strong>Methodology:</strong> A stratified sample of 4,556 reviews was classified
        via Claude API (claude-haiku-4-5). Portuguese text was processed natively —
        no translation step required.
    </div>
    """, unsafe_allow_html=True)

    # Complaint breakdown
    st.markdown("#### Complaint Categories")
    df = pd.DataFrame(COMPLAINT_DATA)

    for _, row in df.iterrows():
        col_label, col_bar, col_pct = st.columns([3, 6, 1])
        col_label.markdown(
            f"<div style='font-size:0.82rem; padding-top:0.3rem;'>{row['Category']}</div>",
            unsafe_allow_html=True,
        )
        col_bar.markdown(
            f"""
            <div style="background:#f3f4f6; border-radius:3px; height:22px; margin-top:0.2rem;">
                <div style="width:{row['Pct'] * 2}%; background:{row['Color']};
                            height:100%; border-radius:3px;"></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        col_pct.markdown(
            f"<div style='font-size:0.82rem; font-family:monospace; padding-top:0.3rem;'>{row['Pct']}%</div>",
            unsafe_allow_html=True,
        )

    st.markdown("<br/>", unsafe_allow_html=True)

    # Key findings
    col_a, col_b = st.columns(2)
    col_a.markdown("""
    <div style="padding:1.2rem 1.4rem; border:1px solid #e5e7eb; border-radius:4px; border-left:3px solid #16a34a;">
        <span style="font-family:monospace; font-size:1.4rem; font-weight:500; color:#16a34a; display:block; margin-bottom:0.2rem;">37%</span>
        <div style="font-size:0.85rem; font-weight:600; margin-bottom:0.3rem;">Wrong Items = #1 Complaint</div>
        <div style="font-size:0.8rem; color:#6b7280;">Fulfillment errors outrank delivery delays — invisible without NLP.</div>
    </div>
    """, unsafe_allow_html=True)

    col_b.markdown("""
    <div style="padding:1.2rem 1.4rem; border:1px solid #e5e7eb; border-radius:4px; border-left:3px solid #2563eb;">
        <span style="font-family:monospace; font-size:1.4rem; font-weight:500; color:#2563eb; display:block; margin-bottom:0.2rem;">93.8%</span>
        <div style="font-size:0.85rem; font-weight:600; margin-bottom:0.3rem;">Seller Fault Rate</div>
        <div style="font-size:0.8rem; color:#6b7280;">Almost all 1-star reviews trace back to seller-side issues.</div>
    </div>
    """, unsafe_allow_html=True)

    # Intensity distribution
    st.markdown("<br/>#### Sentiment Intensity", unsafe_allow_html=True)
    intensity_df = pd.DataFrame(INTENSITY_DATA)
    total = intensity_df["Count"].sum()
    colors = ["#dc2626", "#f97316", "#9ca3af", "#16a34a", "#2563eb"]

    for i, row in intensity_df.iterrows():
        pct = row["Count"] / total * 100
        c1, c2, c3, c4 = st.columns([1, 3, 5, 1])
        c1.markdown(f"<div style='font-family:monospace; padding-top:0.2rem;'>★ {row['Score']}</div>", unsafe_allow_html=True)
        c2.markdown(f"<div style='font-size:0.82rem; color:#6b7280; padding-top:0.25rem;'>{row['Label']}</div>", unsafe_allow_html=True)
        c3.markdown(
            f"""<div style="background:#f3f4f6; border-radius:3px; height:22px; margin-top:0.2rem;">
                <div style="width:{pct*2}%; background:{colors[i]}; height:100%; border-radius:3px;"></div>
            </div>""",
            unsafe_allow_html=True,
        )
        c4.markdown(f"<div style='font-size:0.82rem; font-family:monospace; padding-top:0.2rem; color:#6b7280;'>{row['Count']:,}</div>", unsafe_allow_html=True)