import streamlit as st
import json
import os
from datetime import datetime, timedelta

st.set_page_config(page_title="Kiran ALP CBT-2 Preparation", layout="wide")

# ---------------- BACKGROUND ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(rgba(230,242,255,0.95), rgba(230,242,255,0.95));
}

.main-title {
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#0d47a1;
}

.sub-title {
    text-align:center;
    font-size:28px;
    font-weight:bold;
}

.section-title {
    text-align:center;
    font-size:18px;
    font-weight:bold;
}

.green-box {
    background-color:#00cc44;
    color:white;
    padding:6px;
    border-radius:6px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='main-title'>KIRAN ALP CBT-2 PREPARATION TRACKER</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>📅 51 DAY MASTER STUDY PLAN</div>", unsafe_allow_html=True)
st.markdown("---")

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

# ---------------- ARITHMETIC TOPICS (AS GIVEN) ----------------
aptitude_topics = (
["Number System"]*3 +
["Simplification"]*2 +
["Percentage"]*2 +
["Ratio & Proportion"]*2 +
["Ages"]*1 +
["Profit & Loss"]*3 +
["Simple Interest"]*2 +
["Compound Interest"]*2 +
["Time & Work"]*2 +
["Time Speed Distance"]*2 +
["Algebra"]*2 +
["Geometry"]*5 +
["Mensuration 3D"]*2 +
["Statistics"]*1 +
["Calendar"]*2 +
["Clock"]*2 +
["Trigonometry"]*3
)

# Make total 51 days
while len(aptitude_topics) < 51:
    aptitude_topics.append("Revision / Practice")

# Dummy Other Sections (You can modify later)
engineering_topics = ["Units","Heat","Electricity","Measurements","Safety"] * 11
fitter_topics = ["Marking","Measuring","Welding","Lathe","Drilling"] * 11
daily_test_topics = ["Mock Test"] * 51

# ---------------- CIRCLE FUNCTION ----------------
def draw_circle(percent):
    color = "#00cc44" if percent == 100 else "#ff4d4d"
    deg = percent * 3.6
    pending = 100 - percent

    st.markdown(f"""
    <div style="display:flex;justify-content:center;margin-top:10px;">
        <div style="
            width:100px;
            height:100px;
            border-radius:50%;
            background: conic-gradient({color} {deg}deg, #ffd6d6 {deg}deg);
            display:flex;
            align-items:center;
            justify-content:center;
        ">
            <div style="
                width:70px;
                height:70px;
                border-radius:50%;
                background:white;
                display:flex;
                align-items:center;
                justify-content:center;
                flex-direction:column;
                font-size:13px;
                font-weight:bold;
            ">
                {percent}%<br>
                <span style='color:red;font-size:11px'>P {pending}%</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- DAY LOOP ----------------
start_date = datetime.now() + timedelta(days=1)

total_topics = 51 * 4

for day in range(1, 52):

    date = (start_date + timedelta(days=day-1)).strftime("%d %B %Y")
    st.markdown(f"### Day {day} - {date}")

    col1, col2, col3, col4 = st.columns(4)

    sections = [
        ("Aptitude", aptitude_topics[day-1]),
        ("Daily Test", daily_test_topics[day-1]),
        ("Engineering Science", engineering_topics[day-1]),
        ("Fitter Core", fitter_topics[day-1])
    ]

    for i, col in enumerate([col1, col2, col3, col4]):
        section_name, topic = sections[i]
        key = f"day_{day}_{i}"

        col.markdown(f"<div class='section-title'>{section_name}<br>(Topic: {topic})</div>", unsafe_allow_html=True)

        checked = col.checkbox("Completed", value=progress.get(key, False), key=key)
        progress[key] = checked

        if checked:
            col.markdown("<div class='green-box'>Completed</div>", unsafe_allow_html=True)

    st.markdown("---")

save_data(progress)

# ---------------- CUMULATIVE CALCULATION ----------------
done = sum(progress.values())
overall_percent = int((done / total_topics) * 100)

st.markdown("<div class='sub-title'>📊 Cumulative Subject Wise Completion</div>", unsafe_allow_html=True)

colA, colB, colC, colD = st.columns(4)

# Calculate subject wise cumulative
def subject_percent(index):
    count = 0
    for day in range(1,52):
        if progress.get(f"day_{day}_{index}", False):
            count += 1
    return int((count / 51) * 100)

with colA:
    st.markdown("<div class='section-title'>Aptitude</div>", unsafe_allow_html=True)
    draw_circle(subject_percent(0))

with colB:
    st.markdown("<div class='section-title'>Daily Test</div>", unsafe_allow_html=True)
    draw_circle(subject_percent(1))

with colC:
    st.markdown("<div class='section-title'>Engineering Science</div>", unsafe_allow_html=True)
    draw_circle(subject_percent(2))

with colD:
    st.markdown("<div class='section-title'>Fitter Core</div>", unsafe_allow_html=True)
    draw_circle(subject_percent(3))

st.markdown("---")
st.markdown("<div class='sub-title'>📊 Overall 51 Days Completion</div>", unsafe_allow_html=True)
draw_circle(overall_percent)

if overall_percent == 100:
    st.balloons()
    st.success("🎉 MASTER PLAN COMPLETED SUCCESSFULLY!")
