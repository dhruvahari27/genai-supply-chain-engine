# ⚡ GenAI-Powered Autonomous Supply Chain Engine 

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-FF4B4B?style=for-the-badge&logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker)
![AI](https://img.shields.io/badge/AI-Agentic_Architecture-10b981?style=for-the-badge)

## 📖 Executive Summary
The **GenAI Supply Chain Engine** is an advanced, production-grade AI solution built to fix a fatal flaw in traditional enterprise resource planning (ERP) software: **standard tools only look at math, but real-world operations are constantly disrupted by real-world events.**

Normally, a standard automated supply chain system will buy products from whichever vendor is mathematically the cheapest or fastest on paper. But if that vendor's home port is currently blocked by a massive labor strike or sudden cross-border tariffs, the math fails, causing massive stockouts, lost sales, and thousands of dollars in emergency fees.

This engine solves this problem by fusing **Numerical Demand Forecasting (Statistical Math)** with **Unstructured Risk Intelligence (Retrieval-Augmented Generation)**. It utilizes an autonomous AI Agent that scans real-time numbers *and* text bulletins simultaneously, allowing it to dynamically overrule standard math when real-world crises threaten transit safety.

---

## 🧠 Deep Dive: Structural System Architecture

The engine runs as a modular, three-tiered workflow designed to mimic the processing steps of an elite corporate logistics director:

```text
  +-----------------------+      +-----------------------+
  |   Structured Data     |      |   Unstructured Data   |
  |  (Historical Sales)   |      |  (News/Disaster Logs) |
  +-----------+-----------+      +-----------+-----------+
              |                              |
              v                              v
  +-----------------------+      +-----------------------+
  |   Forecasting Core    |      |     ChromaDB RAG      |
  | (Amazon Chronos T5)   |      | (Semantic Search)     |
  +-----------+-----------+      +-----------+-----------+
              |                              |
              +--------------+---------------+
                             |
                             v
              +------------------------------+
              |     Autonomous AI Agent      |
              |     (Llama 3.3 Orchestrator) |
              +--------------+---------------+
                             |
                             v
              +------------------------------+
              | Enterprise Dark-UI Control   |
              |    & Dispatch Automation     |
              +------------------------------+
1. The Math Layer (Predictive Analytics)Core Technology: Amazon Chronos T5 (Zero-Shot Time-Series Foundation Model)The Operation: The engine takes input from historical datasets to run forward-looking demand projections across a 14-day horizon. It uses statistical models to calculate the Reorder Point (ROP) and Safety Stock cushions needed to protect warehouse operations against worst-case consumer spikes.2. The Context Layer (Semantic RAG Vector Database)Core Technology: ChromaDB & SentenceTransformers (all-MiniLM-L6-v2)The Operation: This layer parses unformatted text notifications (weather advisories, port labor files, custom border updates) and maps them into a dense vector space. When evaluating vendor vulnerability, the system fires semantic similarity searches against the persistent local DB to spot critical operational anomalies.3. The Brain (Autonomous Agent Orchestrator)Core Technology: Llama 3.3 70B (via Groq API Engine)The Operation: The agent takes structured metrics (Lead times, costs, ROP) and maps them against unstructured RAG risk profiles inside an advanced system prompt. If an optimal vendor is compromised by real-world anomalies, the agent actively overrules the statistical system, reroutes procurement to the alternative vendor, recalculates safe safety stock buffers, and exports a raw JSON payload with automated dispatch emails.🛠️ Complete Technology StackArchitecture PieceTool / Library UsedStrategic PurposeFrontend UI ViewStreamlit (Custom HTML/CSS)High-fidelity dark-themed operational control tower.Orchestration BrainGroq Client (Llama 3.3 70B)High-speed, highly deterministic structured JSON reasoning.Vector DB RegistryChromaDB (Local Persistent)Low-latency storage and retrieval of unstructured textual risks.Embedding EngineSentenceTransformersTranslates plain text bulletins into numerical semantic vectors.Forecasting FrameworkAmazon Chronos T5Zero-shot deep learning framework for demand optimization.ContainerizationDocker EnginePackages dependencies for deterministic cross-cloud deployment.MLOps PipelineGitHub Actions WorkflowAutomated CI/CD verification of building code assets.📂 Project Directory StructurePlaintextgenai-supply-chain-engine/
├── .github/
│   └── workflows/
│       └── ci-cd-pipeline.yml # Automated CI/CD build check pipeline
├── data/
│   ├── chroma_db/             # Persistent binary database files
│   ├── news_alerts/           # Simulated text file operational crisis logs
│   ├── historical_demand.csv  # Historical inventory sales records
│   └── vendor_catalog.csv     # Vendor capabilities, costs, and SLA baselines
├── src/
│   ├── __init__.py
│   ├── agent.py               # Main LLM Agent execution and prompt blueprint
│   ├── app.py                 # Streamlit front-end dashboard with injected CSS
│   ├── data_simulator.py      # Script to mock and seed database requirements
│   ├── forecasting.py         # Chronos engine mathematical forecast implementation
│   ├── inventory.py           # Core algorithmic safety stock & ROP computations
│   └── rag_engine.py          # ChromaDB collection build, insert, and query modules
├── config.yaml
├── Dockerfile                 # Multi-layered Linux container deployment recipe
├── README.md
└── requirements.txt           # Explicitly pinned version tracking file

🚀 Installation & Local Execution
Option 1: Direct Python Runtime Installation
1. Clone the Code Repository:

Bash
git clone [https://github.com/dhruvahari27/genai-supply-chain-engine.git](https://github.com/dhruvahari27/genai-supply-chain-engine.git)
cd genai-supply-chain-engine
2. Setup System Package Dependencies:

Bash
pip install -r requirements.txt
3. Configure Runtime Security Variables:
Generate an API Key via the Groq Console. Export the key securely into your active terminal space (do not code this inside python files):

Windows PowerShell: $env:GROQ_API_KEY="your_api_key_here"

Mac / Linux Terminal: export GROQ_API_KEY="your_api_key_here"

4. Compile the Text Vector Database Engine:
Run the ingestion script to process the text reports and seed your local vector store:

Bash
python src/rag_engine.py
5. Spin Up the Visual Control Dashboard:

Bash
streamlit run src/app.py
Option 2: Isolated Container Deployment (Production Method)
To check portabilities without installing Python modules directly to your home OS, run this using Docker:

1. Build the Blueprint Image:

Bash
docker build -t genai-supply-chain .
2. Mount and Start the Container:
Pass your API Key variables into the system environment wrapper upon launch:

Bash
docker run -p 8501:8501 -e GROQ_API_KEY="your_api_key_here" genai-supply-chain
Open up your web browser and view the live deployment environment at http://localhost:8501.

💡 Live Demo Walkthrough Instructions
When showing off this application to engineering teams or recruiters, use this execution walkthrough to prove the value of its architecture:

Review Statistical baselines: Look at the Chronos Zero-Shot Forecast graph and tabulate the base demand limits.

Review Context Feeds: Check out the right column of the workspace. Observe how the system pulls live unstructured text data out of ChromaDB showing that Beta Prime Corp is locked in a massive logistics bottleneck due to an ongoing labor strike.

Simulate an Operational Shortage: Lower the "Current Inventory Level" slider on the left sidebar down to a critical level (e.g., 200 units). This forces an immediate reorder threshold trigger.

Fire the Orchestrator: Click the green Execute Autonomous Neural Orchestration button.

Verify the Intelligent Decision Matrix: Notice how the Agent completely avoids the fast-delivery vendor (Beta Prime Corp) because 
it integrated the text alerts. It systematically selects Alpha Logistics, logs the operational reason why in the analysis dashboard,
and creates an automated dispatch email detailing custom mitigation inquiries.
