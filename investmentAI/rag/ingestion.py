from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

def file_loader(path):
    loader=DirectoryLoader(
        path,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )    
    documents=loader.load()
    return documents

extracted_docs=file_loader("data/")


def chunking_data(split_documents):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunk_data=text_splitter.split_documents(split_documents)
    return chunk_data
chunk_data=chunking_data(extracted_docs)


embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

vector_store=Chroma.from_documents(documents=chunk_data,embedding=embeddings,persist_directory="./chroma_db")

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)
    
