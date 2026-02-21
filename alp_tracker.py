import streamlit as st
import random

st.set_page_config(page_title="ALP CBT-2 Tracker", layout="wide")

# ---------- BACKGROUND ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #e0f7fa, #fce4ec);
}
.section-box {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
}
.quote-box {
    background-color: #fff3e0;
    padding: 15px;
    border-radius: 10px;
    font-size:18px;
    text-align:center;
    margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- MOTIVATIONAL QUOTES ----------
quotes = [
    "Success in Railways starts with daily discipline.",
    "Small daily progress leads to big exam results.",
    "Your effort today decides your rank tomorrow.",
    "Consistency beats intelligence in competitive exams.",
    "Dream ALP uniform? Then study like a champion.",
    "Every topic completed is one step closer to selection.",
    "Hard work never fails in Railway exams.",
    "Focus. Practice. Repeat. Success will follow."
]

st.markdown(f'<div class="quote-box">💡 {random.choice(quotes)}</div>', unsafe_allow_html=True)

st.title("🚆 ALP CBT-2 Preparation Tracker")

# ---------------- SYLLABUS ----------------

syllabus = {
    "📘 Mathematics": [
        "Number System","BODMAS","Decimals","Fractions",
        "LCM & HCF","Ratio and Proportion","Percentages",
        "Mensuration","Time and Work","Time and Distance",
        "Simple & Compound Interest","Profit and Loss",
        "Algebra","Geometry","Trigonometry",
        "Statistics","Square Root","Age Problems",
        "Calendar & Clock","Pipes & Cistern"
    ],
    "🧠 Reasoning": [
        "Analogies","Alphabetical & Number Series",
        "Coding-Decoding","Mathematical Operations",
        "Relationships","Syllogism","Jumbling",
        "Venn Diagram","Data Interpretation",
        "Decision Making","Similarities & Differences",
        "Analytical Reasoning","Classification",
        "Directions","Statement-Arguments"
    ],
    "🔬 Science & Engineering": [
        "Engineering Drawing","Drawing Instruments & Lines",
        "Units & Measurements","Mass, Weight & Density",
        "Work, Power & Energy","Speed & Velocity",
        "Heat & Temperature","Basic Electricity",
        "Levers & Simple Machines","Occupational Safety",
        "Environment","IT Literacy"
    ],
    "🔧 Fitter 1st Year": [
        "Introduction","Occupational Health & Safety",
        "Marking & Marking Tools","Metals",
        "Hand Tools","Measurement & Measuring Tools",
        "Cutting Tools & Operations","Sheet Metal Work",
        "Brazing & Soldering","Riveting",
        "Welding","Drilling & Reaming",
        "Screw Threads","Grinding",
        "Limits & Fits","Lathe Construction",
        "Lathe Accessories","Lathe Tools",
        "Lathe Operations","Preventive Maintenance"
    ],
    "⚙ Fitter 2nd Year": [
        "Fasteners","Gauges","Pipe Fittings",
        "Bearings","Jigs & Fixtures",
        "Working Materials","Transmission of Power",
        "Hydraulics","Lubricants & Coolants",
        "Lifting Appliances","CNC Basics"
    ]
}

# --------------- TRACKING ---------------

total_topics = 0
total_done = 0

for section, topics in syllabus.items():
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader(section)

    done = 0
    cols = st.columns(2)

    for i, topic in enumerate(topics):
        if cols[i % 2].checkbox(topic, key=section + topic):
            done += 1

    section_total = len(topics)
    total_topics += section_total
    total_done += done

    percent = (done / section_total) * 100

    st.progress(percent / 100)
    st.write(f"Completed: {percent:.1f}%")
    st.write(f"Pending: {100 - percent:.1f}%")

    st.markdown('</div>', unsafe_allow_html=True)

# --------------- OVERALL ---------------

overall = (total_done / total_topics) * 100

st.header("📊 Overall Progress")
st.progress(overall / 100)
st.write(f"Total Completed: {overall:.1f}%")
st.write(f"Total Pending: {100 - overall:.1f}%")

# --------------- CONFETTI CELEBRATION ---------------

if overall == 100:
    st.balloons()
    st.success("🎉 Congratulations Mrs Kiran! You completed 100% of the syllabus! ALP Selection Loading... 🚆🔥")
