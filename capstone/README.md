# Kaggle Mentor AI (Simple)

A simplified Kaggle mentor application featuring a Competition Analyzer, a Notebook Explainer, and a text-based RAG Knowledge Base.

## Project Structure

```
kaggle_mentor_ai/
├── app.py              # Main Streamlit user interface
├── requirements.txt    # Python dependencies
├── README.md           # Documentation
├── .env.example        # Environment variables template
├── kaggle_tips.txt     # RAG document source containing 10 Kaggle tips
└── src/
    ├── __init__.py
    ├── config.py       # Configuration and keys
    ├── gemini_client.py # Gemini API connection helpers
    └── rag_store.py    # FAISS index and search manager
```

## Setup Instructions

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Setup environment variables:
   Copy `.env.example` to `.env` and fill in your `GEMINI_API_KEY`.
3. Run Streamlit:
   ```bash
   streamlit run app.py
   ```
