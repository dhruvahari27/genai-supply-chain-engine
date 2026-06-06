import os
import chromadb
from chromadb.utils import embedding_functions

class SupplyChainRAG:
    def __init__(self, db_path="data/chroma_db"):
        self.db_path = db_path
        # Initialize a persistent local Chroma storage client
        self.client = chromadb.PersistentClient(path=self.db_path)
        
        # Use an industry-standard open-source sentence transformer model for local embeddings
        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        
        # Get or create our unique supply chain risk intelligence vector collection
        self.collection = self.client.get_or_create_collection(
            name="supply_chain_risks",
            embedding_function=self.embedding_function
        )

    def ingest_news_alerts(self, alerts_dir="data/news_alerts"):
        print("📥 Initializing Ingestion Engine for Unstructured Risk Intelligence...")
        
        if not os.path.exists(alerts_dir):
            print(f"⚠️ Directory '{alerts_dir}' not found. Please verify paths.")
            return

        documents = []
        metadatas = []
        ids = []

        # Read all text briefs from our mock geopolitical and weather incident files
        for filename in os.listdir(alerts_dir):
            if filename.endswith(".txt"):
                file_path = os.path.join(alerts_dir, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                documents.append(content)
                metadatas.append({"source_file": filename})
                ids.append(filename.split(".")[0])

        if documents:
            # Upsert operations ensure documents update automatically if values switch
            self.collection.upsert(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )
            print(f"✅ Successfully vectorized and stored {len(documents)} incident profiles in local ChromaDB!")
        else:
            print("⚠️ No valid .txt intelligence feeds discovered in the targeted folder.")

    def query_risk_context(self, search_query, max_results=1):
        """Query the vector database for operational context matched to target keywords."""
        results = self.collection.query(
            query_texts=[search_query],
            n_results=max_results
        )
        # Extract and return the plain text documents matched
        if results and 'documents' in results and results['documents']:
            return results['documents'][0]
        return []

if __name__ == "__main__":
    # Create testing execution environment variables
    os.makedirs("data/news_alerts", exist_ok=True)
    
    rag = SupplyChainRAG()
    rag.ingest_news_alerts()
    
    # Run a quick semantic query verification check
    print("\n🔍 Executing Semantic Search Test for 'Beta Prime Corp' risks:")
    matched_docs = rag.query_risk_context("Beta Prime Corp", max_results=1)
    if matched_docs:
        print(f"📄 Found Match:\n{matched_docs[0]}")
    else:
        print("❌ Semantic lookup yielded no records.")