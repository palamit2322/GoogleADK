from google.adk.tools import FunctionTool

from investmentAI.rag.retriever import retriever

def retrieve_documents(query: str) -> str:
    """
    Retrieve relevant investment documents from the Vector Database.
    """

    docs = retriever.invoke(query)

    if not docs:
        return "No relevant documents found."

    context = "\n\n".join(
        [
            f"Document {i+1}:\n{doc.page_content}"
            for i, doc in enumerate(docs)
        ]
    )

    return context


retrieval_tool = FunctionTool(retrieve_documents)