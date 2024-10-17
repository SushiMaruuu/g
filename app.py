# # importing required modules
# from pypdf import PdfReader

# # creating a pdf reader object
# reader = PdfReader('sample.pdf')

# # printing number of pages in pdf file
# print(len(reader.pages))

# # getting a specific page from the pdf file
# page = reader.pages[0]

# # extracting text from page
# text = page.extract_text()
# print(text)

import streamlit as st
from pypdf import PdfReader

# Streamlit app
st.title("PDF Text Extractor")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    # Display file details
    st.write("Filename: ", uploaded_file.name)

    # Read the uploaded PDF
    reader = PdfReader(uploaded_file)

    # Create a container to display extracted text
    st.subheader("Extracted Text")

    # Iterate through pages and extract text
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        st.write(f"**Page {i + 1}:**")
        st.write(text)

    # Optionally, show a message if no text is found
    if not any(page.extract_text() for page in reader.pages):
        st.write("No text found in the PDF.")
