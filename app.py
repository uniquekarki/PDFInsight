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
                "content": f"Summarize this text: {text}"
            }
        ],
        max_tokens=512,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>","<|eom_id|>"],
    )
    return response.choices[0].message.content

def answer_question(text, question):
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": f"Given the following text, answer the question: {text}\n\nQuestion: {question}"
            }
        ],
        max_tokens=512,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>","<|eom_id|>"],
    )
    return response.choices[0].message.content

st.title("PDF Summarizer & Q&A")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# Initialize session state variables
if 'summary' not in st.session_state:
    st.session_state.summary = None
if 'text' not in st.session_state:
    st.session_state.text = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []  # List to store chat history

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    st.subheader("Extracted Text:")
    st.write(text)
    st.session_state.text = text  # Store the extracted text in session state

    if st.button("Summarize"):
        summary = summarize_text(text)
        st.subheader("Summary:")
        st.write(summary)
        st.session_state.summary = summary  # Store the summary in session state

# Display the summary if it has been generated
if st.session_state.summary:
    st.subheader("Summary:")
    st.write(st.session_state.summary)

    # Display the chat history
    for chat in st.session_state.chat_history:
        st.write(f"**User:** {chat['question']}")
        st.write(f"**Assistant:** {chat['answer']}")

    # Get user input
    prompt = st.chat_input("Ask question about PDF")
    if prompt:
        answer = answer_question(st.session_state.text, prompt)
        
        # Store the new Q&A in the chat history
        st.session_state.chat_history.append({"question": prompt, "answer": answer})
        
        # Display the latest Q&A
        st.write(f"**User:** {prompt}")
        st.write(f"**Assistant:** {answer}")
