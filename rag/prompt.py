from langchain.prompts import PromptTemplate

RAG_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a domain assistant.

Answer ONLY using the provided context.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""
)
