import streamlit as st
from PIL import Image
import pytesseract

# Function to perform text detection (replace this with your custom function if you have one)
def detect_text(image):
    return pytesseract.image_to_string(image)

# Streamlit app
st.title("Image Text Detection App")

st.write("Upload an image to detect text in it.")

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open and display the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    
    st.write("Detecting text...")
    
    # Detect text
    text = detect_text(image)
    
    # Display the result
    st.write("Detected Text:")
    st.text_area("Text Output", text, height=200)
