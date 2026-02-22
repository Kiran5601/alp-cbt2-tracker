import streamlit as st
import json
import os
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="KIRAN ALP MASTER DASHBOARD", layout="wide")

# ---------------- SAVE SYSTEM ----------------
SAVE_FILE = "master_progress.json"

def load_progress():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_progress(data):
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

progress_data = load_progress()

# ---------------- STYLE ----------------
st.markdown("""
<style>
.stApp { background-color: #eef6ff; }

.main-title {
    text-align:center;
    font-size:48px;
    font-weight:900;
    background: linear-gradient(90deg,#1565c0,#8e24aa);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.section-box {
    background:white;
    padding:25px;
    border-radius:15px;
    margin-bottom:30px;
    box-shadow:0px 6px 15px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">KIRAN ALP CBT-2 MASTER TRACKER</div>', unsafe_allow_html=True)

# ---------------- ANIMATED CIRCLE ----------------
def animated_circle(percent):
    color = "#2e7d32" if percent >= 80 else "#f9a825" if percent >= 50 else "#c62828"

    circle_html = f"""
    <div style="display:flex;justify-content:center;">
    <svg width="180" height="180">
        <circle cx="90" cy="90" r="75" stroke="#eee" stroke-width="18" fill="none"/>
        <circle cx="90" cy="90" r="75"
            stroke="{color}"
            stroke-width="18"
            fill="none"
            stroke-dasharray="471"
            stroke-dashoffset="{471 - (471 * percent / 100)}"
            transform="rotate(-90 90 90)"
            style="transition: stroke-dashoffset 1.2s ease-out;"
        />
        <text x="50%" y="50%" text-anchor="middle"
            font-size="32" font-weight="900" fill="{color}">
            {percent}%
        </text>
    </svg>
    </div>
    """
    st.markdown(circle_html, unsafe_allow_html=True)

# ======================================================
# ================== FULL SYLLABUS =====================
# ======================================================

st.header("📘 FULL SYLLABUS TRACKER")

syllabus = {
"ARITHMETIC": ["Number System","BODMAS","Percentages","Time & Work"],
"REASONING": ["Analogies","Coding-Decoding","Syllogism","Directions"],
"ENGINEERING SCIENCE": ["Units","Heat","Electricity","Drawing"],
"FITTER CORE": ["Welding","Lathe","Grinding","Bearings"]
}

total_topics = 0
total_done = 0

for section, topics in syllabus.items():

    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader(section)

    done = 0

    for topic in topics:
        key = section + "_" + topic
        default = progress_data.get(key, False)

        if not default:
            checked = st.checkbox(topic, value=False, key=key)

            if checked:
                progress_data[key] = True
                st.balloons()   # POP ANIMATION
        else:
            st.markdown(
                f"""
                <div style="display:flex;align-items:center;">
                    <div style="
                        width:35px;
                        height:35px;
                        border-radius:50%;
                        background-color:#2e7d32;
                        color:white;
                        display:flex;
                        justify-content:center;
                        align-items:center;
                        font-weight:bold;
                        margin-right:10px;">
                        ✓
                    </div>
                    <span style="font-weight:600;">{topic}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

        if progress_data.get(key, False):
            done += 1

    total_topics += len(topics)
    total_done += done

    percent = int((done / len(topics)) * 100)
    animated_circle(percent)

    st.markdown('</div>', unsafe_allow_html=True)

# ======================================================
# ================= OVERALL ============================
# ======================================================

save_progress(progress_data)

overall_percent = int((total_done / total_topics) * 100)

st.header("🏆 OVERALL PROGRESS")
animated_circle(overall_percent)

if overall_percent == 100:
    st.balloons()
    st.success("🎉 COMPLETE SYLLABUS DONE!")
