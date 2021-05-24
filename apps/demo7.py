import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px

def app():
    st.markdown("""
                    # Module 6: Healthcare Budget  
                    #
                    ## Description
                    The main reason for focusing on Healthcare budget is to better analyse how the government has been allocated budget for healthcare. Post Pandemic the economy had gone into a spiral with India noting first ever Quarterly fall and prediction of -9% decrement in the GDP, Hence to recover economy as well as making sure that India comes out stronger from the pandemic it is of utmost importance to see how well the Healthcare sector is doing and how 2021 budget shall be allocated funds in order to tackle the global pandemic situation.

                    
                    ## Inference
                    ->   Over the last three years 2018, 2019, 2020 we can observe that the budget allocation has incremented from 51,000 Crore INR to 62,000 Crore INR. A net increase of almost 10,000 Crore INR. This is however in contrast with the amount spent on the Education sector as well as the Transportation sector.
                    
                    ->   A country of 135 Billion with the modern statistics showing that we have 1 Doctor for over 50 people is an alarming number.
                    
                    ->   Most of the Healthcare budget has been spent on acquisition of modern technology machines such as MRI machines, Few have been allocated to the building of new hospitals.

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
                ** _ `Area Line Chart` _ ** - This chart shows the Revenue, Capital and Total Budget distribution in the Healthcare sector over the past three years. We see a steady rise in the amount.""")

    fig = px.area(z, x='index', y=['Revenue', 'Capital', 'Total'])
    st.plotly_chart(fig)

    st.markdown("""
                ____________________________________________________________________
                ** _ `Pie Chart` _ ** -  This Pie Chart explores the various subsections of the Healthcare Department and how the Budget was allocated to each of the departments.""")

    variables = st.selectbox("Enter the Column", df.columns[3:])
    df2 = df[['Particulars','Actual 2017-2018 Revenue', 'Budget 2018-2019 Revenue', 'Budget 2019-2020 Revenue','Actual 2017-2018 Capital', 'Budget 2018-2019 Capital', 'Budget 2019-2020 Capital','Actual 2017-2018 Total', 'Budget 2018-2019 Total', 'Budget 2019-2020 Total','Revised 2018-2019 Revenue','Revised 2018-2019 Capital','Revised 2018-2019 Total']].iloc[4:25, :].replace('...', np.NaN)
    df2 = df2.replace(np.NaN, 0)
    colname=    variables
    fig2 = px.pie(df2, values=colname, names=df2['Particulars'], title=colname)
    st.plotly_chart(fig2)
