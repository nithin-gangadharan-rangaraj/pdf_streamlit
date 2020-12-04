import streamlit as st
from PyPDF2 import PdfFileReader

def read_pdf(file):
	pdfReader = PdfFileReader(file)
	count = pdfReader.numPages
	all_page_text = ""
	for i in range(count):
		page = pdfReader.getPage(i)
		all_page_text += page.extractText()

	return all_page_text

def main():
	uploaded_file = st.file_uploader("Choose a file")
  	if uploaded_file is not None:
    	raw_text = read_pdf(docx_file)
    	st.write(raw_text)
