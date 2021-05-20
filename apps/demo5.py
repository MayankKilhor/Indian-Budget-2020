import streamlit as st
import numpy as np 
import pandas as pd

import json
import plotly.express as px
import plotly.io as pio
def app():
    
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

    fig2 = px.pie(df2, values='Budget(In Crores)', names='State', hole=.5)
    st.plotly_chart(fig2)

    df3=df2.sort_values(by="Budget(In Crores)",ascending=False)

    fig3 = px.bar(df3, x="State", y="Budget(In Crores)", color="Budget(In Crores)", title="India State Budget 2020")
    st.plotly_chart(fig3)