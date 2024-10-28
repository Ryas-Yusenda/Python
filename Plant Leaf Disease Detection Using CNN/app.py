"""Web application for apple"""

from img_classification import teachable_machine_classification
from PIL import Image

import streamlit as st

st.title("Image Classification CNN")
st.header("Klasifikasi Penyakit Daun Apel")
st.text("Upload gambar Daun Apel untuk di prediksi")

uploaded_file = st.file_uploader("Choose an image", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Gambar.", use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = teachable_machine_classification(image, "model_last.hdf5")
    if label == 0:
        st.write("Prediksi gambar ini adalah Apple Scab")
    if label == 1:
        st.write("Prediksi gambar ini adalah Apple Black Rot")
    if label == 2:
        st.write("Prediksi gambar ini adalah Cedar Apple Rust")
    if label == 3:
        st.write("Prediksi gambar ini adalah Apple Healthy")
