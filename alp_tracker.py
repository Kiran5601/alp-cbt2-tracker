import streamlit as st
import random

st.set_page_config(page_title="KIRAN ALP CBT-2 PREPARATION TRACKER", layout="wide")

# -------------------- STYLE --------------------
st.markdown("""
<style>

.stApp {
    background-color: #eaf4ff;
}

.stApp::before {
    content: "";
    background-image: url("https://img.freepik.com/free-vector/student-studying-desk_23-2148880412.jpg");
    background-repeat: no-repeat;
    background-position: center 65%;
    background-size: 650px;
    opacity: 0.05;
    position: fixed;
    width: 100%;
    height: 100%;
    z-index: -1;
}

/* Heading */
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    background: linear-gradient(90deg, #1565c0, #8e24aa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-top: 20px;
}

/* Quote */
.quote-box {
    text-align: center;
    font-size: 22px;
    font-weight: 600;
    margin-top: 40px;
    margin-bottom: 60px;
    color: #5e35b1;
}

/* Section Box */
.section-box {
    background-color: rgba(255,255,255,0.95);
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 30px;
    box-shadow: 0px 5px 12px rgba(0,0,0,0.1);
}

.circle-container {
    display:flex;
    justify-content:center;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# -------------------- TITLE --------------------
st.markdown('<div class="main-title">KIRAN ALP CBT-2 PREPARATION TRACKER</div>', unsafe_allow_html=True)

# -------------------- QUOTES --------------------
quotes = [
    "Small daily progress leads to big success.",
    "Discipline today, selection tomorrow.",
    "Consistency beats talent.",
    "Railway uniform loading...",
    "Stay focused. You are closer than you think."
]

st.markdown(f'<div class="quote-box">💡 {random.choice(quotes)}</div>', unsafe_allow_html=True)

# -------------------- FULL SYLLABUS --------------------

syllabus = {

"PART A - ARITHMETIC": [
"Number System","BODMAS","Decimals","Fractions","LCM","HCF",
"Ratio & Proportion","Percentages","Mensuration",
"Time & Work","Time & Distance",
"Simple Interest","Compound Interest",
"Profit & Loss","Algebra",
"Geometry","Trigonometry",
"Elementary Statistics","Square Root",
"Age Calculations","Calendar","Clock",
"Pipes & Cistern"
],

"PART A - REASONING": [
"Analogies","Alphabetical Series","Number Series",
"Coding-Decoding","Mathematical Operations",
"Relationships","Syllogism","Jumbling",
"Venn Diagram","Data Interpretation",
"Data Sufficiency","Conclusions",
"Decision Making","Similarities & Differences",
"Analytical Reasoning","Classification",
"Directions","Statement-Arguments",
"Assumptions"
],

"PART A - ENGINEERING SCIENCE": [
"Engineering Drawing","Views & Projections",
"Drawing Instruments","Lines",
"Geometric Figures","Symbolic Representation",
"Units & Measurements","Mass Weight Density",
"Work Power Energy","Speed & Velocity",
"Heat & Temperature","Basic Electricity",
"Levers & Simple Machines",
"Occupational Safety & Health",
"Environmental Education","IT Literacy"
],

"PART B - TRADE THEORY (1st Year)": [
"Introduction","Occupational Safety",
"Marking Tools","Metals",
"Hand Tools","Measuring Tools",
"Cutting Tools","Sheet Metal Work",
"Brazing & Soldering","Riveting",
"Welding","Drilling & Reaming",
"Screw Threads","Grinding",
"Limits & Fits","Lathe Construction",
"Lathe Accessories","Lathe Tools",
"Lathe Operations","Preventive Maintenance"
],

"PART B - TRADE THEORY (2nd Year)": [
"Fasteners","Gauges","Metrology",
"Heat Treatment","Bearings",
"Pipe Fittings","Jigs & Fixtures",
"Working Materials","Transmission of Power",
"Hydraulics & Pneumatics",
"Lubricants & Coolants",
"Lifting Appliances"
]
}

# -------------------- PROGRESS CALCULATION --------------------

total_topics = 0
total_done = 0

for section, topics in syllabus.items():

    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader(section)

    done = 0
    for topic in topics:
        if st.checkbox(topic, key=section+topic):
            done += 1

    total_topics += len(topics)
    total_done += done

    completed = int((done / len(topics)) * 100)
    pending = 100 - completed

    st.progress(completed / 100)
    st.write(f"Completed: {completed}%")
    st.write(f"Pending: {pending}%")

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- OVERALL STATUS --------------------

overall_completed = int((total_done / total_topics) * 100)
overall_pending = 100 - overall_completed

circle_html = f"""
<div class="circle-container">
<svg width="240" height="240">
  <circle cx="120" cy="120" r="100" stroke="#d6e4ff" stroke-width="18" fill="none"/>
  <circle cx="120" cy="120" r="100"
    stroke="#1976d2"
    stroke-width="18"
    fill="none"
    stroke-dasharray="628"
    stroke-dashoffset="{628 - (628 * overall_completed / 100)}"
    stroke-linecap="round"
    transform="rotate(-90 120 120)"
    style="transition: stroke-dashoffset 1.2s ease-in-out;"
  />
  <text x="50%" y="45%" text-anchor="middle"
    font-size="36" fill="black" font-weight="bold">{overall_completed}%</text>
  <text x="50%" y="65%" text-anchor="middle"
    font-size="16" fill="gray">Pending: {overall_pending}%</text>
</svg>
</div>
"""

st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.subheader("Overall Completion Status")
st.markdown(circle_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# -------------------- CELEBRATION --------------------

if overall_completed == 100:
    st.balloons()
    st.success("🎉 100% SYLLABUS COMPLETED! READY FOR EXAM! 🎉")
