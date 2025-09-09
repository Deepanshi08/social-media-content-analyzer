import streamlit as st
import pdfplumber
import pytesseract
from PIL import Image
import io

st.set_page_config(page_title="Social Media Content Analyzer", layout="wide")

st.title("📄 Social Media Content Analyzer")
st.write("Upload a PDF or Image file to extract the text content.")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF or Image file", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file is not None:
    file_type = uploaded_file.type

    extracted_text = ""

    if "pdf" in file_type:
        # Handle PDF
        try:
            with pdfplumber.open(uploaded_file) as pdf:
                for page in pdf.pages:
                    extracted_text += page.extract_text() or ""
            if not extracted_text.strip():
                st.warning("No text found in the PDF.")
        except Exception as e:
            st.error(f"Error while reading PDF: {e}")

    elif "image" in file_type:
        # Handle Image with OCR
        try:
            image = Image.open(uploaded_file)
            extracted_text = pytesseract.image_to_string(image)
            if not extracted_text.strip():
                st.warning("No text could be extracted from the image.")
        except Exception as e:
            st.error(f"Error while proces
