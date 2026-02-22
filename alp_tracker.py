import streamlit as st
import random

st.set_page_config(page_title="KIRAN ALP CBT-2 PREPARATION TRACKER", layout="wide")

# ---------------- BACKGROUND STYLE ----------------
st.markdown("""
<style>
.stApp {
    background-color: #e3f2fd;
    background-image: url("https://img.freepik.com/free-vector/girl-studying-concept-illustration_114360-1465.jpg");
    background-repeat: no-repeat;
    background-position: right bottom;
    background-size: 450px;
}

h1 {
    text-align: center;
    color: black;
    font-size: 42px;
}

.section-box {
    background-color: rgba(255,255,255,0.95);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 25px;
    box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
    color: black;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>KIRAN ALP CBT-2 PREPARATION TRACKER</h1>", unsafe_allow_html=True)

# ---------------- MOTIVATIONAL QUOTES ----------------
quotes = [
    "Stay focused. Railway selection is loading...",
    "Small daily progress leads to big success.",
    "Consistency beats talent.",
    "Dream it. Study it. Achieve it.",
    "Your ALP badge is waiting."
]

st.info(random.choice(quotes))

# ---------------- SYLLABUS ----------------
syllabus = {

    "PART A - MATHEMATICS": [
        "Number System", "BODMAS", "Decimals & Fractions", "LCM & HCF",
        "Ratio & Proportion", "Percentages", "Mensuration",
        "Time and Work", "Time and Distance",
        "Simple & Compound Interest", "Profit and Loss",
        "Algebra", "Geometry & Trigonometry",
        "Elementary Statistics", "Square Root",
        "Age Calculations", "Calendar & Clock",
        "Pipes & Cistern"
    ],

    "PART A - REASONING": [
        "Analogies", "Alphabetical Series", "Number Series",
        "Coding & Decoding", "Mathematical Operations",
        "Relationships", "Syllogism", "Jumbling",
        "Venn Diagram", "Data Interpretation",
        "Decision Making", "Similarities & Differences",
        "Analytical Reasoning", "Classification",
        "Directions", "Statement & Arguments"
    ],

    "PART A - SCIENCE & ENGINEERING": [
        "Engineering Drawing", "Units & Measurements",
        "Mass Weight & Density", "Work Power & Energy",
        "Speed & Velocity", "Heat & Temperature",
        "Basic Electricity", "Levers & Simple Machines",
        "Occupational Safety", "Environment & IT Literacy"
    ],

    "PART B - TRADE THEORY (1st Year)": [
        "Occupational Health and Safety", "Marking Tools",
        "Metals", "Hand Tools", "Measurement Tools",
        "Cutting Tools", "Sheet Metal Work",
        "Brazing and Soldering", "Riveting",
        "Welding", "Drilling and Reaming",
        "Screw Threads", "Grinding",
        "Limits and Fits", "Lathe Construction",
        "Lathe Accessories", "Lathe Tools",
        "Lathe Operations", "Preventive Maintenance"
    ],

    "PART B - TRADE THEORY (2nd Year)": [
        "Fasteners", "Gauges", "Drilling Tools",
        "Heat Treatment", "Bearings",
        "Pipe Fittings", "Jigs and Fixtures"
    ]
}

# ---------------- DISPLAY ----------------
for section, topics in syllabus.items():

    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader(section)

    completed = 0

    for topic in topics:
        if st.checkbox(topic, key=section+topic):
            completed += 1

    percentage = int((completed / len(topics)) * 100)

    st.progress(percentage / 100)
    st.write(f"Completion: {percentage}%")

    if percentage == 100:
        st.success("🎉 Section Completed! Excellent Work!")
        st.balloons()

    st.markdown('</div>', unsafe_allow_html=True)
