import streamlit as st
import random

st.set_page_config(page_title="KIRAN ALP CBT-2 PREPARATION TRACKER", layout="wide")

# ---------- LIGHT BLUE BACKGROUND + TRAIN WATERMARK ----------
st.markdown("""
<style>

/* Main app background */
.stApp {
    background-color: #d6ecff;
    position: relative;
}

/* Train watermark layer */
.stApp::before {
    content: "";
    background-image: url("https://pngimg.com/uploads/train/train_PNG101529.png");
    background-repeat: no-repeat;
    background-position: center;
    background-size: 50%;
    opacity: 0.08;   /* makes it watermark style */
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #0d47a1;
    margin-bottom: 20px;
}

/* Section box */
.section-box {
    background-color: rgba(255,255,255,0.95);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 25px;
    box-shadow: 0px 6px 15px rgba(0,0,0,0.15);
}

/* Quote box */
.quote-box {
    background-color: rgba(255,255,255,0.9);
    padding: 15px;
    border-radius: 10px;
    text-align:center;
    font-size:18px;
    margin-bottom:20px;
}

/* Circle center */
.circle-container {
    display:flex;
    justify-content:center;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="main-title">🚆 KIRAN ALP CBT-2 PREPARATION TRACKER 🚆</div>', unsafe_allow_html=True)

st.write("Background applied successfully 🚆✨")
