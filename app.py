import streamlit as st
from multiapp import MultiApp
from apps import home, demo1
from apps.Module1 import demo2
from apps.Module2 import demo3
from apps.Module3 import demo4
from apps.Module4 import demo5
from apps.Module5 import demo6
from apps.Module6 import demo7

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
