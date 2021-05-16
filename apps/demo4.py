import numpy as np 
import pandas as pd
import streamlit as st 
import streamlit.components.v1 as components
import netgraph
import heatmap

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
    
    # physics1=st.checkbox('add physics interactivity?')
    # netgraph.All_func(physics1)
    # HtmlFile = open("All.html", 'r', encoding='utf-8')
    # source_code = HtmlFile.read() 
    # components.html(source_code, height = 500,width=700)


    option=st.selectbox('select graph',('Andaman and Nicobar Islands','Atomic Energy', 'Cabinet','Capital Outlay on Defence Services','Central Vigilance Commission','Chandigarh','Dadra and Nagar Haveli and Daman and Diu'))
    # physics=st.checkbox('add physics interactivity?')
    netgraph.graph_func(option)
    HtmlFile = open("Graph.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height = 500,width=500)
    
    # physics1=st.checkbox('add physics interactivity?  ')
    netgraph.graph2_func(option)
    HtmlFile = open("Graph2.html", 'r', encoding='utf-8')
    source_code2 = HtmlFile.read() 
    components.html(source_code2, height = 500,width=500)

    option2=st.selectbox('select graph',('Andaman and Nicobar Islands','Atomic Energy', 'Cabinet','Capital Outlay on Defence Services','Central Vigilance Commission','Chandigarh','Dadra and Nagar Haveli and Daman and Diu'))
    heatmap.graph_func(option2)
    

    