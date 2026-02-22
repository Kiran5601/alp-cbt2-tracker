import streamlit as st
import json
import os
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="KIRAN ALP MASTER DASHBOARD", layout="wide")

# ---------------- SAVE SYSTEM ----------------
SAVE_FILE = "master_progress.json"

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
.stApp { background-color: #eef6ff; }

.main-title {
    text-align:center;
    font-size:50px;
    font-weight:900;
    background: linear-gradient(90deg,#1565c0,#8e24aa);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.quote-box {
    text-align:center;
    font-size:22px;
    font-weight:600;
    margin:30px 0 50px 0;
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

st.markdown('<div class="main-title">KIRAN ALP CBT-2 MASTER TRACKER</div>', unsafe_allow_html=True)

quotes = [
"Consistency beats talent.",
"Discipline today, selection tomorrow.",
"Small progress daily = Big success.",
"Railway uniform loading...",
"Stay focused. You are closer than you think."
]

st.markdown(f'<div class="quote-box">💡 {random.choice(quotes)}</div>', unsafe_allow_html=True)

# ---------------- ANIMATED CIRCLE ----------------
def animated_circle(percent):
    green = "#2e7d32"
    red = "#c62828"

    circle_html = f"""
    <div style="display:flex;justify-content:center;">
    <svg width="200" height="200">
        <circle cx="100" cy="100" r="85" stroke="#eee" stroke-width="18" fill="none"/>
        <circle cx="100" cy="100" r="85"
            stroke="{green}"
            stroke-width="18"
            fill="none"
            stroke-dasharray="534"
            stroke-dashoffset="{534 - (534 * percent / 100)}"
            transform="rotate(-90 100 100)"
            style="transition: stroke-dashoffset 1.5s ease-out;"
        />
        <text x="50%" y="45%" text-anchor="middle"
            font-size="36" font-weight="900" fill="{green}">
            {percent}%
        </text>
        <text x="50%" y="65%" text-anchor="middle"
            font-size="18" font-weight="bold" fill="{red}">
            PENDING {100-percent}%
        </text>
    </svg>
    </div>
    """
    st.markdown(circle_html, unsafe_allow_html=True)

# ============================================================
# ================= 50 DAY STUDY PLAN (TOP) ==================
# ============================================================

st.header("📅 50 DAY STUDY PLAN")

start_date = datetime.now() + timedelta(days=1)

aptitude = ["Number System","Percentages","Time & Work","Profit & Loss"]
engg = ["Units","Heat","Electricity","Drawing"]
fitter = ["Welding","Lathe","Grinding","Bearings"]

total_slots = 0
completed_slots = 0

for day in range(1, 51):

    date = start_date + timedelta(days=day-1)

    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader(f"Day {day} – {date.strftime('%d %B %Y')}")

    daily = {
        "6-8 AM Aptitude": aptitude[day % len(aptitude)],
        "10-1 PM Mock Test": "Full Mock + Analysis",
        "5-7 PM Engineering Science": engg[day % len(engg)],
        "9-12 PM Fitter Core": fitter[day % len(fitter)]
    }

    for slot, topic in daily.items():
        key = f"Day{day}_{slot}"
        default_value = progress_data.get(key, False)
        checked = st.checkbox(f"{slot} → {topic}", value=default_value, key=key)
        progress_data[key] = checked

        total_slots += 1
        if checked:
            completed_slots += 1

    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# ================= FULL SYLLABUS TRACKER ====================
# ============================================================

st.header("📘 FULL SYLLABUS TRACKER")

syllabus = {
"ARITHMETIC": ["Number System","BODMAS","LCM & HCF","Percentages",
"Time & Work","Time & Distance","Profit & Loss",
"Simple & Compound Interest","Algebra","Geometry","Trigonometry"],

"REASONING": ["Analogies","Series","Coding-Decoding",
"Syllogism","Venn Diagram","Directions",
"Data Interpretation","Classification"],

"ENGINEERING SCIENCE": ["Engineering Drawing","Units & Measurement",
"Work Power Energy","Heat & Temperature",
"Basic Electricity","Levers","Safety","Environment"],

"FITTER CORE I & II": ["Welding","Lathe","Grinding",
"Bearings","Hydraulics","Metrology"]
}

total_topics = 0
total_done = 0

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
    animated_circle(percent)

    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# ================= MASTER OVERALL ============================
# ============================================================

save_progress(progress_data)

topics_percent = int((total_done / total_topics) * 100) if total_topics else 0
plan_percent = int((completed_slots / total_slots) * 100) if total_slots else 0

final_percent = int((topics_percent + plan_percent) / 2)

st.header("🏆 MASTER OVERALL PROGRESS")
animated_circle(final_percent)

st.write(f"Syllabus Completed: {topics_percent}%")
st.write(f"50-Day Plan Completed: {plan_percent}%")

if final_percent == 100:
    st.balloons()
    st.success("🎉 MASTER PLAN COMPLETED! EXAM READY!")
