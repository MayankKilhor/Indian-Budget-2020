import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px

def app():
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
   
    fig = px.line(df2, x="Tax Particular", y="Budget 2020-2021", color='Tax Category')
    st.plotly_chart(fig)

    fig2 = px.scatter_matrix(df2, dimensions=['Actual 2018-2019', 'Budget 2019-2020', 'Budget 2020-2021'], color="Tax Category")
    st.plotly_chart(fig2)

    fig3 = px.histogram(df2, x="Tax Category", color="Tax Particular")
    st.plotly_chart(fig3)