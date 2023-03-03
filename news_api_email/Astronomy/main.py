import streamlit as st
import requests

# Prepare an API key and API url.
api_key = "5JDFwWjggMeX6fjp0IggloGPgtkbavFSYMmRLC5K"
url = "https://api.nasa.gov/planetary/apod" \
        f"api_key={api_key}"

# Get the requeat data as a dictionary.
response1 = requests.get(url)
data = response1.json()

# Extract the image title, url and, explanation.
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# Download the Image
image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)