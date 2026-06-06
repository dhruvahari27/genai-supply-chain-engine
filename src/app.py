import os
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from forecasting import generate_forecast
from inventory import calculate_inventory_metrics
from agent import SupplyChainAgent
from rag_engine import SupplyChainRAG

# 1. Page Configuration
st.set_page_config(
    page_title="Enterprise AI Supply Chain", 
    layout="wide", 
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS Injection for Enterprise UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .custom-header {
        text-align: center;
        font-weight: 800;
        font-size: 2.5rem;
        background: -webkit-linear-gradient(#4CAF50, #2E7D32);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding-bottom: 10px;
        border-bottom: 1px solid #333;
        margin-bottom: 25px;
    }
    
    div[data-testid="metric-container"] {
        background-color: #111418;
        border: 1px solid #2d3139;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
        transition: transform 0.2s ease-in-out, border-color 0.2s;
    }
    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        border-color: #4CAF50;
    }
    
    .stButton>button {
        background: linear-gradient(90deg, #10b981 0%, #059669 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        font-size: 1.1rem;
        font-weight: bold;
        transition: all 0.3s ease;
        width: 100%;
        box-shadow: 0 4px 6px rgba(16, 185, 129, 0.3);
    }
    .stButton>button:hover {
        transform: scale(1.01);
        box-shadow: 0 6px 15px rgba(16, 185, 129, 0.5);
    }
    
    .stTextArea textarea {
        background-color: #111418 !important;
        border: 1px solid #2d3139 !important;
        color: #e2e8f0 !important;
        border-radius: 8px;
    }
    
    .section-box {
        background-color: #111418;
        border: 1px solid #2d3139;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='custom-header'>⚡ Autonomous AI Supply Chain Engine</h1>", unsafe_allow_html=True)

# 3. Sidebar Control Panel
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2830/2830305.png", width=60)
st.sidebar.markdown("### 🏭 Warehouse Control")
current_stock = st.sidebar.slider(
    "Current Inventory Level", 
    min_value=50, max_value=2000, value=250, step=50
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🗺️ System Blueprint")
st.sidebar.caption("1. **Time Series Core:** Amazon Chronos Foundation Model runs predictive math.")
st.sidebar.caption("2. **Context Layer:** ChromaDB acts as our semantic risk advisor.")
st.sidebar.caption("3. **Brain:** Llama 3.3 orchestrates optimal financial & risk balancing actions.")

# Set API Key securely
os.environ["GROQ_API_KEY"] = ""

# 4. KPI Metric Cards
metrics = calculate_inventory_metrics(current_stock=current_stock)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="📦 Current Warehouse Stock", value=f"{current_stock} Units")
with col2:
    st.metric(
        label="🚛 Standard ROP (VND001)", 
        value=f"{metrics['VND001']['reorder_point']} Units",
        delta="- Order Triggered" if current_stock <= metrics['VND001']['reorder_point'] else "Safe Zone",
        delta_color="inverse"
    )
with col3:
    st.metric(
        label="🚀 Express ROP (VND002)", 
        value=f"{metrics['VND002']['reorder_point']} Units",
        delta="- Order Triggered" if current_stock <= metrics['VND002']['reorder_point'] else "Safe Zone",
        delta_color="inverse"
    )

st.markdown("<br>", unsafe_allow_html=True)

# 5. NEW SECTION: Broader Executive Overview Tab Layer
st.markdown("## 📈 Strategic Control & Executive Insights")
tabs = st.tabs(["📊 Live Forecasting & Risk Data", "🧠 Executive Financial Matrix", "🚨 Historical Anomaly Log"])

with tabs[0]:
    # Dual Dashboard: RAG Intel vs Math Forecast
    col_chart, col_rag = st.columns([2, 1.2])

    with col_chart:
        st.markdown("### 🔮 Chronos Zero-Shot Forecast")
        with st.spinner("Generating foundation model predictions..."):
            forecasts = generate_forecast()
        
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(10, 4.5))
        fig.patch.set_facecolor('#0E1117')
        ax.set_facecolor('#0E1117')
        
        horizon_days = np.arange(1, 15)
        ax.plot(horizon_days, forecasts['median'], label='Median Demand', color='#10b981', linewidth=2.5, marker='o')
        ax.fill_between(horizon_days, forecasts['low'], forecasts['high'], color='#10b981', alpha=0.2, label='90% Risk Margin')
        ax.set_xlabel('Horizon (Days)', color='#a0aec0')
        ax.set_ylabel('Projected Units', color='#a0aec0')
        ax.grid(True, linestyle='--', alpha=0.2)
        ax.tick_params(colors='#a0aec0')
        ax.legend(loc='upper left', facecolor='#111418', edgecolor='#2d3139', labelcolor='white')
        st.pyplot(fig)

    with col_rag:
        st.markdown("### 📰 Live Vector Intel (RAG)")
        rag = SupplyChainRAG()
        v1_alerts = rag.query_risk_context("Alpha Logistics", max_results=1)
        v2_alerts = rag.query_risk_context("Beta Prime Corp", max_results=1)
        
        with st.container(border=True):
            st.markdown("**VND001 (Standard) Intel:**")
            st.caption(f"_{v1_alerts[0] if v1_alerts else 'Clear skies.'}_")
        with st.container(border=True):
            st.markdown("**VND002 (Express) Intel:**")
            st.caption(f"_{v2_alerts[0] if v2_alerts else 'Clear skies.'}_")

with tabs[1]:
    st.markdown("### 💵 Operational & Procurement Cost Matrix")
    st.markdown("""
    This panel outlines the underlying cost metrics and delivery mechanics that the AI Agent balances. 
    When risk is low, the Agent defaults to optimizing **Capital Expenditure (CapEx)**. When risk spikes, it shifts to optimizing **Service Level Agreements (SLAs)**.
    """)
    
    # Financial analysis dataframe display
    cost_data = {
        "Vendor Profile": ["Alpha Logistics (VND001)", "Beta Prime Corp (VND002)"],
        "Delivery Type": ["Standard Rail / Ground", "Express Expedited Air"],
        "Base Unit Cost": ["$12.50", "$18.00"],
        "Lead Time Window": ["5 Days", "2 Days"],
        "Calculated Safety Stock Cushion": [f"{metrics['VND001']['safety_stock']} units", f"{metrics['VND002']['safety_stock']} units"],
        "Financial Strategic Role": ["Primary Cost Saver", "Emergency Safety Valve"]
    }
    st.table(pd.DataFrame(cost_data))

with tabs[2]:
    st.markdown("### 🚨 System Auditing: Root-Cause Anomaly Detection")
    st.info("📊 **Audit Event Log:** A severe 15-day out-of-bounds demand drift spike was historically tracked and analyzed during Year 3 (Days 950-965).")
    st.markdown("""
    * **Root Cause Discovered via Context:** Regional historical reports linked this massive spike to a historic severe Q3 heatwave that broke consumer patterns.
    * **Engine Adaptive Behavior:** The system noted this spike as an *external anomaly* rather than natural baseline growth. This allows the Amazon Chronos model to generate smooth, accurate next-14-day estimates without being warped or ruined by historical noise.
    """)

st.markdown("---")

# 7. Autonomous Execution Section
st.subheader("🤖 GenAI Supply Chain Agent Decision Center")

if st.button("🚀 Execute Autonomous Neural Orchestration"):
    with st.spinner("Agent evaluating unstructured intel against math thresholds..."):
        try:
            agent = SupplyChainAgent()
            decision = agent.run_workflow(current_stock=current_stock)
            
            if decision:
                st.success("✅ Multi-Modal Strategy Profile Fully Compiled!")
                
                res_col1, res_col2 = st.columns([1, 1.5])
                with res_col1:
                    st.markdown("### 🎯 Executive Decision")
                    vendor_color = "#10b981" if decision.get('selected_vendor_id') == "VND001" else "#f59e0b"
                    st.markdown(f"**Target Vendor:** <span style='color:{vendor_color}; font-size:1.2rem; font-weight:bold;'>{decision.get('selected_vendor_id')}</span>", unsafe_allow_html=True)
                    st.markdown(f"**Order Volume:** {decision.get('recommended_order_quantity')} Units")
                    st.markdown("**Reasoning Engine:**")
                    st.info(decision.get('analysis'))
                    
                with res_col2:
                    st.markdown("### ✉️ Automated Dispatch Draft")
                    st.text_area(label="Procurement API Payload", value=decision.get('procurement_email_draft'), height=220, label_visibility="collapsed")
            else:
                st.error("Agent failed to structure valid JSON matrix.")
        except Exception as e:
            st.error(f"Execution pipeline roadblock: {str(e)}")