import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

# Set the title of the Streamlit app
st.title("Streamlit Components and Widgets Demo")

# Introduction section
st.header("Introduction")
st.write("""
Welcome to this Streamlit demo app. Here, we showcase various Streamlit components, widgets, and graph features.
You can interact with the app using the provided widgets and see how the visualizations change dynamically.
""")

# Display text elements
st.subheader("Text Elements")
st.write("This is a regular text element.")
st.markdown("**This is a markdown text element.**")
st.caption("This is a caption text element.")

# Input widgets
st.subheader("Input Widgets")

# Button
if st.button("Click Me"):
    st.write("Button clicked!")

# Checkbox
checkbox = st.checkbox("Check me")
if checkbox:
    st.write("Checkbox is checked.")

# Radio buttons
radio = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {radio}")

# Selectbox
selectbox = st.selectbox("Choose a number:", [1, 2, 3, 4, 5])
st.write(f"You selected: {selectbox}")

# Multiselect
multiselect = st.multiselect("Choose multiple options:", ["A", "B", "C", "D"])
st.write(f"You selected: {multiselect}")

# Slider
slider = st.slider("Select a range of values:", 0, 100, (20, 80))
st.write(f"Slider range: {slider}")

# Text input
text_input = st.text_input("Enter some text:")
st.write(f"Text input: {text_input}")

# Number input
number_input = st.number_input("Enter a number:", min_value=0, max_value=100, value=50)
st.write(f"Number input: {number_input}")

# Date input
date_input = st.date_input("Select a date:")
st.write(f"Date input: {date_input}")

# File uploader
uploaded_file = st.file_uploader("Upload a file")
if uploaded_file:
    st.write("File uploaded successfully.")

# Displaying data
st.subheader("Displaying Data")
df = pd.DataFrame({
    'A': np.random.rand(10),
    'B': np.random.rand(10)
})
st.write("Dataframe example:")
st.dataframe(df)

# Plotly chart
st.subheader("Plotly Chart")
fig = px.scatter(df, x='A', y='B', title="Scatter Plot Example")
st.plotly_chart(fig)

# Matplotlib chart
st.subheader("Matplotlib Chart")
fig, ax = plt.subplots()
ax.plot(df['A'], df['B'], 'o')
ax.set_title("Matplotlib Scatter Plot Example")
st.pyplot(fig)

# Streamlit line chart
st.subheader("Streamlit Line Chart")
st.line_chart(df)

# Streamlit area chart
st.subheader("Streamlit Area Chart")
st.area_chart(df)

# Streamlit bar chart
st.subheader("Streamlit Bar Chart")
st.bar_chart(df)

# Sidebar elements
st.sidebar.header("Sidebar")
st.sidebar.write("This is the sidebar.")
sidebar_selectbox = st.sidebar.selectbox("Choose a side option:", ["Sidebar Option 1", "Sidebar Option 2"])
st.sidebar.write(f"Sidebar selected: {sidebar_selectbox}")

st.sidebar.slider("Sidebar Slider:", 0, 50, 25)

# Conclusion
st.subheader("Conclusion")
st.write("""
This demo app showcases various components and widgets available in Streamlit. You can use these elements to create
interactive and dynamic data applications.
""")
