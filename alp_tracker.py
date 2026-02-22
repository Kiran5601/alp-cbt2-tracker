import streamlit as st
import base64
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="KIRAN ALP CBT-2 PREPARATION TRACKER", layout="wide")

# ---------------- LOAD BACKGROUND IMAGE ----------------
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_base64 = get_base64("background.jpg")

# ---------------- CUSTOM STYLING ----------------
st.markdown(f"""
<style>
.stApp {{
    background-image: url("data:image/jpg;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

h1 {{
    text-align: center;
    color: #00ccff;
    font-size: 40px;
}}

.section-box {{
    background-color: rgba(255,255,255,0.90);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
}}

.topic-title {{
    color: #00ccff;
    font-weight: bold;
    font-size: 18px;
}}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1>KIRAN ALP CBT-2 PREPARATION TRACKER</h1>", unsafe_allow_html=True)

# ---------------- MOTIVATIONAL QUOTES ----------------
quotes = [
    "Success is the sum of small efforts repeated daily.",
    "Your railway dream is closer than you think.",
    "Discipline today, selection tomorrow.",
    "Push yourself — ALP badge is waiting.",
    "Consistency beats talent."
]

st.info(random.choice(quotes))

# ---------------- SYLLABUS ----------------

syllabus = {

    "PART A - MATHEMATICS": [
        "Number System",
        "BODMAS",
        "Decimals & Fractions",
        "LCM & HCF",
        "Ratio & Proportion",
        "Percentages",
        "Mensuration",
        "Time and Work",
        "Time and Distance",
        "Simple & Compound Interest",
        "Profit and Loss",
        "Algebra",
        "Geometry & Trigonometry",
        "Elementary Statistics",
        "Square Root",
        "Age Calculations",
        "Calendar & Clock",
        "Pipes & Cistern"
    ],

    "PART A - REASONING": [
        "Analogies",
        "Alphabetical Series",
        "Number Series",
        "Coding & Decoding",
        "Mathematical Operations",
        "Relationships",
        "Syllogism",
        "Jumbling",
        "Venn Diagram",
        "Data Interpretation",
        "Decision Making",
        "Similarities & Differences",
        "Analytical Reasoning",
        "Classification",
        "Directions",
        "Statement & Arguments"
    ],

    "PART A - SCIENCE & ENGINEERING": [
        "Engineering Drawing",
        "Units & Measurements",
        "Mass Weight & Density",
        "Work Power & Energy",
        "Speed & Velocity",
        "Heat & Temperature",
        "Basic Electricity",
        "Levers & Simple Machines",
        "Occupational Safety",
        "Environment & IT Literacy"
    ],

    "PART B - TRADE THEORY (1st Year)": [
        "Occupational Health and Safety",
        "Marking and Marking Tools",
        "Metals",
        "Hand Tools",
        "Measurement Tools",
        "Cutting Tools",
        "Sheet Metal Work",
        "Brazing and Soldering",
        "Riveting",
        "Welding",
        "Drilling and Reaming",
        "Screw Threads",
        "Grinding",
        "Limits and Fits",
        "Lathe Construction",
        "Lathe Accessories",
        "Lathe Tools",
        "Lathe Operations",
        "Preventive Maintenance"
    ],

    "PART B - TRADE THEORY (2nd Year)": [
        "Fasteners",
        "Gauges",
        "Drilling Tools",
        "Heat Treatment",
        "Bearings",
        "Pipe Fittings",
        "Jigs and Fixtures"
    ]
}

# ---------------- DISPLAY SECTIONS ----------------

for section, topics in syllabus.items():

    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader(section)

    completed = 0

    for topic in topics:
        checked = st.checkbox(topic, key=section+topic)
        if checked:
            completed += 1

    percentage = int((completed / len(topics)) * 100)

    st.progress(percentage / 100)
    st.write(f"Completion: {percentage}%")

    if percentage == 100:
        st.success("🎉 Section Completed! Excellent Work!")
        st.balloons()

    st.markdown('</div>', unsafe_allow_html=True)
