import os
import chromadb
from chromadb.config import Settings
from text_preprocessing import segmentation

# Ensure persistence directory exists
os.makedirs("./chroma", exist_ok=True)

# Initialize ChromaDB client with duckdb backend
client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma"
))

# Create or reset collection
collection_name = "pdf"
try:
    collection = client.create_collection(collection_name)
except:
    client.delete_collection(collection_name)
    collection = client.create_collection(collection_name)

def load_pdf(pdf1, pdf2):
    data = {
        0: segmentation(pdf1),
        1: segmentation(pdf2)
    }

    for i in range(2):
        chunks = data[i]
        if not chunks:
            print(f"⚠️ Warning: No content found in PDF {i+1}, skipping.")
            continue

        print(f"✅ Adding PDF {i+1} to collection — {len(chunks)} segments")

        collection.add(
            ids=[f"pdf{i}_{j}" for j in range(len(chunks))],
            documents=chunks,
            metadatas=[{"pdf": i} for _ in range(len(chunks))]
        )

def query(query: str, n_results=10):
    results = collection.query(query_texts=[query], n_results=n_results)

    output = []
    for i in range(len(results['documents'][0])):
        pdf_num = results['metadatas'][0][i].get('pdf', -1) + 1
        doc_text = results['documents'][0][i]
        output.append(f"from PDF {pdf_num} : {doc_text}")

    return output
