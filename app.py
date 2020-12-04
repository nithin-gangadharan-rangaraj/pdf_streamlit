import streamlit as st
if __name__ == "__main__":
  uploaded_file = st.file_uploader("Choose a file")
  if uploaded_file is not None:
    stringio = StringIO(uploaded_file.decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data)
