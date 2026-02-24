import streamlit as st
import requests

st.title('Bored API App')

st.sidebar.header("Input")
selected_type = st.sidebar.selectbox("Select an activity type", ["education", "recreational", "social", "diy"])

suggested_activity_url = f"http://www.boredapi.com/api/activity?type={selected_type}"
suggested_activity = requests.get(suggested_activity_url).json()

c1, c2 = st.columns(2)
with c1:
    with st.expander("About this app"):
        st.write("This app is powered by Bored API to give you fun things to do")
with c2:
    with st.expander("JSON data"):
        st.write(suggested_activity)

st.header("Suggested activity")
st.info(suggested_activity['activity'])

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Number of Participants", value=suggested_activity['participants'], delta="")
with col2:
    st.metric(label="Type of Activity", value = suggested_activity['type'].capitalize(), delta="")
with col3:
    st.metric(label="Price", value=suggested_activity['price'], delta="")