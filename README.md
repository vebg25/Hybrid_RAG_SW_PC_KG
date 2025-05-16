**Multi-Retriever RAG Pipeline with LlamaIndex**  
A modular Retrieval-Augmented Generation (RAG) system combining vector, sentence window, and knowledge graph retrievers with LlamaIndex, HuggingFace embeddings, and Groq LLMs.

---

## ✨ Features

- ⚙️ **Modular Design**: Clean architecture with reusable components.
- 🤖 **Multi-Retriever Fusion**:
  - Vector-based retrieval
  - Sentence-window context retriever
  - Neo4j-based knowledge graph retriever
- 📚 **RAG Capabilities**: Combines multiple retrievers using `QueryFusionRetriever`.
- 🔌 **LLM Integration**: Uses Groq's blazing-fast LLaMA-4 Scout model.
- 🧠 **Embeddings**: Integrates HuggingFace's `dunzhang/stella_en_1.5B_v5` model.
- 📊 **Long Context Handling**: Applies `LongContextReorder` for improved response relevance.
- 📂 **Paul Graham Essays**: Uses LlamaIndex’s curated essay dataset for demos.

---
