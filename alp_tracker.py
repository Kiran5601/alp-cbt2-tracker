import streamlit as st
import json
import os
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Kiran ALP CBT-2 Preparation", layout="wide")

# ---------------- BACKGROUND ----------------
st.markdown("""
<style>
body { background-color: #e6f2ff; }
.big-title { 
    text-align:center; 
    font-size:42px; 
    font-weight:bold; 
    color:#0d47a1; 
}
.quote {
    text-align:center;
    font-size:26px;
    color:#6a1b9a;
    margin-top:20px;
    margin-bottom:30px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='big-title'>KIRAN ALP CBT-2 PREPARATION TRACKER</div>", unsafe_allow_html=True)

quotes = [
    "Small progress daily = Big success",
    "Consistency beats talent",
    "50 Days Discipline = Railway Job",
    "Stay Focused. Stay Strong.",
    "Your Hard Work Will Pay Off"
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

# ---------------- 50 DAY MASTER PLAN ----------------
st.markdown("## 50 DAY MASTER STUDY PLAN")

start_date = datetime.now() + timedelta(days=1)

total_tasks = 50 * 4
completed_tasks = 0

for day in range(1, 51):

    date = start_date + timedelta(days=day-1)

    st.markdown(f"### Day {day} - {date.strftime('%d %B %Y')}")

    col1, col2, col3, col4 = st.columns(4)

    sessions = [
        ("Aptitude (6-8 AM)", "Mathematics + Reasoning Topics"),
        ("Mock Test (10-1 PM)", "Full Length Practice"),
        ("Engineering Science (5-7 PM)", "Physics + Basic Engineering"),
        ("Fitter Core (9PM-12AM)", "Trade Theory + Workshop")
    ]

    for i, col in enumerate([col1, col2, col3, col4]):
        key = f"day_{day}_{i}"
        checked = col.checkbox(sessions[i][0], value=progress.get(key, False), key=key)
        col.caption(sessions[i][1])

        progress[key] = checked

        if checked:
            completed_tasks += 1

    st.markdown("---")

save_data(progress)

# ---------------- OVERALL 50 DAY PERCENTAGE ----------------

overall_percent = int((completed_tasks / total_tasks) * 100)

circle_color = "#ff4d4d"
if overall_percent == 100:
    circle_color = "#00cc44"

st.markdown("## Overall 50 Day Completion")

st.markdown(f"""
<div style="display:flex;justify-content:center;margin:30px;">
    <div style="
        width:220px;
        height:220px;
        border-radius:50%;
        background:conic-gradient(
            {circle_color} {overall_percent*3.6}deg,
            #ffcccc {overall_percent*3.6}deg
        );
        display:flex;
        align-items:center;
        justify-content:center;
        font-size:40px;
        font-weight:bold;
        color:black;
    ">
    {overall_percent}%
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align:center;font-size:22px;">
Completed: {completed_tasks} / {total_tasks} Tasks
</div>
""", unsafe_allow_html=True)

if overall_percent == 100:
    st.success("🎉 50 DAY MASTER PLAN COMPLETED SUCCESSFULLY!")
    st.balloons()
