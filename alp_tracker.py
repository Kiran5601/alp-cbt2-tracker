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
    background: linear-gradient(rgba(230,242,255,0.9), rgba(230,242,255,0.9)),
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
    font-size:20px;
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

# ---------------- FULL SYLLABUS ----------------
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
    completed = percent
    pending = 100 - percent

    color = "#00cc44" if percent == 100 else "#ff4d4d"
    deg = percent * 3.6

    st.markdown(f"""
    <div style="display:flex;justify-content:center;">
        <div style="
            width:110px;
            height:110px;
            border-radius:50%;
            background: conic-gradient({color} {deg}deg, #ffd6d6 {deg}deg);
            display:flex;
            align-items:center;
            justify-content:center;
        ">
            <div style="
                width:75px;
                height:75px;
                border-radius:50%;
                background:white;
                display:flex;
                align-items:center;
                justify-content:center;
                flex-direction:column;
                font-size:14px;
                font-weight:bold;
            ">
                {completed}%<br>
                <span style='color:red;font-size:12px'>P {pending}%</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- DAY SYSTEM ----------------
st.header("📅 50 DAY MASTER STUDY PLAN")

start_date = datetime.now() + timedelta(days=1)

for day in range(1, 51):

    date = (start_date + timedelta(days=day-1)).strftime("%d %B %Y")
    st.markdown(f"### Day {day} - {date}")

    col1, col2, col3, col4 = st.columns(4)

    sections = [
        ("Aptitude", aptitude_topics[(day-1) % len(aptitude_topics)]),
        ("Reasoning", reasoning_topics[(day-1) % len(reasoning_topics)]),
        ("Engineering Science", engineering_topics[(day-1) % len(engineering_topics)]),
        ("Fitter Core", fitter_topics[(day-1) % len(fitter_topics)])
    ]

    for i, col in enumerate([col1, col2, col3, col4]):
        section_name, topic = sections[i]
        key = f"day_{day}_{i}"

        col.markdown(f"<div class='section-title'>{section_name}<br>(Topic: {topic})</div>", unsafe_allow_html=True)

        checked = col.checkbox("Completed", value=progress.get(key, False), key=key)
        progress[key] = checked

        percent = 100 if checked else 0

        with col:
            draw_circle(percent)

    st.markdown("---")

save_data(progress)

# ---------------- FULL SYLLABUS COMPLETION ----------------
total = 50 * 4
done = sum(progress.values())

overall = int((done / total) * 100)

st.header("📊 Overall 50 Days Completion")

draw_circle(overall)

if overall == 100:
    st.balloons()
    st.success("🎉 MASTER PLAN COMPLETED SUCCESSFULLY!")
