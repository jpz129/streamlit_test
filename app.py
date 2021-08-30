import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

@st.cache
def get_data():
    url = "http://data.insideairbnb.com/united-states/or/portland/2021-07-13/visualisations/listings.csv"
    return pd.read_csv(url)

df = get_data()

st.title('Portland AirBnB Listings')
st.image('https://cdn.geekwire.com/wp-content/uploads/2019/06/bigstock-Portland-Oregon-USA-skyline-247939699-768x512.jpg',
         caption='A view of Portland')

st.header('Data')
st.write(df)
pressed = st.button('Generate EDA Report')

if pressed == True:
    pr = ProfileReport(df, explorative=True)
    st.write('---')
    st.header('Profiling Report')
    st_profile_report(pr)
else:
    st.write('Press `Generate EDA Report` above to get an in-depth look at the data.')