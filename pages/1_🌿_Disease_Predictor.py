import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import json
from database import insert_data

st.set_page_config(layout="wide")

# BACKGROUND
st.markdown("""
<style>
.stApp {
background: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
url("https://images.unsplash.com/photo-1501004318641-b39e6451bec6");
background-size: cover;
color:white;
}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("models/crop_disease_model.h5")
    with open("models/class_indices.json") as f:
        class_indices = json.load(f)
    return model, {v:k for k,v in class_indices.items()}

model, class_names = load_model()

st.title("🌿 Disease Detection")

file = st.file_uploader("Upload leaf image", key="disease_upload")

if file:
    img = Image.open(file)
    st.image(img)

    arr = np.array(img.resize((224,224)))/255.0
    arr = np.expand_dims(arr,0)

    pred = model.predict(arr)
    idx = np.argmax(pred)

    disease = class_names[idx]
    conf = float(pred[0][idx]*100)

    insert_data(disease, conf)

    st.markdown(f"## 🌿 {disease}")
    st.metric("Confidence", f"{conf:.1f}%")

    if conf>80:
        st.error("Severe infection 🚨")
    else:
        st.warning("Moderate infection ⚠️")

    st.info("Remove infected leaves and apply treatment")

else:
    st.info("Upload image to start")