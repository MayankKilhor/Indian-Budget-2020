import streamlit as st
import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px


def app():

    st.markdown("""
                    # Module 1: Previous Year Analysis with 2020 Budget 
                    #
                    ## Description
                    Module 1 focuses on the year wise analysis of various department budgets ranging from year 1941- 2024 along with a detailed graph of predictive analysis for the years 2021, 2022, 2023, 2024.
                    
                    ## Inference
                    ->   Through the visualisations, A rolling mean has been set to determine the progress of the department budgets over the years which pitfalls from the year 1944 - 1950 signifying the independence and change in economic legislature, The graph plateaus from the year 1991 to 2012 with short increments every 5 years. This data represents that the economy booms in the first year of the elected governments. 
                    
                    ->   From 2009 to 2020, We can observe that National Defence has been at the forefront of the economic gains made per 1 Crore INR followed by Social Security, Veterans Benefits (in- line with OROP) and Health and Medicine sector. The lowest of the interests include Education and Energy sector with nominal gains in Transportation sector
                    
                    ->   W.R.T COVID-19 - Now, while the country is deeply affected by Covid-19 and there is a huge shortage of medical supplies everywhere, it does make us wonder that if the government had spent more on healthcare, we would have perhaps been in a better situation.
                    _______________________________________________________________________________________________
                    
                    ## DATASET
                    #####""")
    
    df = st.cache(pd.read_csv)("Datasets/FederalBudgetShares1941_2020.csv")
    is_check = st.checkbox("Display Data")
    if is_check:
        st.write(df)
    teams = st.sidebar.multiselect("Enter categoryy", df['Category'].unique())
    st.write("Your input category", teams)

    variables = st.sidebar.multiselect("Enter the variables", df.columns)
    st.write("You selected these variables", variables)

    selected_category_data = df[(df['Category'].isin(teams))]
    two_category_data = selected_category_data[variables]
    category_data_is_check = st.checkbox("Display the data of selected category")
    if category_data_is_check:
        st.write(two_category_data)

    df2 = df[df.columns[1:]].sum(axis=0)
    rolling_windows = df2.rolling(5, min_periods=1)
    rolling_mean = rolling_windows.mean()
    
    # Figure 1

    st.markdown("""
                ____________________________________________________________________
                ** _ `Bar Graph` _ ** - This Bar Graph shows how the Union Budget of India has evolved, right from 1941 upto 2021. It also makes predictions on the budget of 2024 based on previous year trends. """)
    
    z = df.transpose().iloc[1:]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=z.index,y=df[z.index].sum(axis=0),orientation='v',
            marker=dict(line=dict(color='rgb(248, 248, 249)', width=1))))
    fig.add_trace(go.Scatter(x=z.index,y=rolling_mean,name="Rolling Mean",line=dict(width=4)))

    st.plotly_chart(fig)

    # Figure 2

    z = df.transpose().iloc[72:82]
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=z.index,y=df[z.index].sum(axis=0),orientation='v',
            marker=dict(line=dict(color='rgb(248, 248, 249)', width=1))))
    fig2.add_trace(go.Scatter(x=z.index,y=rolling_mean[72:],name="Rolling Mean",line=dict(width=4)))
    st.plotly_chart(fig2)

    # Figure 3

    st.markdown("""
                ____________________________________________________________________
                ** _ `Line Chart` _ ** - This Line chart shows how the Budget has been distributed across various sectors over the last 10 years. The sector-wise distribution of the budget hasn’t changed much over the years.""")  
    fig4 = go.Figure()
    z = df.transpose().iloc[1:]

    j=0
    for i in z.index:
        # st.write(z.index)
        fig4.add_trace(go.Scatter(x=df['Category'],y=df[i],name=str(i),line=dict(width=4)))
        j=j+1
    st.plotly_chart(fig4)

    # Figure 5  
    fig5 = go.Figure()
    z = df.transpose().iloc[72:82]

    j=0
    for i in z.index:
        # st.write(z.index)
        fig5.add_trace(go.Scatter(x=df['Category'],y=df[i],name=str(i),line=dict(width=4)))
        j=j+1
    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("""
                ____________________________________________________________________
                ** _ `Pie Chart` _ ** - This chart is another visual representation of the sector wise budget representation of the Union Budget. It is a menu-driven chart which enables us to select the year whose distribution we wish to see.""")  

    variables = st.selectbox("Enter the year", df.columns)
    
    fig6 = px.pie(df, values=str(variables), names='Category')
    st.plotly_chart(fig6)