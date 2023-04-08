
import streamlit as st
view = [100,150]
st.write('# My first ChatBot')
st.write('## raw')
view
st.write('## bar_chart')
st.bar_chart(view)
import pandas as pd 
sview = pd.Series (view)
sview