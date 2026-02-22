import streamlit as st
import random
import json
import os
import time

st.set_page_config(page_title="KIRAN ALP CBT-2 PREPARATION TRACKER", layout="wide")

# ---------------- SAVE FILE ----------------
SAVE_FILE = "progress.json"

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
.stApp { background-color: #eaf4ff; }

.stApp::before {
    content: "";
    background-image: url("https://img.freepik.com/free-vector/student-studying-desk_23-2148880412.jpg");
    background-repeat: no-repeat;
    background-position: center 70%;
    background-size: 600px;
    opacity: 0.05;
    position: fixed;
    width: 100%;
    height: 100%;
    z-index: -1;
}

.main-title {
    text-align:center;
    font-size:48px;
    font-weight:900;
    background: linear-gradient(90deg,#1565c0,#8e24aa);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.quote-box {
    text-align:center;
    font-size:24px;
    font-weight:600;
    margin-top:40px;
    margin-bottom:60px;
    color:#6a1b9a;
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

# ---------------- TITLE ----------------
st.markdown('<div class="main-title">KIRAN ALP CBT-2 PREPARATION TRACKER</div>', unsafe_allow_html=True)

quotes = [
"Small daily progress leads to big success.",
"Discipline today, selection tomorrow.",
"Consistency beats talent.",
"Stay focused. You are closer than you think."
]

st.markdown(f'<div class="quote-box">💡 {random.choice(quotes)}</div>', unsafe_allow_html=True)

# ---------------- ANIMATED PROGRESS BAR ----------------
def animated_progress_bar(percent):
    progress_placeholder = st.empty()
    for i in range(percent + 1):
        progress_placeholder.progress(i / 100)
        time.sleep(0.01)

# ---------------- ANIMATED CIRCLE ----------------
def animated_circle(percent):
    circle_html = f"""
    <div style="display:flex;justify-content:center;">
    <svg width="150" height="150">
        <circle cx="75" cy="75" r="65" stroke="#d0e3ff" stroke-width="12" fill="none"/>
        <circle cx="75" cy="75" r="65"
            stroke="#1565c0"
            stroke-width="12"
            fill="none"
            stroke-dasharray="408"
            stroke-dashoffset="{408 - (408 * percent / 100)}"
            style="transition: stroke-dashoffset 1.2s ease-out;"/>
        <text x="50%" y="50%" text-anchor="middle" dy=".3em"
            font-size="24" font-weight="bold" fill="#000">
            {percent}%
        </text>
    </svg>
    </div>
    """
    st.markdown(circle_html, unsafe_allow_html=True)

# ---------------- SYLLABUS ----------------
syllabus = {
"ARITHMETIC": ["Number System","BODMAS","Decimals","Fractions","LCM","HCF",
"Ratio & Proportion","Percentages","Mensuration","Time & Work",
"Time & Distance","Simple Interest","Compound Interest",
"Profit & Loss","Algebra","Geometry","Trigonometry",
"Elementary Statistics","Square Root","Age Problems",
"Calendar","Clock","Pipes & Cistern"],

"REASONING": ["Analogies","Alphabetical Series","Number Series",
"Coding-Decoding","Mathematical Operations","Relationships",
"Syllogism","Jumbling","Venn Diagram","Data Interpretation",
"Data Sufficiency","Conclusions","Decision Making",
"Similarities & Differences","Analytical Reasoning",
"Classification","Directions","Statement-Arguments","Assumptions"],

"ENGINEERING SCIENCE": ["Engineering Drawing","Views","Drawing Instruments",
"Lines","Geometric Figures","Units & Measurements",
"Mass Weight Density","Work Power Energy",
"Speed & Velocity","Heat & Temperature",
"Basic Electricity","Levers","Occupational Safety",
"Environment","IT Literacy"],

"TRADE THEORY 1st YEAR": ["Introduction","Safety","Marking Tools","Metals",
"Hand Tools","Measuring Tools","Cutting Tools",
"Sheet Metal","Welding","Lathe Construction",
"Lathe Tools","Lathe Operations"],

"TRADE THEORY 2nd YEAR": ["Fasteners","Gauges","Metrology",
"Heat Treatment","Bearings","Pipe Fittings",
"Jigs & Fixtures","Hydraulics","Lubricants"]
}

total_topics = 0
total_done = 0

# ---------------- DISPLAY ----------------
for section, topics in syllabus.items():

    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader(section)

    done = 0

    for topic in topics:
        key = section + "_" + topic
        default_value = progress_data.get(key, False)
        checked = st.checkbox(topic, value=default_value, key=key)
        progress_data[key] = checked

        if checked:
            done += 1

    total_topics += len(topics)
    total_done += done

    percent = int((done / len(topics)) * 100)
    pending = 100 - percent

    animated_progress_bar(percent)
    animated_circle(percent)

    st.write(f"Completed: {percent}% | Pending: {pending}%")

    st.markdown('</div>', unsafe_allow_html=True)

save_progress(progress_data)

# ---------------- OVERALL ----------------
overall = int((total_done / total_topics) * 100)
overall_pending = 100 - overall

st.subheader("Overall Completion")
animated_progress_bar(overall)
animated_circle(overall)

st.write(f"Overall Completed: {overall}% | Pending: {overall_pending}%")

if overall == 100:
    st.balloons()
    st.success("🎉 Congratulations! Full Syllabus Completed!")
