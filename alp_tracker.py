import streamlit as st
import random

st.set_page_config(page_title="KIRAN ALP CBT-2 PREPARATION TRACKER", layout="wide")

# ---------- RAILWAY BACKGROUND ----------
st.markdown("""
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee");
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
}
.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: white;
    margin-bottom: 20px;
}
.section-box {
    background-color: rgba(255,255,255,0.95);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 25px;
    box-shadow: 0px 6px 15px rgba(0,0,0,0.3);
}
.quote-box {
    background-color: rgba(255, 248, 220, 0.95);
    padding: 15px;
    border-radius: 10px;
    text-align:center;
    font-size:18px;
    margin-bottom:20px;
}
.circle-container {
    display:flex;
    justify-content:center;
    margin-top:20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="main-title">🚆 KIRAN ALP CBT-2 PREPARATION TRACKER 🚆</div>', unsafe_allow_html=True)

# ---------- QUOTES ----------
quotes = [
    "Success in Railways starts with daily discipline.",
    "Small daily progress leads to big exam results.",
    "Your effort today decides your rank tomorrow.",
    "Consistency beats intelligence in competitive exams.",
    "Dream ALP uniform? Then study like a champion."
]
st.markdown(f'<div class="quote-box">💡 {random.choice(quotes)}</div>', unsafe_allow_html=True)

# ---------- SYLLABUS ----------
syllabus = {
    "📘 Mathematics": ["Number System","BODMAS","Decimals","Fractions","LCM & HCF",
                       "Ratio and Proportion","Percentages","Mensuration",
                       "Time and Work","Time and Distance",
                       "Simple & Compound Interest","Profit and Loss",
                       "Algebra","Geometry","Trigonometry",
                       "Statistics","Square Root","Age Problems",
                       "Calendar & Clock","Pipes & Cistern"]
}

total_topics = 0
total_done = 0

for section, topics in syllabus.items():
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader(section)

    done = 0
    cols = st.columns(2)

    for i, topic in enumerate(topics):
        if cols[i % 2].checkbox(topic, key=section + topic):
            done += 1

    total_topics += len(topics)
    total_done += done
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- OVERALL CALCULATION ----------
overall = 0
if total_topics > 0:
    overall = int((total_done / total_topics) * 100)

# ---------- ANIMATED CIRCLE ----------
circle_html = f"""
<div class="circle-container">
<svg width="200" height="200">
  <circle cx="100" cy="100" r="80" stroke="#ddd" stroke-width="15" fill="none"/>
  <circle cx="100" cy="100" r="80"
    stroke="#4CAF50"
    stroke-width="15"
    fill="none"
    stroke-dasharray="502"
    stroke-dashoffset="{502 - (502 * overall / 100)}"
    stroke-linecap="round"
    transform="rotate(-90 100 100)"
  />
  <text x="50%" y="50%" text-anchor="middle" dy=".3em"
    font-size="28" fill="white">{overall}%</text>
</svg>
</div>
"""

st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.subheader("📊 Overall Completion")
st.markdown(circle_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- CONFETTI ----------
if overall == 100:
    st.balloons()
    st.success("🎉 Congratulations Mrs Kiran! 100% Completed! 🚆🔥")
