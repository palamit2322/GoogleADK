from investmentAI.rag.ingestion import IngestionPipeline

pipeline = IngestionPipeline(
    data_path="data/",
    persist_directory="./chroma_db"
)

pipeline.ingest()