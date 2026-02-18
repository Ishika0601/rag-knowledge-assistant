from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from app.rag.prompt import RAG_PROMPT

def build_chain():
    llm = ChatOpenAI(temperature=0)
    return LLMChain(llm=llm, prompt=RAG_PROMPT)
