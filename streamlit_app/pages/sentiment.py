import streamlit as st
import streamlit.components.v1 as components

REVIEW_SAMPLES = [
    {
        "original": "Bem comprei esse quadro pela targaryen,e solicitei troca imediatamente,quadro parecido com o do anúncio no entanto apresenta impressão sem qualidade,sem foco imagem trêmula,o material da tela terrível.",
        "category": "product_quality",
        "intensity": 4,
        "seller_fault": True,
        "summary": "Received a poster with poor print quality, blurry image, and low-quality canvas that does not match the advertisement.",
        "stars": 1,
    },
    {
        "original": "comprei 2 kits de 3 magnésio dimalato cada, totalizando 6 frascos. me entregaram somente 1 kit com 3 frascos",
        "category": "wrong_or_missing_item",
        "intensity": 4,
        "seller_fault": True,
        "summary": "Customer ordered 2 kits (6 bottles total) but received only 1 kit with 3 bottles.",
        "stars": 1,
    },
    {
        "original": "a entrega demorou e o produto chegou com defeito",
        "category": "damaged_item",
        "intensity": 4,
        "seller_fault": True,
        "summary": "Customer received a defective product after a delivery delay.",
        "stars": 1,
    },
    {
        "original": "Não testei o produto ainda, mas ele veio correto e em boas condições. Apenas a caixa que veio bem amassada e danificada, o que ficará chato, pois se trata de um presente.",
        "category": "damaged_item",
        "intensity": 2,
        "seller_fault": False,
        "summary": "Product arrived intact but packaging was badly crushed — a concern as it was intended as a gift.",
        "stars": 4,
    },
    {
        "original": "O produto foi exatamente o que eu esperava e estava descrito no site e chegou bem antes da data prevista.",
        "category": "positive_experience",
        "intensity": 1,
        "seller_fault": False,
        "summary": "Product matched description exactly and arrived well ahead of schedule. Customer fully satisfied.",
        "stars": 5,
    },
    {
        "original": "Lindos. Acabamento incrivel, muiro macios e super em conta.",
        "category": "positive_experience",
        "intensity": 1,
        "seller_fault": False,
        "summary": "Products are beautiful with incredible finish, very soft, and excellent value for money.",
        "stars": 5,
    },
    {
        "original": "Ficou tudo ok só pensei q fosse maior mas.ta bom",
        "category": "product_quality",
        "intensity": 2,
        "seller_fault": False,
        "summary": "Product is fine overall but smaller than expected — minor disappointment, still acceptable.",
        "stars": 5,
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

    # ── Complaint breakdown + Sentiment Intensity ─────────────────────────
    st.markdown("#### Complaint Categories")
    components.html("""
<!DOCTYPE html><html><head>
<style>
  * { box-sizing:border-box; margin:0; padding:0; }
  body { font-family:sans-serif; background:transparent; padding:4px 0; }
  .section-title { font-size:0.72rem; font-family:monospace; color:#9ca3af;
      text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.8rem; }
  .bar-row { display:flex; align-items:center; gap:0.8rem; margin-bottom:0.6rem; }
  .bar-label { font-size:0.82rem; color:#374151; width:160px; flex-shrink:0; }
  .bar-track { flex:1; background:#f3f4f6; border-radius:3px; height:20px; overflow:hidden; }
  .bar-pct   { font-family:monospace; font-size:0.78rem; color:#6b7280; width:42px; text-align:right; flex-shrink:0; }
  .int-score { font-family:monospace; font-size:0.85rem; width:36px; flex-shrink:0; }
  .int-label { font-size:0.78rem; color:#6b7280; width:110px; flex-shrink:0; }
  .int-count { font-family:monospace; font-size:0.78rem; color:#9ca3af; width:42px; text-align:right; flex-shrink:0; }
  .divider   { border:none; border-top:1px solid #e5e7eb; margin:1.2rem 0; }
  @keyframes grow { from { width:0% } to { width:var(--w) } }
  .bar-fill { height:100%; border-radius:3px; width:var(--w);
              animation: grow 1.4s cubic-bezier(0.22,1,0.36,1) both; }
</style>
</head><body>

<div class="bar-row"><div class="bar-label">Wrong / Missing Item</div>
  <div class="bar-track"><div class="bar-fill" style="--w:73.4%;background:#2563eb;animation-delay:0.1s"></div></div>
  <div class="bar-pct">36.7%</div></div>
<div class="bar-row"><div class="bar-label">Delivery Delay</div>
  <div class="bar-track"><div class="bar-fill" style="--w:66.6%;background:#16a34a;animation-delay:0.2s"></div></div>
  <div class="bar-pct">33.3%</div></div>
<div class="bar-row"><div class="bar-label">Product Quality</div>
  <div class="bar-track"><div class="bar-fill" style="--w:31.2%;background:#d97706;animation-delay:0.3s"></div></div>
  <div class="bar-pct">15.6%</div></div>
<div class="bar-row"><div class="bar-label">No Response</div>
  <div class="bar-track"><div class="bar-fill" style="--w:12.6%;background:#dc2626;animation-delay:0.4s"></div></div>
  <div class="bar-pct">6.3%</div></div>
<div class="bar-row"><div class="bar-label">Damaged Item</div>
  <div class="bar-track"><div class="bar-fill" style="--w:9%;background:#7c3aed;animation-delay:0.5s"></div></div>
  <div class="bar-pct">4.5%</div></div>
<div class="bar-row"><div class="bar-label">Other</div>
  <div class="bar-track"><div class="bar-fill" style="--w:7.2%;background:#9ca3af;animation-delay:0.6s"></div></div>
  <div class="bar-pct">3.6%</div></div>

<hr class="divider"/>
<div class="section-title">Sentiment Intensity</div>

<div class="bar-row"><div class="int-score">★ 1</div><div class="int-label">Very negative</div>
  <div class="bar-track"><div class="bar-fill" style="--w:78.4%;background:#dc2626;animation-delay:0.7s"></div></div>
  <div class="int-count">1,820</div></div>
<div class="bar-row"><div class="int-score">★ 2</div><div class="int-label">Negative</div>
  <div class="bar-track"><div class="bar-fill" style="--w:47.5%;background:#f97316;animation-delay:0.8s"></div></div>
  <div class="int-count">1,102</div></div>
<div class="bar-row"><div class="int-score">★ 3</div><div class="int-label">Neutral</div>
  <div class="bar-track"><div class="bar-fill" style="--w:27.3%;background:#9ca3af;animation-delay:0.9s"></div></div>
  <div class="int-count">634</div></div>
<div class="bar-row"><div class="int-score">★ 4</div><div class="int-label">Positive</div>
  <div class="bar-track"><div class="bar-fill" style="--w:26.7%;background:#16a34a;animation-delay:1.0s"></div></div>
  <div class="int-count">621</div></div>
<div class="bar-row"><div class="int-score">★ 5</div><div class="int-label">Very positive</div>
  <div class="bar-track"><div class="bar-fill" style="--w:16.3%;background:#2563eb;animation-delay:1.1s"></div></div>
  <div class="int-count">379</div></div>

</body></html>
""", height=440)

    st.markdown("<br/>", unsafe_allow_html=True)

    # ── Key findings ──────────────────────────────────────────────────────
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

    # ── Review samples ────────────────────────────────────────────────────
    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown("#### Claude API — Live Classification Examples")
    st.markdown(
        "<div style='font-size:0.82rem; color:#6b7280; margin-bottom:1rem;'>"
        "Sample reviews processed through <code>claude-haiku-4-5</code> with structured JSON prompts. "
        "Negative reviews (1-star) were classified via Claude API. "
        "Positive examples are included for contrast to demonstrate the full sentiment spectrum."
        "</div>",
        unsafe_allow_html=True,
    )

    intensity_color = {1: "#16a34a", 2: "#65a30d", 3: "#d97706", 4: "#ea580c", 5: "#dc2626"}

    for review in REVIEW_SAMPLES:
        stars_str = "★" * review["stars"] + "☆" * (5 - review["stars"])
        icolor    = intensity_color[review["intensity"]]
        fault_html = (
            "<span style='background:#fee2e2;color:#991b1b;border:1px solid #fecaca;"
            "font-size:0.65rem;padding:0.15rem 0.4rem;border-radius:2px;margin-left:0.4rem;'>"
            "Seller fault</span>"
        ) if review["seller_fault"] else ""

        top = (
            "<div style='padding:1rem 1.2rem;background:#f9fafb;border-bottom:1px solid #e5e7eb;'>"
            "<div style='font-size:0.7rem;font-family:monospace;color:#9ca3af;"
            "text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;'>"
            "Original review (Portuguese)</div>"
            f"<div style='font-size:0.88rem;color:#1a1a1a;line-height:1.6;font-style:italic;'>"
            f"&ldquo;{review['original']}&rdquo;</div>"
            f"<div style='margin-top:0.5rem;color:#d97706;font-size:0.9rem;'>{stars_str}</div>"
            "</div>"
        )
        bottom = (
            "<div style='padding:1rem 1.2rem;display:flex;flex-wrap:wrap;gap:1.2rem;'>"
            "<div style='min-width:120px;'>"
            "<div style='font-size:0.65rem;font-family:monospace;color:#9ca3af;"
            "text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.3rem;'>Category</div>"
            f"<div style='font-size:0.82rem;font-weight:600;'>{review['category']}{fault_html}</div>"
            "</div>"
            "<div style='min-width:120px;'>"
            "<div style='font-size:0.65rem;font-family:monospace;color:#9ca3af;"
            "text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.3rem;'>Sentiment Intensity</div>"
            f"<div style='font-size:0.82rem;font-weight:600;color:{icolor};'>{review['intensity']} / 5</div>"
            "</div>"
            "<div style='flex:1;min-width:200px;'>"
            "<div style='font-size:0.65rem;font-family:monospace;color:#9ca3af;"
            "text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.3rem;'>Claude Summary (English)</div>"
            f"<div style='font-size:0.82rem;color:#4b5563;'>{review['summary']}</div>"
            "</div>"
            "</div>"
        )
        st.markdown(
            "<div style='border:1px solid #e5e7eb;border-radius:4px;"
            f"overflow:hidden;margin-bottom:0.8rem;'>{top}{bottom}</div>",
            unsafe_allow_html=True,
        )

    with st.expander("View prompt sent to Claude API"):
        st.markdown(
            "<div style='font-size:0.78rem;color:#6b7280;margin-bottom:0.8rem;'>"
            "Negative reviews (1-star) were classified via Claude API. "
            "Positive examples are shown for contrast."
            "</div>",
            unsafe_allow_html=True,
        )
        st.code('''{
  "model": "claude-haiku-4-5",
  "max_tokens": 200,
  "messages": [{
    "role": "user",
    "content": "Analyze this Portuguese e-commerce review and return JSON only:\\n\\n<review_text>\\n\\nReturn:\\n{\\n  \\"complaint_category\\": string,\\n  \\"sentiment_intensity\\": 1-5,\\n  \\"key_issue_english\\": string,\\n  \\"is_seller_fault\\": boolean\\n}"
  }]
}''', language="json")