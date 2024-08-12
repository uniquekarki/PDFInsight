# PDFInsight

PDFInsight is a PDF summarization tool that leverages advanced natural language processing (NLP) models to generate concise summaries of lengthy PDF documents. The tool is designed to help users quickly understand the key points of a document without having to read through the entire text.

## Features

- Upload PDF files and extract text
- Summarize extracted text using Cohere's powerful NLP models
- Interactive Streamlit interface for easy use

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PDFInsight.git
   cd PDFInsight

2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate   # On Windows, use `env\Scripts\activate`

3. Install the required packages:
    ```bash
    pip install -r requirements.txt

4. Set up Cohere API key:
    - Obtain your API key from Cohere.
    - Create a `.env` file in the project directory and add your API key:
    ```bash
    API_KEY=your_api_key_here

## Usage

1. Run the Streamlit app:
    ```
    streamlit run app.py
    ```
2. Open your web browser and go to http://localhost:8501 to use PDFInsight.

3. Upload a PDF file, extract the text, and click the "Summarize" button to get the summarized content.

## File Structure

    PDFInsight/
    ├── app.py                 # Main Streamlit application
    ├── requirements.txt       # List of dependencies
    ├── .env                   # Environment variables file for API keys
    └── README.md              # Project README file
