from fastapi import FastAPI
from app.ingestion.loader import load_documents
from app.ingestion.splitter import split_text
from app.ingestion.indexer import build_index
from app.rag.retriever import load_retriever
from app.rag.chain import build_chain
from app.evaluation.retrieval_eval import hit_at_k
from app.evaluation.answer_eval import is_faithful
from app.evaluation.system_metrics import measure_latency

app = FastAPI()
retriever = None
chain = None

@app.on_event("startup")
def startup():
    text = load_documents("data/sample_docs.txt")
    chunks = split_text(text)
    build_index(chunks)

    global retriever, chain
    retriever = load_retriever()
    chain = build_chain()

@measure_latency
def answer_question(question: str):
    docs = retriever.get_relevant_documents(question)
    context = "\n".join(d.page_content for d in docs)
    answer = chain.run({"context": context, "question": question})

    retrieval_score = hit_at_k(docs, expected_terms=question.split())
    faithful = is_faithful(answer, context)

    return {
        "answer": answer,
        "retrieval_hit_at_k": retrieval_score,
        "faithful": faithful
    }

@app.get("/ask")
def ask(question: str):
    response, latency = answer_question(question)
    response["latency_seconds"] = round(latency, 3)
    return response
