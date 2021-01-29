import streamlit as st

PAGE_CONFIG = {"page_title":"Arsya.io","page_icon":":smiley:","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

def main():
	st.title("Hello Arsya!")

if __name__ == '__main__':
	main()
