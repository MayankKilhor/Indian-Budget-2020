import numpy as np 
import pandas as pd
import streamlit as st 

def app():
    df = st.cache(pd.read_csv)("Datasets/Expenditure.csv")
    is_check = st.checkbox("Display Data")
    if is_check:
        st.write(df)
    teams = st.sidebar.multiselect("Enter Ministries/Departments", df['Ministries/Departments'].unique())
    st.write("Your input Ministries/Departments", teams)

    variables = st.sidebar.multiselect("Enter the variables", df.columns)
    st.write("You selected these variables", variables)

    selected_category_data = df[(df['Ministries/Departments'].isin(teams))]
    two_category_data = selected_category_data[variables]
    category_data_is_check = st.checkbox("Display the data of selected Ministries/Departments")
    if category_data_is_check:
        st.write(two_category_data)