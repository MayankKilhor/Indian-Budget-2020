import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = st.cache(pd.read_csv)("Datasets/Expenditure.csv")
df["Budget 2019-2020 Total"]= df["Budget 2019-2020 Total"].replace("...", "0.00")
df['Budget 2019-2020 Total'] = pd.to_numeric(df['Budget 2019-2020 Total'])

def graph_func(option):
    data=df
    data = df[df['Ministries/Departments']=='Cabinet']
    table = pd.pivot_table(data3, values='Budget 2019-2020 Total', index='Detailed Head of Expenditure',columns='Head of Expenditure', fill_value=0)
    fig = plt.figure(figsize=(12,12))
    r = sns.heatmap(table, linewidths=1, linecolor='white')
    r.set_title("Heatmap of Flight Density from 1949 to 1961")
    st.write(fig)
