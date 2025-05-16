from llama_index.core.node_parser import HierarchicalNodeParser, get_leaf_nodes
from llama_index.core import SimpleDocumentStore, StorageContext, VectorStoreIndex
from llama_index.core.retrievers import AutoMergingRetriever

def get_vector_retriever(documents, embed_model, llm):
    nodes = HierarchicalNodeParser.from_defaults().get_nodes_from_documents(documents)
    docstore = SimpleDocumentStore()
    docstore.add_documents(nodes)
    leaf_nodes = get_leaf_nodes(nodes)

    storage_context = StorageContext.from_defaults(docstore=docstore)
    index = VectorStoreIndex(leaf_nodes, storage_context=storage_context, embed_model=embed_model, llm=llm)
    base_retriever = index.as_retriever(similarity_top_k=3)

    return AutoMergingRetriever(base_retriever, storage_context, verbose=True)
