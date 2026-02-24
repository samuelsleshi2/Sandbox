import streamlit as st
from datetime import time, datetime

st.header('st.slider')

st.subheader('Slider')
age = st.slider('How old are you?', 10, 30, 18)
st.write('I am ', age, ' years old')

st.subheader('Range Slider')
values = st.slider('Pick a range of values', 0.0, 100.0, (25.0, 67.0))
st.write('Values: ', values)

st.subheader('Time Range Slider')
appointment = st.slider('Schedule your appointment:', value = (time(11, 30), time(12, 45)))
st.write('You have scheduled for ', appointment)

st.subheader('Date/time Slider')
start_time = st.slider("When do you want to start? ", value = datetime(2025, 1, 1, 4, 30), format = "MM/DD/YY - hh:mm")
st.write('You will be starting at ', start_time)