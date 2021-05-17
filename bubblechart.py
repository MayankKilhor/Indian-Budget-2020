import numpy as np 
import pandas as pd
from bubbly.bubbly import bubbleplot 
import streamlit as st

# from chart_studio.plotly import plot, iplot
from plotly.offline import init_notebook_mode, iplot


df = pd.read_csv('Datasets/Expenditure.csv')
df["Actual 2018-2019 Total"]= df["Actual 2018-2019 Total"].replace("...", "0.00")
df["Budget 2019-2020 Total"]= df["Budget 2019-2020 Total"].replace("...", "0.00")
df["Revised 2019-2020 Total"]= df["Revised 2019-2020 Total"].replace("...", "0.00")
df["Budget 2020-2021 Total"]= df["Budget 2020-2021 Total"].replace("...", "0.00")
df['Actual 2018-2019 Total'] = pd.to_numeric(df['Actual 2018-2019 Total'])
df['Budget 2019-2020 Total'] = pd.to_numeric(df['Budget 2019-2020 Total'])
df['Revised 2019-2020 Total'] = pd.to_numeric(df['Revised 2019-2020 Total'])
df['Budget 2020-2021 Total'] = pd.to_numeric(df['Budget 2020-2021 Total'])
df2= df.groupby('Ministries/Departments',as_index=False).sum()

def func_app():
    figure = bubbleplot(dataset=df2, x_column='Budget 2019-2020 Total', y_column='Revised 2019-2020 Total', 
    bubble_column='Ministries/Departments',x_title="Budget 2019-2020 Total", y_title="Revised 2019-2020 Total",color_column="Ministries/Departments", title='Gapminder Global Indicators', x_logscale=True, y_logscale=True,scale_bubble=1.8, height=650,width=1000)
    st.plotly_chart(figure)
    # iplot(figure)