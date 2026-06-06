import os
import json
from groq import Groq
from forecasting import generate_forecast
from inventory import calculate_inventory_metrics
from rag_engine import SupplyChainRAG

class SupplyChainAgent:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("❌ Missing GROQ_API_KEY environment variable. Please export or set it.")
        
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile" 
        # Initialize our RAG module
        self.rag_engine = SupplyChainRAG()

    def run_workflow(self, current_stock=250):
        print("🤖 Activating Advanced RAG-Driven Supply Chain Agent...")
        
        # 1. Fetch Structured Data (Forecasts + Calculations)
        forecasts = generate_forecast()
        metrics = calculate_inventory_metrics(current_stock=current_stock)
        
        # 2. Fetch Unstructured Risk Intelligence Data (RAG Layer)
        print("🔍 Querying Vector Database (ChromaDB) for real-world risk updates...")
        v1_risks = self.rag_engine.query_risk_context("Alpha Logistics", max_results=1)
        v2_risks = self.rag_engine.query_risk_context("Beta Prime Corp", max_results=1)
        
        # Compile unstructured intelligence strings
        alpha_news = v1_risks[0] if v1_risks else "No critical anomalies reported."
        beta_news = v2_risks[0] if v2_risks else "No critical anomalies reported."

        # Assemble the global context payload
        context_summary = f"""
        STRUCTURED INVENTORY METRICS:
        - Warehouse Current Stock: {current_stock} units
        - Next 14-Day Predicted Total Demand (Median): {int(forecasts['median'].sum())} units
        - High-Risk Boundary Demand (90th Percentile): {int(forecasts['high'].sum())} units
        
        VENDOR OPTIONS CRITERIA:
        - Vendor VND001 (Alpha Logistics): Lead Time = {metrics['VND001']['lead_time_days']} days, Unit Cost = $12.50, ROP Threshold = {metrics['VND001']['reorder_point']} units
        - Vendor VND002 (Beta Prime Corp): Lead Time = {metrics['VND002']['lead_time_days']} days, Unit Cost = $18.00, ROP Threshold = {metrics['VND002']['reorder_point']} units
        
        UNSTRUCTURED RISK INTELLIGENCE FEEDS (RAG RETRIEVED):
        - News Alert regarding Alpha Logistics (VND001): {alpha_news}
        - News Alert regarding Beta Prime Corp (VND002): {beta_news}
        """

        # 3. Construct System Prompt with explicit reasoning directives
        system_prompt = """
        You are an elite, autonomous AI Supply Chain Orchestrator. Your objective is to minimize holding costs, avoid stockouts, and proactively adapt to real-world infrastructure crises.
        
        CRITICAL REASONING POLICY:
        1. Evaluate numerical optimization states against the Unstructured Risk Intelligence feeds.
        2. Even if a vendor is mathematically optimal (e.g., faster lead times), if your RAG intelligence flags that their transit routes are actively paralyzed by strikes, weather, or black swan bottlenecks, you must dynamically reroute to the alternative vendor.
        3. Recalculate your order volume requirements if a chosen vendor faces temporary operational friction or slower transit buffers.
        
        OUTPUT FORMAT REQUIREMENTS:
        Your response must be a single, valid, raw JSON object. Do not wrap it in markdown block styling. Use exactly this JSON model layout:
        {{
          "analysis": "Provide a comprehensive executive synthesis explaining why you either followed the baseline mathematical recommendations or explicitly overruled them based on retrieved RAG risk bulletins.",
          "selected_vendor_id": "VND001 or VND002",
          "recommended_order_quantity": 1200,
          "procurement_email_draft": "Formal corporate logistics communication addressed to the chosen entity stating specific volume requirements and inquiring explicitly about transit mitigations regarding any active regional bulletins."
        }}
        """

        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Analyze the operational ecosystem state variables and select optimized tracking paths:\n{context_summary}"}
                ],
                model=self.model,
                temperature=0.15,
                response_format={"type": "json_object"}
            )
            
            agent_decision = json.loads(chat_completion.choices[0].message.content)
            return agent_decision

        except Exception as e:
            print(f"❌ Core processing architecture failure: {str(e)}")
            return None

if __name__ == "__main__":
    os.environ["GROQ_API_KEY"] = ""

    agent = SupplyChainAgent()
    decision = agent.run_workflow(current_stock=250)
    
    if decision:
        print("\n🎯 --- ADVANCED RAG DECISION MATRIX MATRIX --- 🎯")
        print(json.dumps(decision, indent=2))