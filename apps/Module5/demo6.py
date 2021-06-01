import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px

def app():
    st.markdown("""
                    # Module 5: Tax Distribution  
                    #
                    ## Description
                    The distribution of of Tax revenue in line with the Goods and Services Tax introduced in 2017 and fully implemented in 2018 gives a varied visualisation of the amount of economic zones in the country, how well the government over the years has managed to gain interest and tax revenue and future planning of development zones within states can be easily measured with this insight along with Custom duties levied as well as Union Excise duties while moving from state to state.
                    
                    ## Inference
                    ->   Basic duties which range from 3% up to 24% make the highest amount of cess that is levied on goods as well as essential products ranging over 1,00,000 Crore INR
                    
                    ->   The National Calamity Contingency sees the least amount of custom levied as it is a Branch that focuses on War time aid and National Disaster Recovery Plans, hence such goods are exempted from taxation.
                    
                    ->   The Union levies excise duties on Crude Oil as India imports most of its oil from abroad and would be detrimental to the country if tax is levied on crude oil as it accounts for over 80% of energy and 97% of transportation needs.

                    ->   However there is a high duty levied on non essentials such as Vehicles, Spirits and High Speed railways as they are seen as a commodity and not a necessity.
                    _______________________________________________________________________________________________
                    
                    ## DATASET
                    #####""")
    df = st.cache(pd.read_csv)("Datasets/tax_revenue.csv")
    is_check = st.checkbox("Display Data")
    if is_check:
        st.write(df)
    category = st.sidebar.multiselect("Enter categoryy", df['Tax Category'].unique())
    st.write("Your input category", category)

    variables = st.sidebar.multiselect("Enter the variables", df.columns)
    st.write("You selected these variables", variables)

    selected_category_data = df[(df['Tax Category'].isin(category))]
    two_category_data = selected_category_data[variables]
    category_data_is_check = st.checkbox("Display the data of selected category")
    if category_data_is_check:
        st.write(two_category_data)
    df2=df.copy()
    df2 = df2.replace('...', np.NaN)
    df2 = df2.dropna()
    # print(df)
    df2[['Actual 2018-2019', 'Budget 2019-2020', 'Revised 2019-2020', 'Budget 2020-2021']] = df2[['Actual 2018-2019', 'Budget 2019-2020', 'Revised 2019-2020', 'Budget 2020-2021']].apply(pd.to_numeric)
   
    st.markdown("""
                ____________________________________________________________________
                ** _ `Line Plot` _ ** - This line plot shows the sector- wise distribution of the Budget, with different colours of the line showing the Category of Tax where the money has come from. """)

    fig = px.line(df2, x="Tax Particular", y="Budget 2020-2021", color='Tax Category')
    fig.layout.height = 700
    fig.layout.width = 900
    st.plotly_chart(fig)

    st.markdown("""
                ____________________________________________________________________
                ** _ `Scatter Matrix` _ ** - This visualization shows the comparison with a scatterplot of the Budget of three years and gives a colour encoding according to the Category of Taxes.""")

    fig2 = px.scatter_matrix(df2, dimensions=['Actual 2018-2019', 'Budget 2019-2020', 'Budget 2020-2021'], color="Tax Category")
    fig2.layout.height = 700
    fig2.layout.width = 900
    st.plotly_chart(fig2)

    st.markdown("""
                ____________________________________________________________________
                ** _ `Stacked Bar chart` _ ** - This Stacked Bar Chart  gives the count of each Tax Category with each of the Stacks showing the Tax Particular where it has been derived from.""")
    fig3 = px.histogram(df2, x="Tax Category", color="Tax Particular")
    fig3.layout.height = 700
    fig3.layout.width = 900
    st.plotly_chart(fig3)