import streamlit as st
import time

st.title("st.progress")

with st.expander("About this app"):
    st.write("This shows a progress bar")

bar = st.progress(0)

for percent in range(100):
    time.sleep(0.05)
    bar.progress(percent + 1)

st.balloons()
st.snow()