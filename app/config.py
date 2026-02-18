import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
VECTOR_DB_PATH = "vector_store"
TOP_K = 5
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
