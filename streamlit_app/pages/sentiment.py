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

REVIEW_SAMPLES = [
    {
        "original": "o película que recebi apesar de vir identificada a \"caneta\" como sendo para um CELULAR LG K10 - é inadequada para o modelo por ser pequena, não a instalei pois ficaria rídicula.",
        "category": "wrong_or_missing_item",
        "intensity": 3,
        "seller_fault": True,
        "summary": "The screen protector received was labeled for LG K10 but is too small and inadequate for the actual phone model.",
        "stars": 1,
    },
    {
        "original": "Produto com prazo largo de entrega e ainda assim dois dias após o prazo previsto, não entregaram e nem há informação sobre onde este se encontra, conforme informação do rastreamento.",
        "category": "delivery_delay",
        "intensity": 4,
        "seller_fault": True,
        "summary": "Product arrived 8 days late with no tracking information or communication about its whereabouts.",
        "stars": 1,
    },
    {
        "original": "Além de a entrega ter atrasado 1 semana o produto não veio funcionando e a caixa que veio o produto era de amaciante de roupas. Devolvi e não compro nunca mais nessa loja!",
        "category": "product_quality",
        "intensity": 5,
        "seller_fault": True,
        "summary": "Product arrived non-functional and in wrong packaging (fabric softener box), with delivery also delayed by one week.",
        "stars": 1,
    },
    {
        "original": "Estou aguardando meu produto até hoje. Paguei o valor do frete exigido.",
        "category": "delivery_delay",
        "intensity": 3,
        "seller_fault": True,
        "summary": "Customer is still waiting for their product 14 days after the expected delivery date despite having paid for shipping.",
        "stars": 1,
    },
    {
        "original": "Anunciam um produto de uma marca entregam de outra inclusive não me deram uma resposta sobre o outro produto que comprei trata-se de uma fonte para Xbox 360 no anúncio original chegou um similar e ai?",
        "category": "wrong_or_missing_item",
        "intensity": 4,
        "seller_fault": True,
        "summary": "Customer received a similar product from a different brand than advertised, and seller has not responded about another purchased product.",
        "stars": 1,
    },
    {
        "original": "A caixa estava violada, o trocador estava sujo nas extremidades, assim como dois pés da banheira e a mangueira estava presa com fita crepe. Minha impressão é que o produto estava no mostruário.",
        "category": "product_quality",
        "intensity": 4,
        "seller_fault": True,
        "summary": "Product arrived with visible damage — violated box, dirty components, hose secured with duct tape, suggesting it was a display model.",
        "stars": 1,
    },
]

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
   
    # ── Real review samples ───────────────────────────────────────────────
    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown("#### Claude API — Live Classification Examples")
    st.markdown(
        "<div style='font-size:0.82rem; color:#6b7280; margin-bottom:1rem;'>"
        "Sample reviews processed through <code>claude-haiku-4-5</code> with structured JSON prompts. "
        "Each review returns category, intensity (1–5), English summary, and seller fault attribution."
        "</div>",
        unsafe_allow_html=True,
    )

    intensity_color = {1: "#16a34a", 2: "#65a30d", 3: "#d97706", 4: "#ea580c", 5: "#dc2626"}

    for review in REVIEW_SAMPLES:
        stars_str  = "★" * review["stars"] + "☆" * (5 - review["stars"])
        icolor     = intensity_color[review["intensity"]]
        fault_html = (
            "<span style='background:#fee2e2; color:#991b1b; border:1px solid #fecaca;"
            "font-size:0.65rem; padding:0.15rem 0.4rem; border-radius:2px; margin-left:0.4rem;'>"
            "Seller fault</span>"
        ) if review["seller_fault"] else ""

        top = (
            "<div style='padding:1rem 1.2rem; background:#f9fafb; border-bottom:1px solid #e5e7eb;'>"
            "<div style='font-size:0.7rem; font-family:monospace; color:#9ca3af;"
            "text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.4rem;'>"
            "Original review (Portuguese)</div>"
            f"<div style='font-size:0.88rem; color:#1a1a1a; line-height:1.6; font-style:italic;'>"
            f"&ldquo;{review['original']}&rdquo;</div>"
            f"<div style='margin-top:0.5rem; color:#d97706; font-size:0.9rem;'>{stars_str}</div>"
            "</div>"
        )

        bottom = (
            "<div style='padding:1rem 1.2rem; display:flex; flex-wrap:wrap; gap:1.5rem;'>"
            "<div>"
            "<div style='font-size:0.65rem; font-family:monospace; color:#9ca3af;"
            "text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.3rem;'>Category</div>"
            f"<div style='font-size:0.82rem; font-weight:600;'>{review['category']}{fault_html}</div>"
            "</div>"
            "<div>"
            "<div style='font-size:0.65rem; font-family:monospace; color:#9ca3af;"
            "text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.3rem;'>Sentiment Intensity</div>"
            f"<div style='font-size:0.82rem; font-weight:600; color:{icolor};'>{review['intensity']} / 5</div>"
            "</div>"
            "<div style='flex:1; min-width:200px;'>"
            "<div style='font-size:0.65rem; font-family:monospace; color:#9ca3af;"
            "text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.3rem;'>Claude Summary (English)</div>"
            f"<div style='font-size:0.82rem; color:#4b5563;'>{review['summary']}</div>"
            "</div>"
            "</div>"
        )

        st.markdown(
            "<div style='border:1px solid #e5e7eb; border-radius:4px; "
            f"overflow:hidden; margin-bottom:0.8rem;'>{top}{bottom}</div>",
            unsafe_allow_html=True,
        )

    with st.expander("View prompt sent to Claude API"):
        st.code('''{
  "model": "claude-haiku-4-5",
  "max_tokens": 200,
  "messages": [{
    "role": "user",
    "content": "Analyze this Portuguese e-commerce review and return JSON only:\\n\\n<review_text>\\n\\nReturn:\\n{\\n  \\"complaint_category\\": string,\\n  \\"sentiment_intensity\\": 1-5,\\n  \\"key_issue_english\\": string,\\n  \\"is_seller_fault\\": boolean\\n}"
  }]
}''', language="json")