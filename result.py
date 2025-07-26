import chromadb
from text_preprocessing import segmentation

# Initialize ChromaDB client
client = chromadb.Client()

# Ensure fresh collection creation
try:
    collection = client.create_collection("pdf")
except:
    client.delete_collection("pdf")
    collection = client.create_collection("pdf")


def load_pdf(pdf1, pdf2):
    data = {}
    data[0] = segmentation(pdf1)
    data[1] = segmentation(pdf2)

    for i in range(2):
        chunks = data[i]

        if not chunks:
            print(f"⚠️ Warning: No content found in PDF {i+1}, skipping.")
            continue

        print(f"✅ Adding PDF {i+1} to collection — {len(chunks)} segments")

        collection.add(
            ids=[f"pdf{i}_{j}" for j in range(len(chunks))],
            documents=chunks,
            metadatas=[{"pdf": i} for _ in range(len(chunks))],
        )


def query(query: str, n_results=10):
    results = collection.query(query_texts=[query], n_results=n_results)

    output = []
    for i in range(len(results['documents'][0])):  # safer than assuming n_results always exists
        pdf_num = results['metadatas'][0][i].get('pdf', -1) + 1
        doc_text = results['documents'][0][i]
        output.append(f"from PDF {pdf_num} : {doc_text}")

    return output
