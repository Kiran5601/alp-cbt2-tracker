import streamlit as st
import json
import os
from datetime import datetime, timedelta

st.set_page_config(layout="wide")

# ---------------- BACKGROUND STYLE ---------------- #
st.markdown("""
<style>
body {
    background-color: #eaf4ff;
}
.stApp {
    background-image: url("https://images.unsplash.com/photo-1523580494863-6f3031224c94");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
h1, h2, h3 {
    text-align: center;
}
.circle-container {
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
}
.circle {
    width: 170px;
    height: 170px;
    border-radius: 50%;
    position: relative;
    text-align: center;
    font-weight: bold;
}
.inner-circle {
    width: 120px;
    height: 120px;
    background: white;
    border-radius: 50%;
    position: absolute;
    top: 25px;
    left: 25px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- DATA FILE ---------------- #
DATA_FILE = "progress.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

progress_data = load_data()

# ---------------- SYLLABUS ---------------- #

aptitude_topics = [
    "Number System","BODMAS","Decimals","Fractions","LCM","HCF",
    "Ratio & Proportion","Percentages","Mensuration","Time & Work",
    "Time & Distance","Simple Interest","Compound Interest",
    "Profit & Loss","Algebra","Geometry","Trigonometry",
    "Statistics","Square Root","Age Problems","Calendar","Clock","Pipes"
]

reasoning_topics = [
    "Analogies","Alphabetical Series","Number Series","Coding-Decoding",
    "Mathematical Operations","Relationships","Syllogism",
    "Jumbling","Venn Diagram","Data Interpretation",
    "Conclusions","Decision Making","Similarities","Differences",
    "Analytical Reasoning","Classification","Directions",
    "Statement-Arguments","Assumptions"
]

engineering_topics = [
    "Engineering Drawing","Units & Measurements","Mass Weight Density",
    "Work Power Energy","Speed Velocity","Heat Temperature",
    "Basic Electricity","Levers & Simple Machines",
    "Occupational Safety","Environment","IT Literacy"
]

fitter_topics = [
    "Occupational Safety","Marking Tools","Hand Tools","Measuring Tools",
    "Cutting Tools","Sheet Metal","Brazing","Riveting","Welding",
    "Drilling","Screw Threads","Grinding","Limits & Fits",
    "Lathe Construction","Lathe Accessories","Lathe Tools",
    "Lathe Operations","Preventive Maintenance"
]

# ---------------- TOTAL CALCULATION ---------------- #

total_topics = len(aptitude_topics) + len(reasoning_topics) + len(engineering_topics) + len(fitter_topics)

apt_completed = progress_data.get("apt", [])
res_completed = progress_data.get("res", [])
eng_completed = progress_data.get("eng", [])
fit_completed = progress_data.get("fit", [])

total_completed = len(apt_completed) + len(res_completed) + len(eng_completed) + len(fit_completed)

overall_percentage = round((total_completed / total_topics) * 100) if total_topics > 0 else 0

# ---------------- HEADINGS ---------------- #

st.markdown("<h1>📅 50 DAY MASTER STUDY PLAN</h1>", unsafe_allow_html=True)

start_date = datetime.now() + timedelta(days=1)
day_number = min(50, total_completed + 1)
current_date = (start_date + timedelta(days=day_number-1)).strftime("%d %B %Y")

st.markdown(f"<h2>Day {day_number} - {current_date}</h2>", unsafe_allow_html=True)

# ---------------- CHECKBOX SECTION ---------------- #

col1, col2, col3, col4 = st.columns(4)

with col1:
    topic = aptitude_topics[day_number % len(aptitude_topics)]
    if st.checkbox(f"Aptitude (Topic: {topic})", key="apt_check"):
        if topic not in apt_completed:
            apt_completed.append(topic)
            progress_data["apt"] = apt_completed
            save_data(progress_data)

with col2:
    topic = reasoning_topics[day_number % len(reasoning_topics)]
    if st.checkbox(f"Reasoning (Topic: {topic})", key="res_check"):
        if topic not in res_completed:
            res_completed.append(topic)
            progress_data["res"] = res_completed
            save_data(progress_data)

with col3:
    topic = engineering_topics[day_number % len(engineering_topics)]
    if st.checkbox(f"Engineering Science (Topic: {topic})", key="eng_check"):
        if topic not in eng_completed:
            eng_completed.append(topic)
            progress_data["eng"] = eng_completed
            save_data(progress_data)

with col4:
    topic = fitter_topics[day_number % len(fitter_topics)]
    if st.checkbox(f"Fitter Core (Topic: {topic})", key="fit_check"):
        if topic not in fit_completed:
            fit_completed.append(topic)
            progress_data["fit"] = fit_completed
            save_data(progress_data)

# ---------------- SUBJECT CUMULATIVE PERCENTAGE ---------------- #

apt_percent = round((len(apt_completed) / len(aptitude_topics)) * 100)
res_percent = round((len(res_completed) / len(reasoning_topics)) * 100)
eng_percent = round((len(eng_completed) / len(engineering_topics)) * 100)
fit_percent = round((len(fit_completed) / len(fitter_topics)) * 100)

# ---------------- CIRCULAR DISPLAY ---------------- #

def circle(percent):
    color = "green" if percent == 100 else "red"
    pending = 100 - percent
    st.markdown(f"""
    <div class="circle" style="background: conic-gradient({color} {percent*3.6}deg, #f4cccc 0deg);">
        <div class="inner-circle">
            <div>{percent}%</div>
            <div style='color:red;'>P {pending}%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='circle-container'>", unsafe_allow_html=True)
circle(apt_percent)
circle(res_percent)
circle(eng_percent)
circle(fit_percent)
st.markdown("</div>", unsafe_allow_html=True)
