import os
from dotenv import load_dotenv
import streamlit as st
import fitz  # PyMuPDF

load_dotenv()

# Access the API key and endpoint
api_key = os.getenv("API_KEY")

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def summarize_text(text):
    pass

st.title("PDF Summarizer")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    st.subheader("Extracted Text:")
    st.write(text)

    if st.button("Summarize"):
        summary = summarize_text(text)
        st.subheader("Summary:")
        st.write(summary)