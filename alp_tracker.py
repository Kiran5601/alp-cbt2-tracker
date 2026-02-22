import streamlit as st
import json
import os
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Kiran ALP CBT-2 Preparation", layout="wide")

# ---------------- BACKGROUND ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(rgba(230,242,255,0.92), rgba(230,242,255,0.92)),
    url("https://images.unsplash.com/photo-1509062522246-3755977927d7");
    background-size: cover;
    background-position: center;
}

.main-title {
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#0d47a1;
    margin-bottom:10px;
}

.quote {
    text-align:center;
    font-size:22px;
    color:#6a1b9a;
    margin-bottom:25px;
}

.section-title {
    text-align:center;
    font-size:18px;
    font-weight:bold;
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
aptitude_topics = [
    "Number System","BODMAS","Decimals","Fractions","LCM & HCF",
    "Ratio & Proportion","Percentages","Time & Work",
    "Time & Distance","Profit & Loss","Simple Interest",
    "Compound Interest","Algebra","Geometry","Trigonometry",
    "Statistics","Square Root","Ages","Calendar","Pipes"
]

reasoning_topics = [
    "Analogies","Series","Coding-Decoding","Mathematical Operations",
    "Relationships","Syllogism","Jumbling","Venn Diagram",
    "Data Interpretation","Decision Making","Classification",
    "Directions","Statement & Conclusion"
]

engineering_topics = [
    "Units","Measurements","Mass & Density","Work Power Energy",
    "Speed & Velocity","Heat","Basic Electricity",
    "Levers","Simple Machines","Safety","IT Literacy"
]

fitter_topics = [
    "Marking Tools","Measuring Tools","Cutting Tools","Sheet Metal",
    "Brazing","Riveting","Welding","Drilling",
    "Grinding","Limits & Fits","Lathe","Maintenance"
]

# ---------------- CIRCLE FUNCTION ----------------
def draw_circle(percent):
    color = "#00cc44" if percent == 100 else "#ff4d4d"
    deg = percent * 3.6
    pending = 100 - percent

    st.markdown(f"""
    <div style="display:flex;justify-content:center;">
        <div style="
            width:120px;
            height:120px;
            border-radius:50%;
            background: conic-gradient({color} {deg}deg, #ffd6d6 {deg}deg);
            display:flex;
            align-items:center;
            justify-content:center;
        ">
            <div style="
                width:80px;
                height:80px;
                border-radius:50%;
                background:white;
                display:flex;
                align-items:center;
                justify-content:center;
                flex-direction:column;
                font-size:14px;
                font-weight:bold;
            ">
                {percent}%<br>
                <span style='color:red;font-size:12px'>P {pending}%</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- 50 DAY PLAN ----------------
st.markdown("<h2 style='text-align:center;'>📅 50 DAY MASTER STUDY PLAN</h2>", unsafe_allow_html=True)

start_date = datetime.now() + timedelta(days=1)

subject_done = {"apt":0, "res":0, "eng":0, "fit":0}

for day in range(1, 51):

    date = (start_date + timedelta(days=day-1)).strftime("%d %B %Y")
    st.markdown(f"<h4 style='text-align:center;'>Day {day} - {date}</h4>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    sections = [
        ("apt","Aptitude", aptitude_topics[(day-1) % len(aptitude_topics)]),
        ("res","Reasoning", reasoning_topics[(day-1) % len(reasoning_topics)]),
        ("eng","Engineering Science", engineering_topics[(day-1) % len(engineering_topics)]),
        ("fit","Fitter Core", fitter_topics[(day-1) % len(fitter_topics)])
    ]

    for i, col in enumerate([col1,col2,col3,col4]):
        prefix, name, topic = sections[i]
        key = f"day_{day}_{prefix}"

        col.markdown(f"<div class='section-title'>{name}<br>(Topic: {topic})</div>", unsafe_allow_html=True)

        checked = col.checkbox("Completed", value=progress.get(key, False), key=key)
        progress[key] = checked

        if checked:
            subject_done[prefix] += 1

    st.markdown("---")

save_data(progress)

# ---------------- CUMULATIVE CALCULATION ----------------

total_days = 50

apt_percent = int((subject_done["apt"] / total_days) * 100)
res_percent = int((subject_done["res"] / total_days) * 100)
eng_percent = int((subject_done["eng"] / total_days) * 100)
fit_percent = int((subject_done["fit"] / total_days) * 100)

# ---------------- SUBJECT CIRCLES ----------------
st.markdown("<h2 style='text-align:center;'>📊 Subject Wise Cumulative Completion</h2>", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("<h4 style='text-align:center;'>Aptitude</h4>", unsafe_allow_html=True)
    draw_circle(apt_percent)

with c2:
    st.markdown("<h4 style='text-align:center;'>Reasoning</h4>", unsafe_allow_html=True)
    draw_circle(res_percent)

with c3:
    st.markdown("<h4 style='text-align:center;'>Engineering Science</h4>", unsafe_allow_html=True)
    draw_circle(eng_percent)

with c4:
    st.markdown("<h4 style='text-align:center;'>Fitter Core</h4>", unsafe_allow_html=True)
    draw_circle(fit_percent)

# ---------------- OVERALL ----------------
total_done = subject_done["apt"] + subject_done["res"] + subject_done["eng"] + subject_done["fit"]
total_possible = 50 * 4

overall = int((total_done / total_possible) * 100)

st.markdown("<h2 style='text-align:center;'>📊 Overall 50 Days Completion</h2>", unsafe_allow_html=True)
draw_circle(overall)

if overall == 100:
    st.balloons()
    st.success("🎉 MASTER PLAN COMPLETED SUCCESSFULLY!")
