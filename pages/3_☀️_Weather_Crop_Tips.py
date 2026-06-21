import streamlit as st
import requests

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
</style>
""", unsafe_allow_html=True)

st.title("☀️ Smart Crop Advisory System")

# 📥 INPUTS
city = st.text_input("Enter city", "Pune", key="weather_city")

crop = st.selectbox("Select Crop", ["Tomato", "Wheat", "Rice"], key="crop_select")

stage = st.selectbox("Growth Stage", 
                     ["Seedling", "Vegetative", "Flowering", "Harvest"],
                     key="stage_select")

API_KEY = "212465b5d29a05b1d1a084d16052d5e8"

if st.button("Get Smart Advice"):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "main" in data:

            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["main"]

            # 📊 DISPLAY WEATHER
            col1, col2, col3 = st.columns(3)

            col1.metric("🌡 Temp", f"{temp}°C")
            col2.metric("💧 Humidity", f"{humidity}%")
            col3.metric("☁️ Condition", condition)

            st.markdown("---")

            st.markdown("## 🌱 Detailed Crop Advisory")

            tips = []

            # 🌾 CROP-SPECIFIC LOGIC

            if crop == "Tomato":

                if stage == "Seedling":
                    tips.append("🌱 Maintain moist soil, avoid waterlogging")
                
                if stage == "Vegetative":
                    tips.append("🌿 Apply nitrogen fertilizer for leaf growth")
                
                if stage == "Flowering":
                    tips.append("🌸 Avoid excess watering to prevent flower drop")
                
                if stage == "Harvest":
                    tips.append("🍅 Reduce watering to improve fruit quality")

                # Weather impact
                if humidity > 70:
                    tips.append("⚠️ Tomato is prone to fungal diseases → use fungicide spray")

                if temp > 32:
                    tips.append("💧 High temp → irrigate early morning or evening")

            elif crop == "Wheat":

                if stage == "Seedling":
                    tips.append("🌱 Light irrigation required for germination")

                if stage == "Vegetative":
                    tips.append("🌾 Apply nitrogen fertilizer for tillering")

                if stage == "Flowering":
                    tips.append("🌼 Ensure proper irrigation for grain formation")

                if stage == "Harvest":
                    tips.append("🌾 Avoid irrigation before harvesting")

                if temp > 30:
                    tips.append("⚠️ Heat stress may reduce yield")

            elif crop == "Rice":

                if stage == "Seedling":
                    tips.append("🌱 Maintain standing water in field")

                if stage == "Vegetative":
                    tips.append("🌾 Ensure proper water level")

                if stage == "Flowering":
                    tips.append("🌸 Avoid water stress during flowering")

                if stage == "Harvest":
                    tips.append("🌾 Drain field before harvesting")

                if "Rain" in condition:
                    tips.append("🌧 Excess rain → ensure proper drainage")

            # 🌤 GENERAL WEATHER RULES

            if "Rain" in condition:
                tips.append("🌧 Avoid fertilizer application today")

            if "Clear" in condition:
                tips.append("☀️ Good time for irrigation and spraying")

            if humidity < 40:
                tips.append("🌵 Soil may dry quickly → increase watering")

            # 📋 DISPLAY TIPS
            if tips:
                for tip in tips:
                    st.success(tip)
            else:
                st.info("Normal conditions")

        else:
            st.error("Weather data not available")

    else:
        st.error("Invalid city or API issue")