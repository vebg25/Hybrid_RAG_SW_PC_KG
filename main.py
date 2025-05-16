import nest_asyncio
nest_asyncio.apply()

from llm_setup import init_llm
from embeddings import init_embed_model
from data_loader import load_documents
from query_engine import build_query_engine

from retrievers.auto_merger import get_vector_retriever
from retrievers.sentence_window import get_sentence_retriever
from retrievers.knowledge_graph import get_graph_retriever
from retrievers.combined_retriever import get_combined_retriever
from llama_index.core.response.notebook_utils import display_response
from llama_index.core import Settings

def main():
    llm = init_llm()
    embed_model = init_embed_model()
    Settings.llm = llm
    Settings.embed_model = embed_model
    Settings.chunk_size = 512

    documents = load_documents()

    retriever_auto = get_vector_retriever(documents, embed_model, llm)
    retriever_sentence = get_sentence_retriever(documents, embed_model, llm)
    retriever_graph = get_graph_retriever()

    combined_retriever = get_combined_retriever(
        [retriever_sentence, retriever_graph, retriever_auto]
    )

    engine = build_query_engine(combined_retriever)
    response = engine.query("Explain automation and AI")
    display_response(response)

if __name__ == "__main__":
    main()
