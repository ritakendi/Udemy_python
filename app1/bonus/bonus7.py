import streamlit as st
from PIL import Image

with st.expander("start Camera"):
    # start the camera
    camera_image = st.camera_input("Camera")


if camera_image:
    # create a pillow image instance
    img = Image.open(camera_image)

    # convert the pillow image to greyscale
    gray_img = img.convert('L')

    # Render the greyscale image on the webpage
    st.image(gray_img)
