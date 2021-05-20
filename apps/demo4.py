import numpy as np 
import pandas as pd
import streamlit as st 
import streamlit.components.v1 as components
from apps import netgraph
from apps import heatmap
from apps import bubblechart

def app():
    st.markdown("""
                    # Module 3: Department- wise Budget Expenditure Allocation 
                    #
                    ## Description
                    This module focuses mainly on the various ministries and departments in the budget allocation and represents information that is descriptive of the interest levied onto these ministries. 
                    
                    ## Inference
                    ->   Force directed graphs have been used to identify all the departments and ministries that gain interest from the budget allocations levied onto them, not only giving us a clue at the sheer number of sub groups but also what goes where
                    
                    ->   It is to be noted that Union Territories perform higher in this regard as the geographical landscape followed by tourism as well as faster development rate signifies growth in sectors such as Shipping, Healthcare, Power. The revised budget has just 2 instances where a significant change is made. - 1) Central Vigilance Commission 2) Defence pensions
                    
                    ->   A stark contrast can be seen in the heatmap where over 2000 Crore has been spent on Other Establishments which shows the government wishes to spend a good amount on payments and obtaining more capital.
                    _______________________________________________________________________________________________
                    
                    ## DATASET
                    #####""")
    df = pd.read_csv("Datasets/Expenditure.csv")
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
    
    st.markdown("""
                ____________________________________________________________________ """)

    option=st.selectbox('Select Ministries/Department',('Andaman and Nicobar Islands','Atomic Energy', 'Cabinet','Capital Outlay on Defence Services','Central Vigilance Commission','Chandigarh','Dadra and Nagar Haveli and Daman and Diu'))
    st.markdown("""
                ____________________________________________________________________
                ** _ Network Graph _ ** - This graph is a network of ministries/departments and nodes are Head of expenditure.""")
    netgraph.graph_func(option)
    HtmlFile = open("Graph.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height = 500,width=500)
    
    st.markdown("""
                ____________________________________________________________________
                ** _ Network Graph _ ** - This graph is a network of ministries/departments and nodes are Detailed Head of expenditure.""")

    netgraph.graph2_func(option)
    HtmlFile = open("Graph2.html", 'r', encoding='utf-8')
    source_code2 = HtmlFile.read() 
    components.html(source_code2, height = 500,width=500)

    st.markdown("""
                ____________________________________________________________________
                ** _ Heat Map _ ** - This heat map enables users to select a particular ministry and view the data.  x and y axis represent the head of expenditure and detailed head of expenditure respectively.""")
    heatmap.graph_func(option)
    
    st.markdown("""
                ____________________________________________________________________
                ** _ Bubble Plot _ ** - This is the bubble plot of each department's total budget. The x-axis represents the actual budget and the y axis represents the revised budget of 2019-2020.""")
    bubblechart.func_app()
    