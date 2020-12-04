import streamlit as st
import pdfplumber


def main():
	docx_file = st.file_uploader("Upload File",type=['txt','docx','pdf'])
	if docx_file is not None:
    		try:
			with pdfplumber.open(docx_file) as pdf:
				page = pdf.pages[0]
				st.write(page.extract_text())
		except:
			st.write("None")

if __name__ == '__main__':
	main()
