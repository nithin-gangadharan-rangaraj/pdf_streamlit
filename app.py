import streamlit as st
import cv2
import numpy as np

PAGE_CONFIG = {"page_title":"Arsya.io","page_icon":":smiley:","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

html = '''
<style>
body {
background-image: url("https://i.pinimg.com/originals/ec/d5/0e/ecd50ed16de87c9a9b972aeba64de53f.jpg");
background-size: cover;
}
</style>
'''


def main():
	st.title("Hello Sannamyr!")
	st.markdown(html, unsafe_allow_html=True)
	uploaded_file = st.file_uploader("Choose a image file", type="jpg")
	if uploaded_file is not None:
    		# Convert the file to an opencv image.
    		file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    		opencv_image = cv2.imdecode(file_bytes, 1)

    		# Now do something with the image! For example, let's display it:
    		st.image(opencv_image, channels="BGR")

if __name__ == '__main__':
	main()



	
