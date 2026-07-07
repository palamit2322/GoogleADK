from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os

load_dotenv()

class IngestionPipeline:

    def __init__(self, data_path: str, persist_directory: str):
        self.data_path = data_path
        self.persist_directory = persist_directory

        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="gemini-embedding-001"
        )

    def load_documents(self):
        loader = DirectoryLoader(
            self.data_path,
            glob="*.pdf",
            loader_cls=PyPDFLoader
        )

        return loader.load()

    def split_documents(self, documents):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        return splitter.split_documents(documents)

    def ingest(self):

        documents = self.load_documents()

        chunks = self.split_documents(documents)

        Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=self.persist_directory
        )

        print("Ingestion completed successfully.")