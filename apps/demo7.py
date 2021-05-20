import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px

def app():
    st.markdown("""
                    # Module 6: Healthcare Budget  
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
    df = st.cache(pd.read_csv)("Datasets/department-of-health-and-family-welfare.csv")
    is_check = st.checkbox("Display Data")
    if is_check:
        st.write(df)
    
    
    revenue = df[['Particulars', 'Actual 2017-2018 Revenue', 'Budget 2018-2019 Revenue', 'Budget 2019-2020 Revenue', ]].iloc[-1:]
    revenue.columns = ['Particulars', '2017-2018', '2018-2019', '2019-2020']
    revenue['Particulars'] = 'Revenue'

    z = df[['Particulars', 'Actual 2017-2018 Capital', 'Budget 2018-2019 Capital', 'Budget 2019-2020 Capital']].iloc[-1:]
    z.columns = ['Particulars', '2017-2018', '2018-2019', '2019-2020']
    z['Particulars'] = 'Capital'
    revenue = revenue.append(z)

    z = df[['Particulars', 'Actual 2017-2018 Total', 'Budget 2018-2019 Total', 'Budget 2019-2020 Total']].iloc[-1:]
    z.columns = ['Particulars', '2017-2018', '2018-2019', '2019-2020']
    z['Particulars'] = 'Total'
    revenue = revenue.append(z)

    z  = revenue.T 
    new_header = z.iloc[0] #grab the first row for the header
    z = z.iloc[1:] #take the data less the header row
    z.columns = new_header
    z = z.reset_index()
    st.markdown("""
                ____________________________________________________________________
                ** _ Area Line Chart _ ** - This chart shows the Revenue, Capital and Total Budget distribution in the Healthcare sector over the past three years. We see a steady rise in the amount.""")

    fig = px.area(z, x='index', y=['Revenue', 'Capital', 'Total'])
    st.plotly_chart(fig)

    st.markdown("""
                ____________________________________________________________________
                ** _ Pie Chart _ ** -  This Pie Chart explores the various subsections of the Healthcare Department and how the Budget was allocated to each of the departments.""")

    variables = st.selectbox("Enter the Column", df.columns[3:])
    df2 = df[['Particulars','Actual 2017-2018 Revenue', 'Budget 2018-2019 Revenue', 'Budget 2019-2020 Revenue','Actual 2017-2018 Capital', 'Budget 2018-2019 Capital', 'Budget 2019-2020 Capital','Actual 2017-2018 Total', 'Budget 2018-2019 Total', 'Budget 2019-2020 Total','Revised 2018-2019 Revenue','Revised 2018-2019 Capital','Revised 2018-2019 Total']].iloc[4:25, :].replace('...', np.NaN)
    df2 = df2.replace(np.NaN, 0)
    colname=    variables
    fig2 = px.pie(df2, values=colname, names=df2['Particulars'], title=colname)
    st.plotly_chart(fig2)
