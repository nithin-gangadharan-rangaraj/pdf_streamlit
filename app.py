import streamlit as st
import cv2
import numpy as np

PAGE_CONFIG = {"page_title":"Arsya.io","page_icon":":smiley:","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

html = '''
<style>
body {
background-image: url("https://media.istockphoto.com/vectors/human-heart-anatomy-form-lines-and-triangles-point-connecting-network-vector-id943649026?k=6&m=943649026&s=612x612&w=0&h=zPjXH1Dfk8HJQJs-1OyZVyN7OJKv9uhl5n2SvsWf0Io=");
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



	
