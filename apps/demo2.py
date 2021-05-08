import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.tools as tls

def app():
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

    df2 = df[df.columns[1:]].sum(axis=0)
    rolling_windows = df2.rolling(5, min_periods=1)
    rolling_mean = rolling_windows.mean()
    #  print(rolling_mean)

    fig = plt.figure(figsize=(15,8))
    sns.barplot(df.columns[1:],df[df.columns[1:]].sum(axis=0))
    plt.plot(df.columns[1:], rolling_mean, color='red',label='moving average')
    plt.xticks(rotation='vertical')
    # st.pyplot()
    st.write(fig)
    # tls.mpl_to_plotly(fig)
    # st.write(fig)
    # st.plotly_chart(fig, use_container_width=True)


    # z = df.transpose().iloc[1:]
    # plt.figure(figsize=(20,10))
    # for cat in df['Category']:
    #     print(z[cat])
    #     plt.plot(z.index, z[cat], label=cat)
    #     plt.xticks(rotation='vertical')
    # plt.legend()