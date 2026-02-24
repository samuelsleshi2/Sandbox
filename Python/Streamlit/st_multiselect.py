import streamlit as st

st.header("st.multiselect")

options = st.multiselect(
    "What are you favorite colors? ", ["Green", "Yellow", "Red"], ["Yellow", "Red"]
)

st.write("You selected ", options)