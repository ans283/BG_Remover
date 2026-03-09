import streamlit as st
import os
from PIL import Image
from rembg import remove    

st.title("AI Background Remover")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key="file_uploader")

if uploaded_file:
    img = Image.open(uploaded_file)
    st.subheader("Original Image")
    st.image(img, caption="Original Image", use_container_width=True)

    if st.button("Remove Background", key="remove_bg_button"):
        with st.spinner("Removing background..."):
            output = remove(img)
            st.subheader("Image with Background Removed")
            st.image(output, caption="Background Removed Image", use_container_width=True)

            # Save the output image to a temporary file
            output_path = "output.png"
            output.save(output_path)

            # Provide a download link for the output image
            st.markdown(f"[Download Image](./{output_path})")