from llama_index.core.retrievers import QueryFusionRetriever

def get_combined_retriever(retrievers):
    return QueryFusionRetriever(
        retrievers=retrievers,
        similarity_top_k=3,
        num_queries=4,
        mode="reciprocal_rerank",
        use_async=True,
        verbose=True,
    )
