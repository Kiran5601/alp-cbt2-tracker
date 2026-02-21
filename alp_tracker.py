import streamlit as st
import random

st.set_page_config(page_title="KIRAN ALP CBT-2 PREPARATION TRACKER", layout="wide")

# ---------------- BACKGROUND + STYLE ----------------
st.markdown("""
<style>

/* Train Background with Light Blue Overlay */
.stApp {
    background: linear-gradient(rgba(214,236,255,0.85), rgba(214,236,255,0.85)),
                url("https://images.unsplash.com/photo-1504384308090-c894fdcc538d");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #0d47a1;
    margin-bottom: 20px;
}

/* Section Box */
.section-box {
    background-color: rgba(255,255,255,0.95);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 25px;
    box-shadow: 0px 6px 15px rgba(0,0,0,0.15);
}

/* Quote Box */
.quote-box {
    background-color: rgba(255,255,255,0.9);
    padding: 15px;
    border-radius: 10px;
    text-align:center;
    font-size:18px;
    margin-bottom:20px;
}

/* Circle container */
.circle-container {
    display:flex;
    justify-content:center;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="main-title">🚆 KIRAN ALP CBT-2 PREPARATION TRACKER 🚆</div>', unsafe_allow_html=True)

# ---------------- MOTIVATIONAL QUOTES ----------------
quotes = [
    "Success in Railways starts with daily discipline.",
    "Every topic completed brings you closer to selection.",
    "Consistency + Practice = Railway Job.",
    "Small daily progress creates big exam success.",
    "Hard work today, Railway uniform tomorrow."
]

st.markdown(f'<div class="quote-box">💡 {random.choice(quotes)}</div>', unsafe_allow_html=True)

# ---------------- FULL SYLLABUS ----------------
syllabus = {

    "📘 Mathematics": [
        "Number System","BODMAS","Decimals","Fractions","LCM & HCF",
        "Ratio and Proportion","Percentages","Mensuration",
        "Time and Work","Time and Distance",
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

# ---------------- TRACKING ----------------
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

    total_topics += len(topics)
    total_done += done

    percent = (done / len(topics)) * 100
    st.progress(percent / 100)
    st.write(f"Completed: {percent:.1f}%")
    st.write(f"Pending: {100 - percent:.1f}%")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- OVERALL CALCULATION ----------------
overall = 0
if total_topics > 0:
    overall = int((total_done / total_topics) * 100)

# ---------------- ANIMATED CIRCLE ----------------
circle_html = f"""
<div class="circle-container">
<svg width="220" height="220">
  <circle cx="110" cy="110" r="90" stroke="#bbdefb" stroke-width="18" fill="none"/>
  <circle cx="110" cy="110" r="90"
    stroke="#1565c0"
    stroke-width="18"
    fill="none"
    stroke-dasharray="565"
    stroke-dashoffset="{565 - (565 * overall / 100)}"
    stroke-linecap="round"
    transform="rotate(-90 110 110)"
  />
  <text x="50%" y="50%" text-anchor="middle" dy=".3em"
    font-size="32" fill="#0d47a1">{overall}%</text>
</svg>
</div>
"""

st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.subheader("📊 Overall Completion")
st.markdown(circle_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CONFETTI ----------------
if overall == 100:
    st.balloons()
    st.success("🎉 100% SYLLABUS COMPLETED! ALP SELECTION MODE ACTIVATED 🚆🔥")
