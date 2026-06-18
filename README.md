# Rag-m-Model-summarizer
An AI-powered RAG application that summarizes  PDF and TXT documents using LangChain and  Mistral AI, built with a Streamlit interface  for real-time document summarization.

# RAG Document Summarizer

An end-to-end Retrieval-Augmented Generation (RAG) 
based application that summarizes PDF and TXT 
documents using LLM APIs. Upload any document and 
get an instant AI-generated summary.

## Features

- Upload PDF or TXT files
- Automatic text extraction and chunking
- Context-aware retrieval using RAG pipeline
- AI-generated summaries using Mistral AI
- Simple and interactive Streamlit interface

## Tech Stack

- **Language:** Python
- **Framework:** LangChain
- **LLM API:** Mistral AI
- **Frontend:** Streamlit
- **PDF Processing:** PyMuPDF

## How It Works

1. User uploads a PDF or TXT file
2. Document is parsed and split into chunks
3. Relevant chunks are retrieved based on context
4. Mistral AI generates a concise summary
5. Summary is displayed on the Streamlit interface

## Installation

```bash
git clone https://github.com/Chinmay-Nanda/RAG-Document-Summarizer.git
cd RAG-Document-Summarizer
pip install -r requirements.txt
streamlit run app.py
```

## Usage

1. Run the Streamlit app
2. Upload a PDF or TXT file
3. Wait for processing
4. View the generated summary

## Future Improvements

- Add support for DOCX files
- Add multi-language summarization
- Deploy on Streamlit Cloud
- Add downloadable summary feature
