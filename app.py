import streamlit as st
import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

st.title("PDF Summarizer")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    st.write(text)