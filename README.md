# Hybrid_RAG_SW_PC_KG

🧠 Multi-Retriever RAG Pipeline with LlamaIndex
A modular Retrieval-Augmented Generation (RAG) system combining vector, sentence window, and knowledge graph retrievers with LlamaIndex, HuggingFace embeddings, and Groq LLMs.



✨ Features
⚙️ Modular Design: Clean architecture with reusable components.

🤖 Multi-Retriever Fusion:

Vector-based retrieval

Sentence-window context retriever

Neo4j-based knowledge graph retriever

📚 RAG Capabilities: Combines multiple retrievers using QueryFusionRetriever.

🔌 LLM Integration: Uses Groq's blazing-fast LLaMA-4 Scout model.

🧠 Embeddings: Integrates HuggingFace's dunzhang/stella_en_1.5B_v5 model.

📊 Long Context Handling: Applies LongContextReorder for improved response relevance.

📂 Paul Graham Essays: Uses LlamaIndex’s curated essay dataset for demos.

🗂️ Project Structure
bash
Copy
Edit
llama_index_rag/
├── app/
│   ├── config.py                      # API keys and model settings
│   ├── llm_setup.py                  # LLM initialization
│   ├── embeddings.py                 # Embedding model setup
│   ├── data_loader.py                # Loads and parses documents
│   ├── query_engine.py               # Builds the final query engine
│   ├── main.py                       # Main orchestration script
│   └── retrievers/
│       ├── __init__.py
│       ├── vector_retriever.py       # Auto-merging vector retriever
│       ├── sentence_window_retriever.py # Sentence window retriever
│       ├── knowledge_graph_retriever.py # Neo4j KG retriever
│       └── combined_retriever.py     # Fusion logic for all retrievers
├── requirements.txt
└── run.sh
🚀 Quickstart
Clone the repo

bash
Copy
Edit
git clone https://github.com/yourusername/llamaindex-rag.git
cd llamaindex-rag
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Download the Paul Graham Dataset

bash
Copy
Edit
llamaindex-cli download-llamadataset PaulGrahamEssayDataset
Set your API keys in app/config.py:

python
Copy
Edit
GROQ_API_KEY = "your-groq-api-key"
HF_TOKEN = "your-huggingface-token"
NEO4J_CONFIG = {
    "username": "neo4j",
    "password": "your-password",
    "url": "bolt+s://your-neo4j-url",
    "database": "neo4j"
}
Run the pipeline

bash
Copy
Edit
bash run.sh
📌 Query Demo
python
Copy
Edit
response = final_query_engine.query("Explain automation and AI")
display_response(response)
✅ Output is a structured, summarized response retrieved and ranked from multiple semantic sources.

📘 Built With
LlamaIndex

HuggingFace Transformers

Groq LLMs

Neo4j Graph DB

Paul Graham Dataset

🧪 Next Steps
Add Streamlit or Gradio interface

Fine-tune sentence/window fusion strategies

Experiment with additional graph schemas in Neo4j

Use OpenWebText or Wikipedia dump for large-scale retrieval

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

📜 License
MIT License

💬 Questions?
Feel free to open an issue or reach out via LinkedIn or Twitter.

