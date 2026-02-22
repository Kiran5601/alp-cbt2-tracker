import streamlit as st
import json
import os
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="KIRAN ALP CBT-2 PREPARATION TRACKER", layout="wide")

# ------------------ LIGHT BLUE BACKGROUND + WATERMARK ------------------

st.markdown("""
<style>
.stApp {
    background-color: #dff2ff;
    background-image: url("https://cdn-icons-png.flaticon.com/512/3135/3135715.png");
    background-repeat: no-repeat;
    background-position: center;
    background-size: 400px;
    background-attachment: fixed;
    background-blend-mode: lighten;
}
.big-title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #003366;
}
.quote-box {
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    color: #5c0080;
    padding: 25px;
}
.percent-text {
    text-align: center;
    font-size: 30px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADING ------------------

st.markdown('<div class="big-title">KIRAN ALP CBT-2 PREPARATION TRACKER</div>', unsafe_allow_html=True)

# ------------------ QUOTES ------------------

quotes = [
    "Success doesn’t come from what you do occasionally.",
    "Discipline is choosing between what you want now and what you want most.",
    "Small daily progress leads to big success.",
    "Your hard work will pay off.",
]

st.markdown(f'<div class="quote-box">{random.choice(quotes)}</div>', unsafe_allow_html=True)

# ------------------ SYLLABUS ------------------

syllabus = {
    "Arithmetic": [
        "Number System","BODMAS","Decimals","Fractions","LCM & HCF",
        "Ratio & Proportion","Percentages","Mensuration","Time & Work",
        "Time & Distance","Simple Interest","Compound Interest",
        "Profit & Loss","Algebra","Geometry","Trigonometry",
        "Statistics","Square Root","Age","Calendar & Clock","Pipes & Cistern"
    ],
    "Reasoning": [
        "Analogies","Alphabet Series","Number Series","Coding Decoding",
        "Mathematical Operations","Relationships","Syllogism",
        "Jumbling","Venn Diagram","Data Interpretation",
        "Decision Making","Analytical Reasoning","Classification",
        "Directions","Statement & Arguments"
    ],
    "Engineering Science": [
        "Engineering Drawing","Units & Measurements",
        "Mass Weight Density","Work Power Energy",
        "Speed Velocity","Heat Temperature",
        "Basic Electricity","Levers","Simple Machines",
        "Occupational Safety","Environment","IT Literacy"
    ],
    "Fitter Core": [
        "Occupational Safety","Marking Tools","Metals",
        "Hand Tools","Measuring Tools","Cutting Tools",
        "Sheet Metal","Brazing","Riveting","Welding",
        "Drilling","Threads","Grinding","Limits & Fits",
        "Lathe Construction","Lathe Accessories",
        "Lathe Tools","Lathe Operations","Maintenance"
    ]
}

# ------------------ SAVE DATA ------------------

DATA_FILE = "progress.json"

def load_progress():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_progress(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

progress = load_progress()

# ------------------ DISPLAY CHECKLIST ------------------

total_topics = 0
completed_topics = 0

for section, topics in syllabus.items():
    st.subheader(section)
    for topic in topics:
        key = f"{section}_{topic}"
        checked = st.checkbox(topic, value=progress.get(key, False), key=key)
        progress[key] = checked
        total_topics += 1
        if checked:
            completed_topics += 1

save_progress(progress)

# ------------------ PERCENTAGE CALCULATION ------------------

percentage = int((completed_topics / total_topics) * 100)
pending = 100 - percentage

# ------------------ ANIMATED PROGRESS ------------------

progress_bar = st.progress(0)

for i in range(percentage + 1):
    progress_bar.progress(i)

if percentage == 100:
    st.balloons()
    st.success("🎉 FULL SYLLABUS COMPLETED! 🎉")

# ------------------ PERCENT DISPLAY ------------------

if percentage < 100:
    st.markdown(
        f'<div class="percent-text" style="color:red;">Completed: {percentage}% | Pending: {pending}%</div>',
        unsafe_allow_html=True
    )
else:
    st.markdown(
        f'<div class="percent-text" style="color:green;">Completed: 100% | Pending: 0%</div>',
        unsafe_allow_html=True
    )

# ------------------ 50 DAY MASTER PLAN ------------------

st.markdown("## 50 DAY MASTER STUDY PLAN")

start_date = datetime.now() + timedelta(days=1)

for day in range(1, 51):
    date = start_date + timedelta(days=day-1)
    st.markdown(f"### Day {day} - {date.strftime('%d %B %Y')}")

    col1, col2, col3, col4 = st.columns(4)

    tasks = [
        "Aptitude (6-8 AM)",
        "Mock Test (10-1 PM)",
        "Engineering Science (5-7 PM)",
        "Fitter Core (9PM-12AM)"
    ]

    day_completed = 0

    for i in range(4):
        task_key = f"day{day}_{i}"
        checked = col1.checkbox(tasks[i] if i==0 else "", value=progress.get(task_key, False), key=task_key)
        progress[task_key] = checked
        if checked:
            day_completed += 1

    circle_percent = int((day_completed/4)*100)

    if circle_percent == 100:
        color = "green"
    else:
        color = "red"

    st.markdown(
        f'<div style="text-align:center; font-size:20px; font-weight:bold; color:{color};">'
        f"Day {day} Completion: {circle_percent}%</div>",
        unsafe_allow_html=True
    )

save_progress(progress)
