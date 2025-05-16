from neo4j import GraphDatabase
from llama_index.graph_stores.neo4j import Neo4jGraphStore
from llama_index.core import StorageContext
from llama_index.core.retrievers import KnowledgeGraphRAGRetriever
from config import NEO4J_USERNAME, NEO4J_PASSWORD, NEO4J_URL, NEO4J_DATABASE

def get_graph_retriever():

    # Run for creating knowledge graph 
    # index = KnowledgeGraphIndex.from_documents(
    #     documents,
    #     storage_context=storage_context_graph,
    #     max_triplets_per_chunk=2,
    #     embed_model=embed_model,
    #     llm=llm,
    #     include_embeddings=True,
    # )

    driver = GraphDatabase.driver(NEO4J_URL, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
    driver.verify_connectivity()

    graph_store = Neo4jGraphStore(
        username=NEO4J_USERNAME,
        password=NEO4J_PASSWORD,
        url=NEO4J_URL,
        database=NEO4J_DATABASE,
    )
    storage_context = StorageContext.from_defaults(graph_store=graph_store)

    return KnowledgeGraphRAGRetriever(storage_context=storage_context, verbose=True)
