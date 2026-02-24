import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
    "What is your favorite color?", ("Red", "Blue", "Green")
)

st.write("Your favorite color is ", option)