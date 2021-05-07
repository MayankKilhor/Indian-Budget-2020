import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


df = st.cache(pd.read_csv)("FederalBudgetShares1941_2020.csv")
is_check = st.checkbox("Display Data")
if is_check:
    st.write(df)
teams = st.sidebar.multiselect("Enter categoryy", df['Category'].unique())
st.write("Your input category", teams)

variables = st.sidebar.multiselect("Enter the variables", df.columns)
st.write("You selected these variables", variables)

selected_category_data = df[(df['Category'].isin(teams))]
two_category_data = selected_category_data[variables]
category_data_is_check = st.checkbox("Display the data of selected category")
if category_data_is_check:
    st.write(two_category_data)



# z = df.transpose().iloc[1:]
# plt.figure(figsize=(20,10))
# for cat in df['Category']:
#     print(z[cat])
#     plt.plot(z.index, z[cat], label=cat)
#     plt.xticks(rotation='vertical')
# plt.legend()