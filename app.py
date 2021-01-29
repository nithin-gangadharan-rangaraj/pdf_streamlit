import streamlit as st
import cv2
import numpy as np
import pickle
import sklearn

PAGE_CONFIG = {"page_title":"Arsya.io","page_icon":":smiley:","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

html = '''
<style>
body {
background-image: url("https://img.freepik.com/free-vector/white-elegant-texture-wallpaper_23-2148421854.jpg?size=626&ext=jpg&ga=GA1.2.145878890.1611360000");
background-size: cover;
}
</style>
'''
pickle_in = open('knn.pkl', 'rb') 
clf = pickle.load(pickle_in)

pickle_in1 = open('svm_classifier.pkl','rb')
clf_svm = pickle.load(pickle_in1)

def scale_fun(data):
	mean = [ 51.12846111, 240.48910043, 135.62179425,  84.37183021, 26.05929871,  75.67808511,  83.90784418]
	scale = [ 8.29909773, 45.64248672, 23.34040109, 12.31718928,  3.94429646, 11.46452091, 29.47992596]
	transformed_data = []
	for i in range(0,7):
		x = (data[i] - mean[i])/scale[i]
		transformed_data.append(round(x, 8))
	return(transformed_data)

def main():
	st.title("Heart Risk prediction!")
	st.markdown(html, unsafe_allow_html=True)
	age = st.number_input("Enter Age")
	totChol = st.number_input("Enter Cholesterol")
	sysBP = st.number_input("Enter Systolic BP")
	diaBP = st.number_input("Enter Diastolic BP")
	BMI = st.number_input("Enter BMI")
	heartrate = st.number_input("Enter Heart Rate")
	glucose = st.number_input("Enter Glucose")
	st.text(clf)
	x = [age, totChol, sysBP, diaBP, BMI, heartrate, glucose]
	new = np.array(scale_fun(x))
	if(st.button("Predict using KNN")):
		if (clf.predict(new.reshape(1, -1))==1):
  			st.text("Risk")
		else:
  			st.text("Safe")
	st.text(clf_svm)
	if(st.button("Predict using SVM")):
		if (clf_svm.predict(new.reshape(1, -1))==1):
  			st.text("Risk")
		else:
  			st.text("Safe")
	st.text(sklearn.__version__)
	

if __name__ == '__main__':
	main()



	
