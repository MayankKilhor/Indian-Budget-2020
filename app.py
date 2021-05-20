import streamlit as st
from multiapp import MultiApp
from apps import home, demo1, demo2, demo3, demo4, demo5, demo6, demo7 # import your app modules here

app = MultiApp()

st.markdown("""
# Indian Budget 2020 Analysis
""")

# Add all your application here
app.add_app("Home", home.app)

app.add_app("Online Survey", demo1.app)
app.add_app("Previous Year Analysis with 2020 Budget", demo2.app)
app.add_app("Budget Speech Text Visualization ", demo3.app)
app.add_app("Department- wise Budget Expenditure Allocation", demo4.app)
app.add_app("Budget Allocations across different States", demo5.app)
app.add_app("Tax Distribution ", demo6.app)
app.add_app("Healthcare Budget", demo7.app)
# The main app
app.run()
