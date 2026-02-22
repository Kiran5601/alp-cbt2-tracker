import streamlit as st
import json
import os
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Kiran ALP CBT-2 Preparation", layout="wide")

# ---------------- STYLE ----------------

st.markdown("""
<style>
body {
    background-color:#e6f2ff;
}

.main-title {
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#0d47a1;
    margin-bottom:15px;
}

.quote {
    text-align:center;
    font-size:22px;
    color:#6a1b9a;
    margin-bottom:30px;
}

.section-box {
    text-align:center;
    font-size:20px;
    font-weight:bold;
}

.circle {
    width:130px;
    height:130px;
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:22px;
    font-weight:bold;
    margin:auto;
    color:black;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown("<div class='main-title'>KIRAN ALP CBT-2 PREPARATION TRACKER</div>", unsafe_allow_html=True)

quotes = [
    "Small daily progress leads to big success.",
    "Consistency builds rank.",
    "Focus 50 Days = Secure Job.",
    "Discipline creates Railway Officer."
]

st.markdown(f"<div class='quote'>{random.choice(quotes)}</div>", unsafe_allow_html=True)

# ---------------- SAVE SYSTEM ----------------

FILE = "progress.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

progress = load_data()

# ---------------- TOPICS ----------------

aptitude_topics = ["Number System","Ages","Percentages","Time & Work","Ratio","Profit & Loss"]
engg_topics = ["Units","Work Power Energy","Heat","Basic Electricity","Safety"]
fitter_topics = ["Marking Tools","Measuring Tools","Cutting Tools","Welding","Lathe Operations"]

# ---------------- CIRCLE FUNCTION ----------------

def draw_circle(percent):
    color = "#ff4d4d"
    if percent == 100:
        color = "#00cc44"

    deg = percent * 3.6

    st.markdown(f"""
    <div style="display:flex;justify-content:center;">
        <div class="circle" style="
            background: conic-gradient(
                {color} {deg}deg,
                #ffcccc {deg}deg
            );
        ">
            {percent}%
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- DAY SYSTEM ----------------

start_date = datetime.now() + timedelta(days=1)
day = 1
date = start_date.strftime("%d %B %Y")

st.markdown(f"## Day {day} - {date}")

# ---------------- 4 SECTIONS HORIZONTAL ----------------

col1, col2, col3, col4 = st.columns(4)

sections = [
    ("Aptitude", aptitude_topics[0]),
    ("Mock Test", "Practice"),
    ("Engineering Science", engg_topics[0]),
    ("Fitter Core", fitter_topics[0])
]

for idx, col in enumerate([col1, col2, col3, col4]):
    section_name, topic = sections[idx]
    key = f"day_{day}_{idx}"

    col.markdown(f"<div class='section-box'>{section_name}<br>(Topic: {topic})</div>", unsafe_allow_html=True)

    checked = col.checkbox("Completed", value=progress.get(key, False), key=key)
    progress[key] = checked

    percent = 100 if checked else 0

    col.markdown("##### Progress")
    with col:
        draw_circle(percent)

save_data(progress)

# Celebration
if all(progress.get(f"day_{day}_{i}", False) for i in range(4)):
    st.balloons()
    st.success("🎉 All Sections Completed for Today!")
