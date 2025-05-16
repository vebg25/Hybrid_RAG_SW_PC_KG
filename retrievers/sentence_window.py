from llama_index.core.node_parser import SentenceWindowNodeParser, SentenceSplitter
from llama_index.core import VectorStoreIndex, Settings

def get_sentence_retriever(documents, embed_model, llm):
    parser = SentenceWindowNodeParser.from_defaults(window_size=3)
    Settings.text_splitter = SentenceSplitter()

    nodes = parser.get_nodes_from_documents(documents)
    index = VectorStoreIndex(nodes, embed_model=embed_model, llm=llm)
    return index.as_retriever(similarity_top_k=3)
