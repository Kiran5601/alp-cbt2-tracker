import streamlit as st
import json
import os
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Kiran ALP CBT-2 Preparation", layout="wide")

# ------------------- STYLING -------------------

st.markdown("""
<style>
body { background-color: #e6f2ff; }

.main-title {
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#0d47a1;
}

.quote {
    text-align:center;
    font-size:24px;
    color:#6a1b9a;
    margin-top:20px;
    margin-bottom:30px;
}

.circle-container {
    display:flex;
    justify-content:center;
    margin-top:10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>KIRAN ALP CBT-2 PREPARATION TRACKER</div>", unsafe_allow_html=True)

quotes = [
    "Small daily progress leads to big success.",
    "Consistency builds railway rank.",
    "50 Days. One Goal.",
    "Discipline = Success.",
    "Focus like a topper."
]

st.markdown(f"<div class='quote'>{random.choice(quotes)}</div>", unsafe_allow_html=True)

# ------------------- SAVE SYSTEM -------------------

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

# ------------------- TOPIC LISTS -------------------

aptitude_topics = [
    "Number System","LCM & HCF","Ratio & Proportion","Percentages",
    "Ages","Time & Work","Time & Distance","Simple Interest",
    "Compound Interest","Profit & Loss","Algebra","Geometry",
    "Trigonometry","Statistics","Calendar & Clock"
]

engg_topics = [
    "Units","Mass & Density","Work Power Energy","Speed & Velocity",
    "Heat","Basic Electricity","Levers","Simple Machines",
    "Safety","Environment","IT Literacy"
]

fitter_topics = [
    "Marking Tools","Hand Tools","Measuring Tools","Cutting Tools",
    "Sheet Metal","Welding","Drilling","Grinding",
    "Lathe Construction","Lathe Operations"
]

# ------------------- CIRCLE FUNCTION -------------------

def draw_circle(percent, size=120):
    color = "#ff4d4d"
    if percent == 100:
        color = "#00cc44"

    st.markdown(f"""
    <div class="circle-container">
        <div style="
            width:{size}px;
            height:{size}px;
            border-radius:50%;
            background:conic-gradient(
                {color} {percent*3.6}deg,
                #ffcccc {percent*3.6}deg
            );
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:22px;
            font-weight:bold;
            color:black;
        ">
            {percent}%
        </div>
    </div>
    """, unsafe_allow_html=True)

# ------------------- 50 DAY PLAN -------------------

st.markdown("## 50 DAY MASTER STUDY PLAN")

start_date = datetime.now() + timedelta(days=1)

total_completed = 0
total_tasks = 50 * 4

for day in range(1, 51):

    date = start_date + timedelta(days=day-1)

    st.markdown(f"### Day {day} - {date.strftime('%d %B %Y')}")

    col1, col2, col3, col4 = st.columns(4)

    apt_topic = aptitude_topics[(day-1) % len(aptitude_topics)]
    eng_topic = engg_topics[(day-1) % len(engg_topics)]
    fit_topic = fitter_topics[(day-1) % len(fitter_topics)]

    sessions = [
        f"Aptitude (Topic: {apt_topic})",
        f"Mock Test (Topic: Practice)",
        f"Engineering Science (Topic: {eng_topic})",
        f"Fitter Core (Topic: {fit_topic})"
    ]

    day_completed = 0

    for i, col in enumerate([col1, col2, col3, col4]):
        key = f"day_{day}_{i}"
        checked = col.checkbox(sessions[i], value=progress.get(key, False), key=key)
        progress[key] = checked

        percent = 100 if checked else 0
        col.markdown("<br>", unsafe_allow_html=True)
        col.markdown("Progress:")
        draw_circle(percent, size=90)

        if checked:
            day_completed += 1
            total_completed += 1

    save_data(progress)

    day_percent = int((day_completed / 4) * 100)

    st.markdown("#### Daily Overall Progress")
    draw_circle(day_percent, size=140)

    if day_percent == 100:
        st.success(f"Day {day} Fully Completed!")

    st.markdown("---")

# ------------------- FINAL OVERALL PROGRESS -------------------

overall_percent = int((total_completed / total_tasks) * 100)

st.markdown("## 🚀 COMPLETE SYLLABUS PROGRESS")
draw_circle(overall_percent, size=200)

if overall_percent == 100:
    st.balloons()
    st.success("🎉 Entire 50-Day Syllabus Completed!")
