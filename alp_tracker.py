# ============================================================
# ================= 50 DAY STUDY PLAN ========================
# ============================================================

st.header("50 DAY MASTER STUDY PLAN")

from math import pi

def day_circle(completed_count):
    radius = 45
    circumference = 2 * pi * radius
    segment = circumference / 4

    light_red = "#ffcdd2"
    red = "#c62828"
    green = "#2e7d32"

    if completed_count == 4:
        stroke_color = green
        offset = 0
    else:
        stroke_color = red
        offset = circumference - (segment * completed_count)

    percent = int((completed_count / 4) * 100)

    circle_html = f"""
    <div style="display:flex;justify-content:center;">
    <svg width="130" height="130">
        <circle cx="65" cy="65" r="{radius}"
            stroke="{light_red}"
            stroke-width="14"
            fill="none"/>
        <circle cx="65" cy="65" r="{radius}"
            stroke="{stroke_color}"
            stroke-width="14"
            fill="none"
            stroke-dasharray="{circumference}"
            stroke-dashoffset="{offset}"
            transform="rotate(-90 65 65)"
            style="transition: stroke-dashoffset 0.8s ease-out;"
        />
        <text x="50%" y="50%" text-anchor="middle"
            dy=".3em"
            font-size="20"
            font-weight="bold"
            fill="{stroke_color}">
            {percent}%
        </text>
    </svg>
    </div>
    """
    st.markdown(circle_html, unsafe_allow_html=True)

# ---------------- FULL TOPIC LISTS ----------------

arithmetic_topics = [
"Number System","BODMAS","Decimals","Fractions","LCM","HCF",
"Ratio & Proportion","Percentages","Mensuration",
"Time & Work","Time & Distance","Simple Interest",
"Compound Interest","Profit & Loss","Algebra",
"Geometry","Trigonometry","Statistics",
"Square Root","Age Problems","Calendar",
"Clock","Pipes & Cistern"
]

reasoning_topics = [
"Analogies","Alphabetical Series","Number Series",
"Coding-Decoding","Mathematical Operations",
"Relationships","Syllogism","Jumbling",
"Venn Diagram","Data Interpretation",
"Data Sufficiency","Conclusions",
"Decision Making","Classification",
"Directions","Statement-Arguments"
]

engineering_topics = [
"Engineering Drawing","Views & Projections",
"Drawing Instruments","Units & Measurement",
"Mass Weight Density","Work Power Energy",
"Heat & Temperature","Basic Electricity",
"Levers & Machines","Occupational Safety",
"Environment","IT Literacy"
]

fitter_topics = [
"Safety","Marking Tools","Metals",
"Hand Tools","Measuring Tools","Cutting Tools",
"Sheet Metal Work","Welding",
"Drilling & Reaming","Grinding",
"Lathe Construction","Lathe Operations",
"Limits & Fits","Heat Treatment",
"Bearings","Hydraulics","Jigs & Fixtures"
]

start_date = datetime.now() + timedelta(days=1)

total_slots = 0
completed_slots = 0

for day in range(1, 51):

    date = start_date + timedelta(days=day-1)

    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader(f"Day {day} – {date.strftime('%d %B %Y')}")

    # Proper rotation
    arithmetic = arithmetic_topics[(day-1) % len(arithmetic_topics)]
    reasoning = reasoning_topics[(day-1) % len(reasoning_topics)]
    engineering = engineering_topics[(day-1) % len(engineering_topics)]
    fitter = fitter_topics[(day-1) % len(fitter_topics)]

    daily = {
        "6-8 AM Aptitude": f"{arithmetic} + {reasoning}",
        "10-1 PM Mock Test": "Full Length Mock + Analysis",
        "5-7 PM Engineering Science": engineering,
        "9-12 PM Fitter Core I & II": fitter
    }

    completed_today = 0

    for slot, topic in daily.items():
        key = f"Day{day}_{slot}"
        default_value = progress_data.get(key, False)

        checked = st.checkbox(f"{slot} → {topic}", value=default_value, key=key)
        progress_data[key] = checked

        total_slots += 1
        if checked:
            completed_today += 1
            completed_slots += 1

    # Circular progress per day
    day_circle(completed_today)

    st.markdown('</div>', unsafe_allow_html=True)
