from llama_index.embeddings.huggingface import HuggingFaceEmbedding

def init_embed_model():
    return HuggingFaceEmbedding(model_name="dunzhang/stella_en_1.5B_v5")
