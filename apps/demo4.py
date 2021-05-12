import numpy as np 
import pandas as pd
import streamlit as st 
import streamlit.components.v1 as components
import netgraph


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


    option2=st.selectbox('select graph',('Andaman and Nicobar Islands','Atomic Energy', 'Cabinet','Capital Outlay on Defence Services','Central Vigilance Commission','Chandigarh','Dadra and Nagar Haveli and Daman and Diu'))
    # physics=st.checkbox('add physics interactivity?')
    netgraph.graph_func(option2)
    HtmlFile = open("Graph.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height = 500,width=500)
    
    # physics1=st.checkbox('add physics interactivity?  ')
    netgraph.graph2_func(option2)
    HtmlFile = open("Graph2.html", 'r', encoding='utf-8')
    source_code2 = HtmlFile.read() 
    components.html(source_code2, height = 500,width=500)
    
    # option=st.selectbox('select graph',('Andaman and Nicobar Islands','Atomic Energy', 'Cabinet','Capital Outlay on Defence Services','Central Vigilance Commission','Chandigarh','Dadra and Nagar Haveli and Daman and Diu'))
    # 

    # netgraph.Andaman_func(physics)
physics=st.checkbox('add physics interactivity?')
    # # Andaman and Nicobar Islands
    # if option=='Andaman and Nicobar Islands':
    #     HtmlFile = open("Andaman_and_Nicobar_Islands.html", 'r', encoding='utf-8')
    #     source_code = HtmlFile.read() 
    #     components.html(source_code, height = 1000,width=900)

    # netgraph.Atomic_func(physics)
    # # Atomic Energy
    # if option=='Atomic Energy':
    #     HtmlFile = open("Atomic_Energy.html", 'r', encoding='utf-8')
    #     source_code = HtmlFile.read() 
    #     components.html(source_code, height = 900,width=900)

    # netgraph.Cabinet_func(physics)
    # # Cabinet
    # if option=='Cabinet':
    #     HtmlFile = open("Cabinet.html", 'r', encoding='utf-8')
    #     source_code = HtmlFile.read() 
    #     components.html(source_code, height = 900,width=900)

    # netgraph.Capital_Outlay_func(physics)
    # # Capital Outlay on Defence Services
    # if option=='Capital Outlay on Defence Services':
    #     HtmlFile = open("Capital_Outlay_on_Defence_Services.html", 'r', encoding='utf-8')
    #     source_code = HtmlFile.read() 
    #     components.html(source_code, height = 900,width=900)

    # netgraph.Central_Vigilance_func(physics)
    # # Central Vigilance Commission
    # if option=='Central Vigilance Commission':
    #     HtmlFile = open("Central_Vigilance_Commission.html", 'r', encoding='utf-8')
    #     source_code = HtmlFile.read() 
    #     components.html(source_code, height = 900,width=900)

    # netgraph.Chandigarh_func(physics)
    # # Chandigarh
    # if option=='Chandigarh':
    #     HtmlFile = open("Chandigarh.html", 'r', encoding='utf-8')
    #     source_code = HtmlFile.read() 
    #     components.html(source_code, height = 900,width=900)

    # netgraph.Dadra_func(physics)
    # # Dadra and Nagar Haveli and Daman and Diu
    # if option=='Dadra and Nagar Haveli and Daman and Diu':
    #     HtmlFile = open("Dadra_and_Nagar_Haveli_and_Daman_and_Diu.html", 'r', encoding='utf-8')
    #     source_code = HtmlFile.read() 
    #     components.html(source_code, height = 900,width=900)
    