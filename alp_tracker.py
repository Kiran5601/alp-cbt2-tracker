import streamlit as st
import math

st.set_page_config(layout="wide")

# ---------------- BACKGROUND ---------------- #

st.markdown("""
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1523580846011-d3a5bc25702b");
    background-size: cover;
    background-attachment: fixed;
}

.main {
    background-color: rgba(255,255,255,0.88);
    padding: 30px;
    border-radius: 15px;
}

h1, h2, h3 {
    text-align: center;
}

.circle-container {
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)

st.markdown("<h1>📅 50 DAY MASTER STUDY PLAN</h1>", unsafe_allow_html=True)

# ---------------- SUBJECT TOPICS ---------------- #

aptitude_topics = [
    "Number System", "BODMAS", "Decimals", "Fractions", "LCM & HCF",
    "Ratio & Proportion", "Percentages", "Time & Work",
    "Time & Distance", "Simple & Compound Interest",
    "Profit & Loss", "Algebra", "Geometry",
    "Trigonometry", "Statistics", "Square Root",
    "Ages", "Calendar", "Clock", "Pipes & Cistern"
]

reasoning_topics = [
    "Analogies", "Alphabetical Series", "Number Series",
    "Coding & Decoding", "Mathematical Operations",
    "Relationships", "Syllogism", "Jumbling",
    "Venn Diagram", "Data Interpretation",
    "Conclusions", "Decision Making",
    "Similarities & Differences",
    "Analytical Reasoning", "Classification",
    "Directions", "Statements & Assumptions"
]

engineering_topics = [
    "Units & Measurements", "Mass & Density",
    "Work Power Energy", "Speed & Velocity",
    "Heat & Temperature", "Basic Electricity",
    "Levers & Machines", "Safety & Health",
    "Environment", "IT Literacy"
]

fitter_topics = [
    "Safety", "Marking Tools", "Metals",
    "Hand Tools", "Measuring Tools",
    "Cutting Tools", "Sheet Metal",
    "Welding", "Drilling",
    "Grinding", "Limits & Fits",
    "Lathe Construction",
    "Lathe Accessories",
    "Lathe Tools",
    "Lathe Operations"
]

total_topics = (
    len(aptitude_topics)
    + len(reasoning_topics)
    + len(engineering_topics)
    + len(fitter_topics)
)

# ---------------- CHECKLIST ---------------- #

st.markdown("<h2>Daily Topic Completion</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Aptitude")
    apt_completed = []
    for topic in aptitude_topics:
        if st.checkbox(topic, key="apt_" + topic):
            apt_completed.append(topic)

    st.subheader("Reasoning")
    res_completed = []
    for topic in reasoning_topics:
        if st.checkbox(topic, key="res_" + topic):
            res_completed.append(topic)

with col2:
    st.subheader("Engineering Science")
    eng_completed = []
    for topic in engineering_topics:
        if st.checkbox(topic, key="eng_" + topic):
            eng_completed.append(topic)

    st.subheader("Fitter Core")
    fit_completed = []
    for topic in fitter_topics:
        if st.checkbox(topic, key="fit_" + topic):
            fit_completed.append(topic)

# ---------------- CUMULATIVE CALCULATION ---------------- #

total_completed = (
    len(apt_completed)
    + len(res_completed)
    + len(eng_completed)
    + len(fit_completed)
)

overall_percentage = round((total_completed / total_topics) * 100)

# Individual cumulative %
apt_percent = round((len(apt_completed) / len(aptitude_topics)) * 100)
res_percent = round((len(res_completed) / len(reasoning_topics)) * 100)
eng_percent = round((len(eng_completed) / len(engineering_topics)) * 100)
fit_percent = round((len(fit_completed) / len(fitter_topics)) * 100)

# ---------------- CIRCLE FUNCTION ---------------- #

def draw_circle(percent, title):
    color = "#00b894" if percent == 100 else "#ff7675"

    circle_html = f"""
    <div style='text-align:center'>
        <h3>{title}</h3>
        <div style="
            width:150px;
            height:150px;
            border-radius:50%;
            background:conic-gradient({color} {percent*3.6}deg, #ffe6e6 0deg);
            display:flex;
            align-items:center;
            justify-content:center;
            margin:auto;
        ">
            <div style="
                width:110px;
                height:110px;
                border-radius:50%;
                background:white;
                display:flex;
                flex-direction:column;
                align-items:center;
                justify-content:center;
                font-weight:bold;
                font-size:18px;
            ">
                {percent}%<br>
                <span style='color:red'>P {100-percent}%</span>
            </div>
        </div>
    </div>
    """
    st.markdown(circle_html, unsafe_allow_html=True)

# ---------------- DISPLAY CIRCLES HORIZONTAL ---------------- #

st.markdown("<h2>Subject Wise Cumulative Progress</h2>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    draw_circle(apt_percent, "Aptitude")

with c2:
    draw_circle(res_percent, "Reasoning")

with c3:
    draw_circle(eng_percent, "Engineering")

with c4:
    draw_circle(fit_percent, "Fitter Core")

# ---------------- OVERALL CIRCLE ---------------- #

st.markdown("<h2>Overall 50 Day Completion</h2>", unsafe_allow_html=True)

draw_circle(overall_percentage, "TOTAL SYLLABUS")

st.markdown('</div>', unsafe_allow_html=True)
