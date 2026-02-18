from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from app.config import VECTOR_DB_PATH, TOP_K

def load_retriever():
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local(VECTOR_DB_PATH, embeddings)
    return db.as_retriever(search_kwargs={"k": TOP_K})
