import streamlit as st
from PIL import Image

def app():

    st.markdown(""" # Survey
    To get a clear understanding of the User Requirements of our web application, we created a Google Form and surveyed people of various age groups and occupations.From the responses obtained from the form, we could summarise 8 major user requirements of our website, and we designed and developed our website on that basis.

    ## User Requirements:
        1) Attractive UI

        2) Previous year comparison of Budget

        3) Interactivity

        4) Options to Filter or Search for data according to requirements

        5) Menu Driven website

        6) Responsive across Multiple devices/ Screen sizes

        7) Easy comparison of Data

        8) Choropleth map of india to show state wise budget
    """,True)

    img = Image.open('Datasets/s1.jfif')
    st.image(img)
    img2 = Image.open('Datasets/s2.jfif')
    st.image(img2)
    img3 = Image.open('Datasets/s3.jfif')
    st.image(img3)
    img4 = Image.open('Datasets/s4.jfif')
    st.image(img4)
    img5 = Image.open('Datasets/s5.jfif')
    st.image(img5)
    img6 = Image.open('Datasets/s6.jfif')
    st.image(img6)
    img7 = Image.open('Datasets/s7.jfif')
    st.image(img7)
    img8 = Image.open('Datasets/s8.jfif')
    st.image(img8)

    
