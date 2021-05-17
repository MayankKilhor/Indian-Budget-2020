import streamlit as st

def app():
    import numpy as np 
    import pandas as pd
    import json
    import plotly.express as px
    import plotly.io as pio
    pio.renderers.default = 'browser'
    india_states = json.load(open("Datasets/states_india.geojson", "r"))
    state_id_map = {}
    for feature in india_states["features"]:
        feature["id"] = feature["properties"]["state_code"]
        state_id_map[feature["properties"]["st_nm"]] = feature["id"]
    df = pd.read_csv("Datasets/state_budget.csv")
    df["Budget(In Crores)"]= df["Budget(In Crores)"].replace("TBA", "0")
    df["Budget(In Crores)"] = df["Budget(In Crores)"].apply(lambda x: int(x.split("/")[0].replace(",", "")))
    df["id"] = df["State"].apply(lambda x: state_id_map[x])
    fig = px.choropleth(
    df,
    locations="id",
    geojson=india_states,
    color="Budget(In Crores)",
    hover_name="State",
    hover_data=["Budget(In Crores)"],
    title="India State Budget 2020",
    )
    fig.update_geos(fitbounds="locations", visible=False)

    st.plotly_chart(fig)

    fig2 = px.pie(df, values='Budget(In Crores)', names='State')
    st.plotly_chart(fig2)