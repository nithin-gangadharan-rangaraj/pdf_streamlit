import streamlit as st
import cv2
import numpy as np

PAGE_CONFIG = {"page_title":"Arsya.io","page_icon":":smiley:","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

def main():
	st.title("Hello Saannmyr!")
	uploaded_file = st.file_uploader("Choose a image file", type="jpg")
	if uploaded_file is not None:
    		# Convert the file to an opencv image.
    		file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    		opencv_image = cv2.imdecode(file_bytes, 1)

    		# Now do something with the image! For example, let's display it:
    		st.image(opencv_image, channels="BGR")

if __name__ == '__main__':
	main()



	
