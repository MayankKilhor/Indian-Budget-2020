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
    st.write(fig)
 
    # Figure 2

    z = df.transpose().iloc[1:]
    fig4 = go.Figure()
    fig4.add_trace(go.Bar(x=z.index,y=df[z.index].sum(axis=0),orientation='v',
            marker=dict(line=dict(color='rgb(248, 248, 249)', width=1))))
    fig4.add_trace(go.Scatter(x=z.index,y=rolling_mean,name="Rolling Mean",line=dict(width=4)))

    st.plotly_chart(fig4)

    # Figure 3
    colors = ['rgba(38, 24, 74, 0.8)', 'rgba(71, 58, 131, 0.8)',
          'rgba(122, 120, 168, 0.8)', 'rgba(164, 163, 204, 0.85)',
          'rgba(190, 192, 213, 1)']

    z = df.transpose().iloc[72:82]
    fig3 = go.Figure()
    fig3.add_trace(go.Bar(x=z.index,y=df[z.index].sum(axis=0),orientation='v',
            marker=dict(line=dict(color='rgb(248, 248, 249)', width=1))))
    fig3.add_trace(go.Scatter(x=z.index,y=rolling_mean[72:],name="Rolling Mean",line=dict(width=4)))
    st.plotly_chart(fig3)

    # Figure 4  
    fig5 = go.Figure()
    z = df.transpose().iloc[1:]

    j=0
    for i in z.index:
        # st.write(z.index)
        fig5.add_trace(go.Scatter(x=df['Category'],y=df[i],name=str(i),line=dict(width=4)))
        j=j+1
    st.plotly_chart(fig5)

    # Figure 5  
    fig2 = go.Figure()
    z = df.transpose().iloc[72:82]

    j=0
    for i in z.index:
        # st.write(z.index)
        fig2.add_trace(go.Scatter(x=df['Category'],y=df[i],name=str(i),line=dict(width=4)))
        j=j+1
    st.plotly_chart(fig2, use_container_width=True)

    variables = st.selectbox("Enter the year", df.columns)
    st.write("You selected these variables", variables)
    
    fig6 = px.pie(df, values=str(variables), names='Category')
    st.plotly_chart(fig6)