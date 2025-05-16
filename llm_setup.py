from llama_index.llms.groq import Groq
from config import GROQ_API_KEY

def init_llm():
    return Groq(model="meta-llama/llama-4-scout-17b-16e-instruct", api_key=GROQ_API_KEY)