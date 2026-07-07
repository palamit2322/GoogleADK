from investmentAI.rag.ingestion import IngestionPipeline

pipeline = IngestionPipeline(
    data_path="investmentAI/data",
    persist_directory="investmentAI/chroma_db"
)
pipeline.ingest()