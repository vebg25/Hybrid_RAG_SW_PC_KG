**Multi-Retriever RAG Pipeline with LlamaIndex**  

A modular Retrieval-Augmented Generation (RAG) system combining parent-child, sentence window, and knowledge graph retrievers with LlamaIndex, HuggingFace embeddings, and Groq LLMs.

---

## ✨ Features

- ⚙️ **Modular Design**: Clean architecture with reusable components.
- 🤖 **Multi-Retriever Fusion**:
  - Parent-child retrieval
  - Sentence-window context retriever
  - Neo4j-based knowledge graph retriever
- 📚 **RAG Capabilities**: Combines multiple retrievers using `QueryFusionRetriever`.
- 🔌 **LLM Integration**: Uses Groq's blazing-fast LLaMA-4 Scout model.
- 🧠 **Embeddings**: Integrates HuggingFace's `dunzhang/stella_en_1.5B_v5` model.
- 📊 **Long Context Handling**: Applies `LongContextReorder` for improved response relevance.
- 📂 **Paul Graham Essays**: Uses LlamaIndex’s curated essay dataset for demos.

---
### Clone this repository
```git
git clone https://github.com/vebg25/Hybrid_RAG_SW_PC_KG.git
```
### Install requirements.txt
```python
pip install -r requirements.txt
```

### Set your API keys and neo4j config
```python
GROQ_API_KEY = "your-groq-api-key"
HF_TOKEN = "your-huggingface-token"
NEO4J_CONFIG = {
    "username": "neo4j",
    "password": "your-password",
    "url": "bolt+s://your-neo4j-url",
    "database": "neo4j"
}
```

### 
Run main.py

```python
python main.py
```


