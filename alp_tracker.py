import streamlit as st
import random

st.set_page_config(page_title="KIRAN ALP CBT-2 PREPARATION TRACKER", layout="wide")

# ---------------- BACKGROUND STYLE ----------------
st.markdown("""
<style>

/* Main soft background */
.stApp {
    background-color: #e6f2ff;
}

/* Very light watermark study student on bench */
.stApp::before {
    content: "";
    background-image: url("https://img.freepik.com/free-vector/student-studying-desk_23-2148880412.jpg");
    background-repeat: no-repeat;
    background-position: center 60%;
    background-size: 600px;
    opacity: 0.05;   /* very light watermark */
    position: fixed;
    width: 100%;
    height: 100%;
    z-index: -1;
}

/* Title */
h1 {
    text-align: center;
    color: black;
    font-size: 42px;
}

/* Centered quote with space */
.quote-box {
    text-align: center;
    font-size: 22px;
    font-weight: 600;
    margin-top: 40px;
    margin-bottom: 60px;
    color: #5e35b1;   /* unique purple shade */
}

/* Section style */
.section-box {
    background-color: rgba(255,255,255,0.95);
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 30px;
    box-shadow: 0px 5px 12px rgba(0,0,0,0.1);
}

/* Center circle container */
.circle-container {
    display:flex;
    justify-content:center;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1>KIRAN ALP CBT-2 PREPARATION TRACKER</h1>", unsafe_allow_html=True)

# ---------------- CENTER QUOTE ----------------
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

# ---------------- DISPLAY SECTIONS ----------------
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

# ---------------- TZN STYLE ANIMATED CIRCLE ----------------
overall = int((total_done / total_topics) * 100) if total_topics > 0 else 0

circle_html = f"""
<div class="circle-container">
<svg width="230" height="230">
  <circle cx="115" cy="115" r="95" stroke="#cfe2ff" stroke-width="18" fill="none"/>
  <circle cx="115" cy="115" r="95"
    stroke="#1976d2"
    stroke-width="18"
    fill="none"
    stroke-dasharray="597"
    stroke-dashoffset="{597 - (597 * overall / 100)}"
    stroke-linecap="round"
    transform="rotate(-90 115 115)"
    style="transition: stroke-dashoffset 1.2s ease-in-out;"
  />
  <text x="50%" y="50%" text-anchor="middle" dy=".3em"
    font-size="36" fill="black" font-weight="bold">{overall}%</text>
</svg>
</div>
"""

st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.subheader("Overall Completion")
st.markdown(circle_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CELEBRATION ----------------
if overall == 100:
    st.balloons()
    st.success("🎉 Congratulations! You Completed 100% 🎉")
