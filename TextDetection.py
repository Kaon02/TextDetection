import streamlit as st
from PIL import Image
import pytesseract

# Set the path to Tesseract (update this to your Tesseract path)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Update this path

# Streamlit app to upload an image and display OCR results
def main():
    st.title("OCR Text Detection")

    st.write("Upload an image and the app will detect the text.")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Open the image using PIL
        image = Image.open(uploaded_file)

        # Display the image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Apply OCR to the image
        detected_text = pytesseract.image_to_string(image)

        # Show the detected text
        if detected_text.strip():
            st.subheader("Detected Text:")
            st.text_area("Text", detected_text, height=200)
        else:
            st.write("No text detected in this image.")

if __name__ == "__main__":
    main()
