import streamlit as st
import random

st.set_page_config(page_title="KIRAN ALP CBT-2 PREPARATION TRACKER", layout="wide")

# ---------- CLEAN LIGHT BLUE + STUDY GIRL WATERMARK ----------
st.markdown("""
<style>
.stApp {
    background-color: #e3f2fd;
    background-image: url("https://img.freepik.com/free-vector/girl-studying-concept-illustration_114360-1465.jpg");
    background-repeat: no-repeat;
    background-position: center;
    background-size: 500px;
    background-attachment: fixed;
    opacity: 1;
}

/* make watermark very light */
.stApp::after {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url("https://img.freepik.com/free-vector/girl-studying-concept-illustration_114360-1465.jpg");
    background-repeat: no-repeat;
    background-position: center;
    background-size: 500px;
    opacity: 0.06;
    z-index: -1;
}

h1 {
    text-align: center;
    color: black;
    font-size: 42px;
}

.center-quote {
    text-align: center;
    font-size: 20px;
    font-weight: 500;
    margin-bottom: 30px;
    color: black;
}

.section-box {
    background-color: rgba(255,255,255,0.95);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 25px;
    box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
    color: black;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>KIRAN ALP CBT-2 PREPARATION TRACKER</h1>", unsafe_allow_html=True)

quotes = [
    "Stay focused. Railway selection is loading...",
    "Small daily progress leads to big success.",
    "Consistency beats talent.",
    "Dream it. Study it. Achieve it.",
    "Your ALP badge is waiting."
]

st.markdown(f'<div class="center-quote">💡 {random.choice(quotes)}</div>', unsafe_allow_html=True)

# Simple Sample Section
topics = ["Number System", "BODMAS", "Percentages", "Time & Work"]

st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.subheader("PART A - MATHEMATICS")

done = 0
for topic in topics:
    if st.checkbox(topic):
        done += 1

percent = int((done / len(topics)) * 100)
st.progress(percent / 100)
st.write(f"Completion: {percent}%")

st.markdown('</div>', unsafe_allow_html=True)

if percent == 100:
    st.balloons()
