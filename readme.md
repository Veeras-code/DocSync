

📘 DocSync — Smart PDF Comparison and Analysis
Project Image <!-- Add an actual image link or placeholder -->
DocSync is a powerful web application for analyzing and comparing PDF documents using AI-based embedding models and cosine similarity scans. It also features a chatbot interface powered by cutting-edge LLMs—LLAMA 3 and Google Gemini—to interact with your documents seamlessly.

🚀 Features
- 🧠 PDF Comparison Modes
- Document-Level Cosine Similarity Scan
- Sentence-Level Cosine Similarity Scan
- Preprocessed Sentence-Level Cosine Similarity Scan
- 🤖 ChatBot Interaction
- Chat with your PDF using custom LLMs
- LLAMA 3 (via OLLAMA) and Google Gemini integrations
- Intelligent query responses from embedded document vectors

🔧 Tech Stack
| Tool | Purpose | 
| Streamlit | UI framework | 
| FastAPI | Backend API | 
| LangChain | LLM orchestration & logic | 
| Chroma DB | Vector database for embeddings | 
| LLMs | LLAMA 3, Google Gemini | 



⚙️ Installation
- Upload PDFs — Select two documents to compare.
- Choose Scan Type — Document-Level, Sentence-Level, or Preprocessed.
- Select Embedding — Count Vectorizer, TF-IDF, or all-MiniLM-L6-v2.
- Run Comparison — Hit Submit to view similarity score.

💬 ChatBot Usage
- Navigate to the ChatBot page.
- Load PDFs into the vector database.
- Choose a model (LLAMA 3 or Gemini).
- Enter your query to chat with the PDFs.
```
📁 File Structure
├── app.py                     # Main Streamlit application
├── compare.py                 # PDF comparison logic
├── pdf_extractor.py           # PDF text extraction
├── text_preprocessing.py      # Sentence preprocessing
├── LLM/
│   ├── gemini.py              # Google Gemini integration
│   ├── llama3.py              # LLAMA 3 integration
│   └── prompt.py              # Prompt generation
├── embeddings/
│   ├── CountVectorizer.py     # Count Vectorizer logic
│   ├── TfidfVectorizer.py     # TF-IDF logic
│   └── all_MiniLM_L6_v2.py    # MiniLM embedding
├── result.py                  # ChatBot response handling
├── requirements.txt           # Python dependencies
└── .env                       # Environment variables (not included)

```

🙏 Acknowledgements
- Streamlit
- Meta LLAMA 3
- OLLAMA
- Chroma Vector DB
- LangChain

Let me know if you'd like help designing a badge set, demo GIFs, or tagline refinements like:
“Empowering document insights through smart similarity scans and conversational AI.” 💡

Want me to write your GitHub repo description or short summary? I’ve got more up my digital sleeve.
