import streamlit as st
import numpy as np 
import pandas as pd

import json
import plotly.express as px
import plotly.io as pio
def app():
    st.markdown("""
                    # Module 4: Budget Allocations across different States 
                    #
                    ## Description
                    Module 4 has insights into the Budget allocations based on State Wise data along with Union Territories. It is of prime importance to segregate the union budget into state wise budget allocations to make sure that the viewer’s state has been allocated sufficient provisions and to be able to check progress on a unary level. 

                    
                    ## Inference
                    ->   The Choropleth Map of India shows the state wise distribution of the budget allocated to the various states and Union Territories in the country. It is to be noted that a significant amount of funds have been allocated to the state of Uttar Pradesh which is emerging as a central hub of operations for northern India followed by Maharashtra which houses cities like Mumbai, Akola, Nagpur, Pune which form the major Economic zone for the country as well as international trade.
                    
                    ->   The least funds are allocated to the Seven Sister states, The Union Territory of Jammu and Kashmir followed by communal Kerala.
                    
                    ->   The pie chart gives a percentage analysis of the State Wise budget allocation

                    ->   It is to be noted that the government focus is on least developed states such as Uttar Pradesh, Bihar, West Bengal. 
                    _______________________________________________________________________________________________
                    
                    ## DATASET
                    #####""")
    df = pd.read_csv("Datasets/state_budget.csv")
    is_check = st.checkbox("Display Data")
    if is_check:
        st.write(df)
    category = st.sidebar.multiselect("Enter State", df['State'].unique())
    st.write("Your input State", category)

    variables = st.sidebar.multiselect("Enter the variables", df.columns)
    st.write("You selected these variables", variables)

    selected_category_data = df[(df['State'].isin(category))]
    two_category_data = selected_category_data[variables]
    category_data_is_check = st.checkbox("Display the data of selected State")
    if category_data_is_check:
        st.write(two_category_data)

    st.markdown("""
                ____________________________________________________________________
                ** _ Choropleth Map _ ** - This choropleth map showing  state- wise budget of all the states in India.""")

    pio.renderers.default = 'browser'
    india_states = json.load(open("Datasets/states_india.geojson", "r"))
    state_id_map = {}
    for feature in india_states["features"]:
        feature["id"] = feature["properties"]["state_code"]
        state_id_map[feature["properties"]["st_nm"]] = feature["id"]
    df2=df.copy()
    df2["Budget(In Crores)"]= df2["Budget(In Crores)"].replace("TBA", "0")
    df2["Budget(In Crores)"] = df2["Budget(In Crores)"].apply(lambda x: int(x.split("/")[0].replace(",", "")))
    df2["id"] = df2["State"].apply(lambda x: state_id_map[x])
    fig = px.choropleth(
    df2,
    locations="id",
    geojson=india_states,
    color="Budget(In Crores)",
    hover_name="State",
    hover_data=["Budget(In Crores)"],
    title="India State Budget 2020",
    )
    fig.update_geos(fitbounds="locations", visible=False)

    st.plotly_chart(fig)

    st.markdown("""
                ____________________________________________________________________
                ** _ Pie Chart _ ** - This chart is another visual representation of the state wise budget distribution. It is a menu-driven chart which enables us to select the year whose distribution we wish to see.""")

    fig2 = px.pie(df2, values='Budget(In Crores)', names='State', hole=.5)
    st.plotly_chart(fig2)

    df3=df2.sort_values(by="Budget(In Crores)",ascending=False)

    st.markdown("""
                ____________________________________________________________________
                ** _ Ordered Bar Chart _ ** - We created a bar chart to show the comparison of budgets in different states.""")

    fig3 = px.bar(df3, x="State", y="Budget(In Crores)", color="Budget(In Crores)", title="India State Budget 2020")
    st.plotly_chart(fig3)