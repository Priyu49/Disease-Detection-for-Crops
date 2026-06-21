import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""<style>
.stApp {
background: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
url("https://images.unsplash.com/photo-1501004318641-b39e6451bec6");
background-size: cover;
color:white;
}
</style>""", unsafe_allow_html=True)

st.title("🤖 Farm Assistant")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

msg = st.chat_input("Ask anything...")

if msg:
    st.session_state.messages.append({"role":"user","content":msg})

    if "disease" in msg.lower():
        reply="Upload image in disease page"
    else:
        reply="I help with farming 🌱"

    st.session_state.messages.append({"role":"assistant","content":reply})

    with st.chat_message("assistant"):
        st.write(reply)