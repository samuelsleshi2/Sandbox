import streamlit as st

st.header("Make a choice")

chicken = st.checkbox("Here's some chicken")
steak = st.checkbox("Here's some steak")
beef = st.checkbox("Here's some beef")

if chicken:
    st.write("Enjoy the chicken")

if steak:
    st.write("Enjoy the steak")

if beef:
    st.write("Enjoy the beef")