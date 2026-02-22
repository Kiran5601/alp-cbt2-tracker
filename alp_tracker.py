import streamlit as st
import random

st.set_page_config(page_title="KIRAN ALP CBT-2 PREPARATION TRACKER", layout="wide")

# ---------------- LIGHT BACKGROUND WITH STUDY GIRL WATERMARK ----------------
st.markdown("""
<style>
.stApp {
    background-color: #e3f2fd;
    position: relative;
}

/* Soft watermark image */
.stApp::before {
    content: "";
    background-image: url("https://img.freepik.com/free-vector/girl-studying-concept-illustration_114360-1465.jpg");
    background-repeat: no-repeat;
    background-position: center;
    background-size: 500px;
    opacity: 0.08;   /* makes it very light */
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
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

.circle-container {
    display:flex;
    justify-content:center;
    margin-top:20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1>KIRAN ALP CBT-2 PREPARATION TRACKER</h1>", unsafe_allow_html=True)

# ---------------- CENTERED QUOTES ----------------
quotes = [
    "Stay focused. Railway selection is loading...",
    "Small daily progress leads to big success.",
    "Consistency beats talent.",
    "Dream it. Study it. Achieve it.",
    "Your ALP badge is waiting."
]

st.markdown(f'<div class="center-quote">💡 {random.choice(quotes)}</div>', unsafe_allow_html=True)

# ---------------- SAMPLE SYLLABUS ----------------
syllabus = {
    "PART A - MATHEMATICS": ["Number System","BODMAS","Percentages","Time & Work"],
    "PART A - REASONING": ["Analogies","Series","Coding-Decoding","Syllogism"],
    "PART A - SCIENCE": ["Units","Heat","Electricity","Energy"],
    "PART B - TRADE THEORY": ["Welding","Lathe","Grinding","Bearings"]
}

total_topics = 0
total_done = 0

# ---------------- DISPLAY ----------------
for section, topics in syllabus.items():

    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader(section)

    done = 0
    for topic in topics:
        if st.checkbox(topic, key=section+topic):
            done += 1

    total_topics += len(topics)
    total_done += done

    percent = int((done / len(topics)) * 100)

    st.progress(percent / 100)
    st.write(f"Completion: {percent}%")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- ANIMATED OVERALL CIRCLE ----------------
overall = int((total_done / total_topics) * 100) if total_topics > 0 else 0

circle_html = f"""
<div class="circle-container">
<svg width="220" height="220">
  <circle cx="110" cy="110" r="90" stroke="#bbdefb" stroke-width="15" fill="none"/>
  <circle cx="110" cy="110" r="90"
    stroke="#2196f3"
    stroke-width="15"
    fill="none"
    stroke-dasharray="565"
    stroke-dashoffset="{565 - (565 * overall / 100)}"
    stroke-linecap="round"
    transform="rotate(-90 110 110)"
    style="transition: stroke-dashoffset 1s ease;"
  />
  <text x="50%" y="50%" text-anchor="middle" dy=".3em"
    font-size="32" fill="black">{overall}%</text>
</svg>
</div>
"""

st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.subheader("Overall Completion")
st.markdown(circle_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CONFETTI ----------------
if overall == 100:
    st.balloons()
    st.success("🎉 100% Completed! Excellent Work!")
