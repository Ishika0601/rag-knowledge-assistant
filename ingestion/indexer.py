from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from app.config import VECTOR_DB_PATH

def build_index(chunks):
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_texts(chunks, embeddings)
    db.save_local(VECTOR_DB_PATH)
