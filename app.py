import streamlit as st
from transformers import pipeline
import PyPDF2

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function to summarize text
def summarize_text(text):
    # Summarize text
    summary = summarizer(text, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
    return summary[0]['summary_text']

# Streamlit application
st.set_page_config(page_title="Collaborative Summarizer", page_icon="📝", layout="wide")

# Custom CSS styles
st.markdown("""
    <style>
    .reportview-container {
        background: url('https://your-image-url.com/background.jpg');
        background-size: cover;
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background: url('https://your-image-url.com/sidebar-background.jpg');
        background-size: cover;
    }
    h1, h2, h3 {
        color: #FFD700;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .stTextArea textarea {
        background-color: #333;
        color: white;
    }
    .stFileUploader label {
        color: #FFD700;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📝 Collaborative Summarizer")

st.write("""
## 🌟 Welcome to the Collaborative Summarizer!
Upload a PDF file or enter text below to get a concise summary using state-of-the-art AI technology.
""")

st.write("### 🚀 Powered by Llama 3 and Streamlit")

# Layout for file upload and text input
col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Upload a PDF File")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        st.write("Processing your PDF file...")
        try:
            # Use PdfReader instead of PdfFileReader
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            pdf_text = ""
            for page in pdf_reader.pages:
                pdf_text += page.extract_text()

            if pdf_text:
                st.write("### 📜 Extracted Text from PDF:")
                st.text_area("Extracted Text", value=pdf_text, height=200, disabled=True)

                st.write("### ✨ Summary:")
                with st.spinner("Generating summary..."):
                    summary = summarize_text(pdf_text)
                st.success("Summary generated successfully! 🎉")
                st.write("### Summary:")
                st.write(summary)  # Changed to st.write() for displaying the summary
            else:
                st.error("No text found in the PDF. ⚠️")
        except Exception as e:
            st.error(f"An error occurred while processing the PDF: {e} ❌")

with col2:
    st.subheader("📝 Enter Text Directly")
    input_text = st.text_area("Text Input", height=200)

    if st.button("Generate Summary", key="text_summary"):
        if input_text:
            st.write("### ✨ Summary:")
            with st.spinner("Generating summary..."):
                summary = summarize_text(input_text)
            st.success("Summary generated successfully! 🎉")
            st.write("### Summary:")
            st.write(summary)  # Changed to st.write() for displaying the summary
        else:
            st.error("Please enter some text. ⚠️")

st.write("### 🤖 Project created using Llama 3")
