import streamlit as st
from PIL import Image

st.subheader("color to Grayscale Converter")

# create a file uploader component allowing the user to upload a file
uploaded_image = st.file_uploader("Upload Image")

with st.expander("start Camera"):
    # start the camera
    camera_image = st.camera_input("Camera")
    
if camera_image:
    # create a pillow image instance
    img = Image.open(camera_image)
    # convert the pillow image to greyscale
    gray_camera_img = img.convert('L')
    # Render the greyscale image on the webpage
    st.image(gray_camera_img)

# check if the image exists meaning the user uploaded a file
if  uploaded_image:
    # open the user uploaded image with pillow
    img = Image.open(uploaded_image)
    # convert the image to greyscale on the webpage
    grey_uploaded_img = img.convert('L')
    # display the greyscale image on the webpage
    st.image(grey_uploaded_img)
