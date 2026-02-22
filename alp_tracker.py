import streamlit as st
import json
import os
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Kiran ALP CBT-2 Preparation", layout="wide")

# ---------- LIGHT BLUE BACKGROUND + STUDY GIRL WATERMARK ----------
st.markdown("""
<style>
body {
    background-color: #e6f2ff;
}
.main {
    background-color: #e6f2ff;
}
.study-bg {
    position: fixed;
    right: 5%;
    bottom: 5%;
    opacity: 0.08;
    width: 400px;
}
.percent-text {
    font-size:28px;
    font-weight:bold;
}
.quote-box {
    text-align:center;
    font-size:28px;
    font-weight:bold;
    color:#6a1b9a;
    margin-top:30px;
    margin-bottom:30px;
}
</style>
""", unsafe_allow_html=True)

# watermark image (royalty free illustration link)
st.markdown("""
<img class="study-bg" src="https://cdn-icons-png.flaticon.com/512/3135/3135755.png">
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1 style='text-align:center;color:#003366;'>KIRAN ALP CBT-2 PREPARATION TRACKER</h1>", unsafe_allow_html=True)

# ---------- MOTIVATION ----------
quotes = [
    "Small progress daily = Big success",
    "Consistency beats talent",
    "Your railway dream is waiting",
    "Discipline creates results",
    "One day or Day One – You decide"
]
st.markdown(f"<div class='quote-box'>{random.choice(quotes)}</div>", unsafe_allow_html=True)

# ---------- SAVE / LOAD PROGRESS ----------
FILE = "progress.json"

def load_progress():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_progress(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

progress = load_progress()

# ---------- SYLLABUS ----------
syllabus = {
    "MATHEMATICS": [
        "Number System","BODMAS","Decimals","Fractions","LCM","HCF",
        "Ratio & Proportion","Percentages","Mensuration","Time & Work",
        "Time & Distance","Simple Interest","Compound Interest",
        "Profit & Loss","Algebra","Geometry","Trigonometry",
        "Elementary Statistics","Square Root","Age Problems",
        "Calendar","Clock","Pipes & Cistern"
    ],
    "REASONING": [
        "Analogies","Alphabetical Series","Number Series",
        "Coding-Decoding","Mathematical Operations","Relationships",
        "Syllogism","Jumbling","Venn Diagram","Data Interpretation",
        "Conclusions","Decision Making","Analytical Reasoning",
        "Classification","Directions","Statement & Arguments"
    ],
    "ENGINEERING SCIENCE": [
        "Engineering Drawing","Units & Measurements","Mass & Density",
        "Work Power Energy","Speed & Velocity","Heat & Temperature",
        "Basic Electricity","Levers & Simple Machines",
        "Occupational Safety","Environment","IT Literacy"
    ],
    "FITTER CORE": [
        "Occupational Safety","Marking Tools","Hand Tools",
        "Measurement Tools","Cutting Tools","Sheet Metal",
        "Brazing","Riveting","Welding","Drilling","Screw Threads",
        "Grinding","Limits & Fits","Lathe Construction",
        "Lathe Accessories","Lathe Tools","Lathe Operations",
        "Preventive Maintenance","Hydraulics","Bearings",
        "Pipes & Fittings","Jigs & Fixtures"
    ]
}

# ---------- SECTION TRACKER ----------
for section, topics in syllabus.items():

    st.markdown(f"## {section}")

    completed = 0

    for topic in topics:
        key = f"{section}_{topic}"
        checked = st.checkbox(topic, value=progress.get(key, False), key=key)
        progress[key] = checked
        if checked:
            completed += 1

    save_progress(progress)

    percent = int((completed / len(topics)) * 100)

    color = "red"
    if percent == 100:
        color = "green"

    st.markdown(f"""
    <div class='percent-text' style='color:{color};'>
    Completed: {percent}% | Pending: {100-percent}%
    </div>
    """, unsafe_allow_html=True)

    if percent == 100:
        st.balloons()

    st.markdown("---")

# ---------- 50 DAY MASTER PLAN ----------
st.markdown("<h2 style='text-align:center;'>50 DAY MASTER STUDY PLAN</h2>", unsafe_allow_html=True)

start_date = datetime.now() + timedelta(days=1)

for day in range(1, 51):

    date = start_date + timedelta(days=day-1)
    st.markdown(f"### Day {day} - {date.strftime('%d %B %Y')}")

    tasks = [
        "Aptitude (6-8 AM)",
        "Mock Test (10-1 PM)",
        "Engineering Science (5-7 PM)",
        "Fitter Core (9PM-12AM)"
    ]

    completed = 0
    cols = st.columns(4)

    for i in range(4):
        key = f"day_{day}_{i}"
        checked = cols[i].checkbox(tasks[i], value=progress.get(key, False), key=key)
        progress[key] = checked
        if checked:
            completed += 1

    save_progress(progress)

    percent = int((completed / 4) * 100)

    circle_color = "#ff4d4d"
    if percent == 100:
        circle_color = "#00cc44"

    st.markdown(f"""
    <div style="display:flex;justify-content:center;margin:20px;">
        <div style="
            width:140px;
            height:140px;
            border-radius:50%;
            background:conic-gradient(
                {circle_color} {percent*3.6}deg,
                #ffcccc {percent*3.6}deg
            );
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:24px;
            font-weight:bold;
            color:black;
        ">
        {percent}%
        </div>
    </div>
    """, unsafe_allow_html=True)

    if percent == 100:
        st.success(f"Day {day} Fully Completed!")
        st.balloons()

    st.markdown("---")
