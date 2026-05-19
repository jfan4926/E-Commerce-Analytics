import streamlit as st
import time

# Pre-canned demo responses for each example question
DEMOS = {
    "Which product categories have the highest average review score?": {
        "sql": """SELECT
    p.product_category_name_english AS category,
    ROUND(AVG(o.review_score), 2)   AS avg_review_score,
    COUNT(*)                         AS order_count
FROM fact_orders o
JOIN dim_products p ON o.product_id = p.product_id
WHERE o.review_score IS NOT NULL
GROUP BY p.product_category_name_english
HAVING COUNT(*) > 100
ORDER BY avg_review_score DESC;""",
        "table": {
            "Category":         ["books_imported", "fashion_sport", "flowers", "arts_crafts", "audio"],
            "Avg Review Score": [4.51, 4.43, 4.41, 4.38, 4.35],
            "Order Count":      [312, 874, 213, 567, 189],
        },
        "insight": "📖 Books and fashion categories consistently outperform others, averaging above 4.4 stars. These categories likely benefit from lower complexity fulfillment and accurate product descriptions.",
"chart": {
            "type": "bar",
            "data": {
                "Category": ["books_imported", "fashion_sport", "flowers", "arts_crafts", "audio"],
                "Avg Review Score": [4.51, 4.43, 4.41, 4.38, 4.35]
            },
            "x": "Category",
            "y": "Avg Review Score",
        },
    },
    "What's the average delivery delay by Brazilian state?": {
        "sql": """SELECT
    c.customer_state,
    ROUND(AVG(DATEDIFF(day,
        o.order_estimated_delivery_date,
        o.order_delivered_customer_date)), 1) AS avg_delay_days,
    COUNT(*) AS order_count
FROM fact_orders o
JOIN dim_customers c ON o.customer_id = c.customer_id
WHERE o.order_status = 'delivered'
  AND o.order_delivered_customer_date > o.order_estimated_delivery_date
GROUP BY c.customer_state
ORDER BY avg_delay_days DESC;""",
        "table": {
            "State":          ["RR", "AP", "AM", "PA", "AL"],
            "Avg Delay Days": [12.4, 10.1, 8.7, 7.2, 6.9],
            "Order Count":    [187, 243, 891, 1204, 673],
        },
        "insight": "🗺️ Northern states (RR, AP, AM) experience the worst delays — up to 12 days past estimated delivery. This matches the geospatial view in the Dashboard tab and points to last-mile logistics gaps in remote regions.",
        "chart": {
            "type": "bar",
            "data": {"State": ["RR", "AP", "AM", "PA", "AL"], "Avg Delay Days": [12.4, 10.1, 8.7, 7.2, 6.9]},
            "x": "State", "y": "Avg Delay Days",
        },
    },
    "How do 1-star reviews correlate with delivery time?": {
        "sql": """SELECT
    CASE
        WHEN DATEDIFF(day, o.order_purchase_timestamp,
                          o.order_delivered_customer_date) <= 7  THEN '0-7 days'
        WHEN DATEDIFF(day, o.order_purchase_timestamp,
                          o.order_delivered_customer_date) <= 14 THEN '8-14 days'
        WHEN DATEDIFF(day, o.order_purchase_timestamp,
                          o.order_delivered_customer_date) <= 21 THEN '15-21 days'
        ELSE '21+ days'
    END AS delivery_bucket,
    ROUND(AVG(CASE WHEN o.review_score = 1 THEN 1.0 ELSE 0.0 END) * 100, 1)
        AS pct_one_star
FROM fact_orders o
WHERE o.order_status = 'delivered'
  AND o.review_score IS NOT NULL
GROUP BY
    CASE
        WHEN DATEDIFF(day, o.order_purchase_timestamp,
                          o.order_delivered_customer_date) <= 7  THEN '0-7 days'
        WHEN DATEDIFF(day, o.order_purchase_timestamp,
                          o.order_delivered_customer_date) <= 14 THEN '8-14 days'
        WHEN DATEDIFF(day, o.order_purchase_timestamp,
                          o.order_delivered_customer_date) <= 21 THEN '15-21 days'
        ELSE '21+ days'
    END
ORDER BY pct_one_star;""",
        "table": {
            "Delivery Bucket":  ["0-7 days", "8-14 days", "15-21 days", "21+ days"],
            "% 1-Star Reviews": [8.2, 15.7, 31.4, 54.1],
        },
        "insight": "⚠️ Clear threshold at 15+ days — 1-star rates jump from 15% to 31% and continue climbing. Orders taking over 21 days are 6.6× more likely to receive a 1-star review than fast deliveries.",
        "chart": {
            "type": "bar",
            "data": {"Delivery Bucket": ["0-7 days", "8-14 days", "15-21 days", "21+ days"], "% 1-Star Reviews": [8.2, 15.7, 31.4, 54.1]},
            "x": "Delivery Bucket", "y": "% 1-Star Reviews",
        },
    },
    "Which sellers have the most wrong item complaints?": {
        "sql": """SELECT TOP 5
    s.seller_id,
    s.seller_city,
    s.seller_state,
    COUNT(*) AS wrong_item_complaints
FROM fact_orders o
JOIN dim_sellers s ON o.seller_id = s.seller_id
WHERE o.complaint_category = 'wrong_or_missing_item'
GROUP BY s.seller_id, s.seller_city, s.seller_state
ORDER BY wrong_item_complaints DESC;""",
        "table": {
            "Seller ID":  ["4a3ca...", "6e31c...", "1f29a...", "8b72d...", "2c98f..."],
            "City":       ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Salvador"],
            "State":      ["SP", "RJ", "MG", "PR", "BA"],
            "Complaints": [47, 38, 29, 24, 21],
        },
        "insight": "🏪 Top 5 sellers account for 159 wrong-item complaints — a small number of sellers disproportionately drive fulfillment errors. Targeted seller quality intervention could significantly reduce this category.",
        "chart": {
            "type": "bar",
            "data": {"City": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Salvador"], "Complaints": [47, 38, 29, 24, 21]},
            "x": "City", "y": "Complaints",
        },
    },
    "What was the peak sales month in 2017?": {
        "sql": """SELECT
    FORMAT(o.order_purchase_timestamp, 'yyyy-MM') AS month,
    COUNT(*)                                       AS order_count,
    ROUND(SUM(o.payment_value), 0)                 AS total_gmv
FROM fact_orders o
WHERE YEAR(o.order_purchase_timestamp) = 2017
GROUP BY FORMAT(o.order_purchase_timestamp, 'yyyy-MM')
ORDER BY total_gmv DESC;""",
        "table": {
            "Month":   ["2017-11", "2017-10", "2017-12", "2017-09", "2017-08"],
            "Orders":  [7544, 6884, 6545, 6274, 5741],
            "GMV ($)": [1548320, 1401870, 1389440, 1287650, 1198320],
        },
        "insight": "🛍️ November 2017 was the peak month with $1.55M GMV — driven by Black Friday. October and December follow closely, confirming a strong Q4 seasonal pattern consistent with global e-commerce trends.",
        "chart": {
            "type": "line",
            "data": {"Month": ["2017-08", "2017-09", "2017-10", "2017-11", "2017-12"], "GMV ($)": [1198320, 1287650, 1401870, 1548320, 1389440]},
            "x": "Month", "y": "GMV ($)",
        },
    },
}

def render():
    st.markdown("""
    <div style="margin-bottom:1.5rem;">
        <div style="font-size:1.1rem; font-weight:600; margin-bottom:0.3rem;">
            Text-to-SQL AI Agent
        </div>
        <div style="font-size:0.88rem; color:#6b7280; max-width:620px;">
            Ask questions about the data in plain English. Claude generates SQL,
            runs it against the database, and explains the results.
        </div>
    </div>
    """, unsafe_allow_html=True)
# Demo note
    st.markdown("""
    <div style="padding:0.9rem 1.2rem; background:#f9fafb; border-left:3px solid #9ca3af;
                border-radius:0 4px 4px 0; font-size:0.82rem; color:#6b7280; margin-bottom:1.5rem;
                line-height:1.6;">
        <strong style="color:#1a1a1a;">Demo mode</strong> — This interface simulates the full
        Text-to-SQL pipeline. In production, each question is sent to
        <code>claude-sonnet-4-20250514</code> which generates SQL, runs it against Azure SQL
        via SQLAlchemy, and returns a plain-English interpretation. API and database
        credentials are required to enable live queries.
    </div>
    """, unsafe_allow_html=True)
    # Example question buttons
    st.markdown("**Try an example:**")
    col1, col2 = st.columns(2)
    for i, q in enumerate(DEMOS.keys()):
        col = col1 if i % 2 == 0 else col2
        if col.button(q, key=f"ex_{i}", use_container_width=True):
            st.session_state["agent_q"] = q

    st.markdown("<br/>", unsafe_allow_html=True)

    # Free-text input
    question = st.text_input(
        "Your question",
        value=st.session_state.get("agent_q", ""),
        placeholder="e.g. Which state has the worst delivery performance?",
        label_visibility="collapsed",
    )

    if st.button("Ask", type="primary") and question:
        demo = DEMOS.get(question)

        with st.spinner("Generating SQL..."):
            time.sleep(0.8)

        st.markdown("**Generated SQL**")
        sql = demo["sql"] if demo else "-- No demo available for this question\nSELECT 1;"
        st.code(sql, language="sql")

        with st.spinner("Running query..."):
            time.sleep(0.6)

        st.markdown("**Result**")
        if demo:
            import pandas as pd
            df = pd.DataFrame(demo["table"])
            st.dataframe(df, use_container_width=True, hide_index=True)

            # ── Typewriter effect for insight ─────────────────────────────
            insight_box = st.empty()
            full_text   = demo["insight"]
            displayed   = ""
            for char in full_text:
                displayed += char
                insight_box.markdown(
                    f"<div style='margin-top:0.8rem; padding:0.9rem 1.2rem;"
                    f"background:#f0fdf4; border-left:3px solid #16a34a;"
                    f"border-radius:0 4px 4px 0; font-size:0.85rem; color:#166534;"
                    f"line-height:1.6;'>💡 {displayed}▌</div>",
                    unsafe_allow_html=True,
                )
                time.sleep(0.018)
            insight_box.markdown(
                f"<div style='margin-top:0.8rem; padding:0.9rem 1.2rem;"
                f"background:#f0fdf4; border-left:3px solid #16a34a;"
                f"border-radius:0 4px 4px 0; font-size:0.85rem; color:#166534;"
                f"line-height:1.6;'>💡 {full_text}</div>",
                unsafe_allow_html=True,
            )

            # ── Chart ─────────────────────────────────────────────────────
            chart_data = demo.get("chart")
            if chart_data:
                st.markdown("<br/>**Visualisation**", unsafe_allow_html=True)
                chart_df = pd.DataFrame({
                    chart_data["x"]: chart_data["data"][chart_data["x"]],
                    chart_data["y"]: chart_data["data"][chart_data["y"]],
                })
                if chart_data["type"] == "bar":
                    st.bar_chart(
                        chart_df.set_index(chart_data["x"])[chart_data["y"]],
                        color="#2563eb",
                    )
                elif chart_data["type"] == "line":
                    st.line_chart(
                        chart_df.set_index(chart_data["x"])[chart_data["y"]],
                        color="#2563eb",
                    )
        else:
            st.info("Try one of the example questions above to see a full demo.")

    # How it works
    st.markdown("<br/>", unsafe_allow_html=True)
    with st.expander("How it works"):
        st.markdown("""
1. **Schema extraction** — reads table and column names from the database at runtime
2. **Prompt construction** — your question + schema sent to `claude-sonnet-4-20250514`
3. **SQL generation** — Claude returns a query in Azure SQL dialect
4. **Execution** — query runs against Azure SQL via SQLAlchemy
5. **Interpretation** — Claude summarises the result in plain English
        """)

    with st.expander("View prompt sent to Claude API"):
        st.code('''{
  "model": "claude-sonnet-4-20250514",
  "max_tokens": 1000,
  "system": "You are a SQL expert. Given a database schema and a question, return only a valid SQL query with no explanation.",
  "messages": [{
    "role": "user",
    "content": "Schema:\\n\\nfact_orders(order_id, customer_key, product_key, seller_key, price, freight_value, total_payment, payment_type, review_score, delivery_days, estimated_days, delay_days, is_delayed, delay_bucket, purchase_year, purchase_month)\\n\\ndim_customer(customer_key, customer_unique_id, city, state, zip_code)\\n\\ndim_product(product_key, category_english, weight_g)\\n\\ndim_seller(seller_key, city, state, zip_code)\\n\\ndim_date(date_key, full_date, year, quarter, month, month_name)\\n\\nQuestion: What is the average delivery delay by Brazilian state?\\n\\nReturn SQL only."
  }]
}''', language="json")