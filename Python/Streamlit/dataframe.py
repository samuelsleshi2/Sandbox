import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

st.header('Welcome to my project')
st.write('Hello, *World!* :sunglasses:')
st.write(1234)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [5, 6, 7, 8]
    })
st.write(df)

st.write('Just want to show you my DataFrame:', df, 'It\'s cool, right?')

df2 = pd.DataFrame(
        np.random.randn(200, 3),
        columns = ['a', 'b', 'c'])

c = alt.Chart(df2).mark_circle().encode(
    x = 'a', y = 'b', size = 'c', color = 'c', tooltip = ['a', 'b', 'c'])
st.write(c)