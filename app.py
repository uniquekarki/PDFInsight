import cohere
from dotenv import load_dotenv
import fitz  # PyMuPDF
import os
import streamlit as st
from together import Together

load_dotenv()

# Access the API key and endpoint
client = Together(api_key=os.environ.get('TOGETHER_API_KEY'))

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def summarize_text(text):
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        messages=[
            {
                    "role": "user",
                    "content": f"Summarize this text {text}"
            }
    ],
        max_tokens=512,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>","<|eom_id|>"],
    )
    return(response.choices[0].message.content)

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
    prompt = st.chat_input("Ask question about PDF")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")