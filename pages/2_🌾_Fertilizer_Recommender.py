import streamlit as st
import random

st.set_page_config(layout="wide")

# 🌄 BACKGROUND
st.markdown("""
<style>
.stApp {
background: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
url("https://images.unsplash.com/photo-1501004318641-b39e6451bec6");
background-size: cover;
color:white;
}
.block-container {
background: rgba(0,0,0,0.4);
padding: 30px;
border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

st.title("🌾 Smart Fertilizer Advisor")
st.markdown("### 🌱 Soil → Nutrient → Growth Cycle")
st.progress(70)

st.markdown("Get intelligent fertilizer recommendations based on your crop and soil.")

# INPUTS
crop = st.selectbox("🌱 Crop", ["Tomato","Potato","Wheat"])
soil = st.selectbox("🌍 Soil Type", ["Sandy","Loamy","Clay"])

if st.button("Get Recommendation"):

    # RANDOM LOGIC (you can improve later)
    npk = random.choice(["10-20-10","20-10-10","15-15-15"])
    dose = random.randint(200,300)

    st.markdown("## 📊 Recommended Plan")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("NPK Ratio", npk)
        st.metric("Dosage", f"{dose} kg/ha")

    with col2:
        cost = dose * 5
        st.metric("Estimated Cost", f"₹{cost}")
        st.success("✔ Suitable for your soil & crop")

    st.markdown("---")

    # 🧠 EXPLANATION
    st.markdown("## 🧠 What is NPK?")

    st.info("""
    **NPK stands for:**
    
    - **N (Nitrogen)** → Helps leaf growth 🌿  
    - **P (Phosphorus)** → Helps root & flower growth 🌼  
    - **K (Potassium)** → Improves disease resistance 💪  
    """)

    st.markdown(f"👉 Your ratio **{npk}** means balanced nutrients for your crop.")

    st.markdown("---")

    # 🌾 REAL FERTILIZER SUGGESTIONS
    st.markdown("## 🌾 Recommended Fertilizers")

    st.write("""
    Based on your inputs, you can use:

    - **Urea** → High Nitrogen (boosts leaf growth)  
    - **DAP (Di-Ammonium Phosphate)** → Good for roots  
    - **MOP (Muriate of Potash)** → Improves resistance  
    """)

    st.markdown("---")

    # 🚜 APPLICATION GUIDE
    st.markdown("## 🚜 How to Apply")

    st.success("""
    1. Apply during early growth stage  
    2. Mix fertilizer evenly in soil  
    3. Avoid application before heavy rain  
    4. Water after application  
    """)

    st.markdown("---")

    # 💡 SMART TIPS
    st.markdown("## 💡 Smart Farming Tips")

    st.warning("""
    - Do not overuse fertilizer ❗  
    - Test soil pH for best results  
    - Combine with organic compost for better yield  
    """)

else:
    st.info("Select crop and soil, then click recommendation")