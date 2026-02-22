import streamlit as st
import random

st.set_page_config(page_title="KIRAN ALP CBT-2 PREPARATION TRACKER", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>

/* Soft background */
.stApp {
    background-color: #eaf4ff;
}

/* Very light watermark */
.stApp::before {
    content: "";
    background-image: url("https://img.freepik.com/free-vector/student-studying-desk_23-2148880412.jpg");
    background-repeat: no-repeat;
    background-position: center 60%;
    background-size: 600px;
    opacity: 0.05;
    position: fixed;
    width: 100%;
    height: 100%;
    z-index: -1;
}

/* Attractive heading */
.main-title {
    text-align: center;
    font-size: 46px;
    font-weight: 800;
    background: linear-gradient(90deg, #1565c0, #8e24aa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-top: 20px;
}

/* Quote */
.quote-box {
    text-align: center;
    font-size: 22px;
    font-weight: 600;
    margin-top: 40px;
    margin-bottom: 60px;
    color: #5e35b1;
}

/* Section */
.section-box {
    background-color: rgba(255,255,255,0.95);
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 30px;
    box-shadow: 0px 5px 12px rgba(0,0,0,0.1);
}

/* Circle center */
.circle-container {
    display:flex;
    justify-content:center;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="main-title">KIRAN ALP CBT-2 PREPARATION TRACKER</div>', unsafe_allow_html=True)

# ---------------- QUOTE ----------------
quotes = [
    "Small daily progress leads to big success.",
    "Discipline today, selection tomorrow.",
    "Stay focused. Railway dream is loading...",
    "Consistency is your secret weapon.",
    "Study hard now. Shine later."
]

st.markdown(f'<div class="quote-box">💡 {random.choice(quotes)}</div>', unsafe_allow_html=True)

# ---------------- SYLLABUS ----------------
syllabus = {
    "PART A - MATHEMATICS": [
        "Number System","BODMAS","Percentages","Time & Work"
    ],
    "PART A - REASONING": [
        "Analogies","Series","Coding-Decoding","Syllogism"
    ],
    "PART B - TRADE THEORY": [
        "Welding","Lathe","Grinding","Bearings"
    ]
}

total_topics = 0
total_done = 0

# ---------------- SECTIONS ----------------
for section, topics in syllabus.items():

    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader(section)

    done = 0
    for topic in topics:
        if st.checkbox(topic, key=section+topic):
            done += 1

    total_topics += len(topics)
    total_done += done

    completed_percent = int((done / len(topics)) * 100)
    pending_percent = 100 - completed_percent

    st.progress(completed_percent / 100)
    st.write(f"Completed: {completed_percent}%")
    st.write(f"Pending: {pending_percent}%")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- OVERALL PROGRESS ----------------
overall_completed = int((total_done / total_topics) * 100) if total_topics > 0 else 0
overall_pending = 100 - overall_completed

circle_html = f"""
<div class="circle-container">
<svg width="240" height="240">
  <circle cx="120" cy="120" r="100" stroke="#d6e4ff" stroke-width="18" fill="none"/>
  <circle cx="120" cy="120" r="100"
    stroke="#1976d2"
    stroke-width="18"
    fill="none"
    stroke-dasharray="628"
    stroke-dashoffset="{628 - (628 * overall_completed / 100)}"
    stroke-linecap="round"
    transform="rotate(-90 120 120)"
    style="transition: stroke-dashoffset 1.2s ease-in-out;"
  />
  <text x="50%" y="45%" text-anchor="middle"
    font-size="36" fill="black" font-weight="bold">{overall_completed}%</text>
  <text x="50%" y="65%" text-anchor="middle"
    font-size="16" fill="gray">Pending: {overall_pending}%</text>
</svg>
</div>
"""

st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.subheader("Overall Completion Status")
st.markdown(circle_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CELEBRATION ----------------
if overall_completed == 100:
    st.balloons()
    st.success("🎉 Congratulations! You Completed 100% 🎉")
