from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import LongContextReorder

def build_query_engine(combined_retriever):
    return RetrieverQueryEngine.from_args(
        retriever=combined_retriever,
        response_mode="tree_summarize",
        node_postprocessors=[LongContextReorder()],
    )
