
import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Student Performance Analyzer")
st.write("Analyze student marks using this cloud-based application.")

st.divider()

# Student details
st.subheader("Enter Student Details")

name = st.text_input("Student Name")
roll_no = st.text_input("Roll Number")

num_subjects = st.number_input(
    "Number of Subjects",
    min_value=1,
    max_value=10,
    value=5,
    step=1
)

# Enter marks
st.subheader("Enter Subject Marks")

marks = []

for i in range(int(num_subjects)):
    mark = st.number_input(
        f"Subject {i + 1} Marks (out of 100)",
        min_value=0,
        max_value=100,
        value=0,
        key=f"mark_{i}"
    )
    marks.append(mark)

# Analyze button
if st.button("Analyze Performance", type="primary"):

    if name.strip() == "":
        st.error("Please enter the student name.")

    else:
        total = sum(marks)
        maximum = int(num_subjects) * 100
        percentage = (total / maximum) * 100

        if all(mark >= 35 for mark in marks):
            result = "PASS"
        else:
            result = "FAIL"

        st.divider()
        st.subheader("📊 Student Result")

        st.write("**Student Name:**", name)
        st.write("**Roll Number:**", roll_no)

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Marks", f"{total}/{maximum}")
        col2.metric("Percentage", f"{percentage:.2f}%")
        col3.metric("Result", result)

        if result == "PASS":
            st.success("Congratulations! Student passed.")
        else:
            st.warning("Student needs improvement.")

        # Subject-wise marks table
        data = pd.DataFrame({
            "Subject": [
                f"Subject {i + 1}"
                for i in range(int(num_subjects))
            ],
            "Marks": marks
        })

        st.subheader("📈 Subject-wise Performance")
        st.bar_chart(data.set_index("Subject"))

        st.subheader("Marks Details")
        st.dataframe(data, use_container_width=True)

st.divider()
st.caption("Cloud Computing Mini Project | Python + Streamlit")
