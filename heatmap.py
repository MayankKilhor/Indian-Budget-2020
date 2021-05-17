import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.graph_objects as go

df = pd.read_csv("Datasets/Expenditure.csv")
df["Budget 2019-2020 Total"]= df["Budget 2019-2020 Total"].replace("...", "0.00")
df['Budget 2019-2020 Total'] = pd.to_numeric(df['Budget 2019-2020 Total'])


def graph_func(option2):
    data=df
    data = df[df['Ministries/Departments']==str(option2)]
    table = pd.pivot_table(data, values='Budget 2019-2020 Total', index='Detailed Head of Expenditure',columns='Head of Expenditure', fill_value=0)
    fig = plt.figure(figsize=(12,12))
    r = sns.heatmap(table, linewidths=1, linecolor='white')
    r.set_title("Heatmap of "+str(option2))
    st.write(fig)

    fig2 = go.Figure(data=go.Heatmap(z=table.values, x=table.columns, y=table.index))
    fig2.layout.height = 1000
    fig2.layout.width = 1000
    st.plotly_chart(fig2)
