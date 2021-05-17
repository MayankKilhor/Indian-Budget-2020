import streamlit as st
from multiapp import MultiApp
from apps import home, demo1, demo2, demo3, demo4, demo5 # import your app modules here

app = MultiApp()

st.markdown("""
# Multi-Page App

This multi-page app is made by Mayank Kilhor

""")

# Add all your application here
app.add_app("Home", home.app)

app.add_app("Demo1", demo1.app)
app.add_app("Demo2", demo2.app)
app.add_app("Demo3", demo3.app)
app.add_app("Demo4", demo4.app)
app.add_app("Demo5", demo5.app)
# The main app
app.run()
