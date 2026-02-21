import streamlit as st

st.set_page_config(page_title="ALP CBT-2 Tracker")

st.title("ALP CBT-2 Preparation Tracker")

syllabus = {
    "Engineering Science": [
        "Units and Measurements",
        "Work, Power and Energy",
        "Heat",
        "Basic Electricity",
        "Basic Electronics"
    ],
    "Arithmetic": [
        "Number System",
        "Percentage",
        "Ratio and Proportion",
        "Time and Work",
        "Profit and Loss"
    ],
    "Pure Maths": [
        "Algebra",
        "Trigonometry",
        "Geometry",
        "Mensuration"
    ],
    "Core Section": [
        "Engineering Drawing",
        "Workshop Calculation",
        "Machine Tools",
        "Welding",
        "Fitting"
    ]
}

total_topics = 0
total_done = 0

for section, topics in syllabus.items():
    st.header(section)
    done = 0
    
    for topic in topics:
        if st.checkbox(topic, key=section + topic):
            done += 1
    
    total_topics += len(topics)
    total_done += done
    
    percent = (done / len(topics)) * 100
    st.write(f"Completed: {percent:.1f}%")
    st.write(f"Pending: {100 - percent:.1f}%")
    st.write("---")

overall = (total_done / total_topics) * 100
st.header("Overall Progress")
st.progress(overall / 100)
st.write(f"Total Completed: {overall:.1f}%")
st.write(f"Total Pending: {100 - overall:.1f}%")
