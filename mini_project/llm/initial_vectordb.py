from langchain_community.vectorstores import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectordb = Chroma(
    embedding_function=model,
    persist_directory="./llm/chroma_db",
    collection_name = "collection_1"
)