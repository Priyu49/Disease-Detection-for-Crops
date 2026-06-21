import streamlit as st

st.set_page_config(page_title="FarmSense AI", page_icon="🌱", layout="wide")

# 🌄 BACKGROUND + OVERLAY
st.markdown("""
<style>
.stApp {
    background: 
        linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)),
        url("https://images.unsplash.com/photo-1501004318641-b39e6451bec6");
    background-size: cover;
    background-position: center;
    color: white;
}

/* GLASS CARD */
.card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    text-align: center;
    transition: 0.3s;
}

/* HOVER EFFECT */
.card:hover {
    transform: translateY(-5px);
    background: rgba(255,255,255,0.12);
}

/* TITLE */
.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #d1d5db;
}
</style>
""", unsafe_allow_html=True)

# 🌱 HERO SECTION
st.markdown('<div class="title">🌱 FarmSense AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered crop health assistant</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# 🎯 FEATURE CARDS (NO RANDOM IMAGES)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h2>🌿</h2>
        <h3>Disease Detection</h3>
        <p>Upload leaf image and detect diseases instantly with AI.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h2>🌾</h2>
        <h3>Fertilizer Advisor</h3>
        <p>Get the right fertilizer based on soil and crop conditions.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h2>☀️</h2>
        <h3>Weather Insights</h3>
        <p>Smart weather-based tips to improve crop productivity.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 💡 PROJECT PURPOSE (VERY IMPORTANT)
st.markdown("## 💡 Why This Project Matters")

st.markdown("""
- 🌍 Helps farmers reduce crop losses  
- 💰 Saves money on fertilizers  
- ⚡ Instant AI-based decisions  
- 📱 Simple and accessible for everyone  
""")

st.markdown("<br>", unsafe_allow_html=True)

# 🚀 HOW TO USE
st.markdown("## 🚀 How to Use")

st.markdown("""
1. Upload leaf image → Detect disease  
2. Enter crop & soil → Get fertilizer  
3. Enter city → Get weather tips  

👉 Everything in one smart system
""")

st.success("👈 Use sidebar to explore features")