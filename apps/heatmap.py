
import pandas as pd 
import streamlit as st
import plotly.graph_objects as go

df = pd.read_csv("Datasets/Expenditure.csv")
df["Budget 2019-2020 Total"]= df["Budget 2019-2020 Total"].replace("...", "0.00")
df['Budget 2019-2020 Total'] = pd.to_numeric(df['Budget 2019-2020 Total'])


def graph_func(option2):
    data=df
    data = df[df['Ministries/Departments']==str(option2)]
    table = pd.pivot_table(data, values='Budget 2019-2020 Total', index='Detailed Head of Expenditure',columns='Head of Expenditure', fill_value=0)

    fig = go.Figure(data=go.Heatmap(z=table.values, x=table.columns, y=table.index))
    fig.layout.height = 1000
    fig.layout.width = 900
    st.plotly_chart(fig)
