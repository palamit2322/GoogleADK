
from investmentAI.rag.ingestion import retriever
def retrieve_documents(query: str) -> str:
    docs = retriever.invoke(query)

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )

