import streamlit as st
from predict_page import show_predict_page
from overview_page import show_overview_page


page = st.sidebar.selectbox("Survey Overview Or Predict Salary", ("Predict Salary", "Survey Overview"))

if page == "Predict Salary":
    show_predict_page()
else:
    show_overview_page()
    
