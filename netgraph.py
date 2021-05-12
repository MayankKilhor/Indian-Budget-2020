import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.traversal.depth_first_search import dfs_edges
from pyvis import physics
from pyvis.network import Network
import pandas as pd
from pyvis.physics import Physics
import streamlit as st

df = st.cache(pd.read_csv)("Datasets/Expenditure.csv")

import pyvis

def graph_func(option2):
    df1 = df[df['Ministries/Departments']==str(option2)]
    G = nx.from_pandas_edgelist(df1, 
                            source = 'Ministries/Departments',
                            target ='Head of Expenditure',
                            edge_attr='Budget 2019-2020 Total')
    from pyvis.network import Network
    nt = Network(notebook = True)

    nt.from_nx(G)
    if physics:
        nt.show_buttons(filter_=['physics'])
    nt.show("Graph.html")

def graph2_func(option2):
    df1 = df[df['Ministries/Departments']==str(option2)]
    G = nx.from_pandas_edgelist(df1, 
                            source = 'Ministries/Departments',
                            target ='Detailed Head of Expenditure',
                            edge_attr='Budget 2019-2020 Total')
    from pyvis.network import Network
    nt = Network(notebook = True)

    nt.from_nx(G)
    if physics1:
        nt.show_buttons(filter_=['physics'])
    nt.show("Graph2.html")

def All_func(physics1):
    G = nx.from_pandas_edgelist(df, 
                            source = 'Head of Expenditure',
                            target ='Detailed Head of Expenditure',
                            edge_attr='Budget 2019-2020 Total')
    from pyvis.network import Network
    nt = Network(notebook = True)

    nt.from_nx(G)
    
    if physics1:
        nt.show_buttons(filter_=['physics'])
    nt.show("All.html")

# def Andaman_func(physics):
#     # Andaman and Nicobar Islands
#     df1 = df[df['Ministries/Departments']=='Andaman and Nicobar Islands']
#     G1 = nx.from_pandas_edgelist(df1, 
#                             source = 'Ministries/Departments',
#                             target ='Detailed Head of Expenditure',
#                             edge_attr='Budget 2019-2020 Total')
#     net = Network("500px", "500px",notebook = True)
#     net.from_nx(G1)
#     if physics:
#         net.show_buttons(filter_=['physics'])
#     net.show("Andaman_and_Nicobar_Islands.html")

# def Atomic_func(physics):

#     # Atomic Energy
#     df2 = df[df['Ministries/Departments']=='Atomic Energy']
#     G2 = nx.from_pandas_edgelist(df2, 
#                             source = 'Ministries/Departments',
#                             target ='Detailed Head of Expenditure',
#                             edge_attr='Budget 2019-2020 Total')
#     net = Network(notebook = True)
#     net.from_nx(G2)
#     if physics:
#         net.show_buttons(filter_=['physics'])
#     net.show("Atomic_Energy.html")

# def Cabinet_func(physics):
#     # Cabinet
#     df3 = df[df['Ministries/Departments']=='Cabinet']
#     G3 = nx.from_pandas_edgelist(df3, 
#                             source = 'Ministries/Departments',
#                             target ='Detailed Head of Expenditure',
#                             edge_attr='Budget 2019-2020 Total')
#     net = Network(notebook = True)
#     net.from_nx(G3)
#     if physics:
#         net.show_buttons(filter_=['physics'])
#     net.show("Cabinet.html")

# def Capital_Outlay_func(physics):

#     # Capital Outlay on Defence Services
#     df4 = df[df['Ministries/Departments']=='Capital Outlay on Defence Services']
#     G4= nx.from_pandas_edgelist(df4, 
#                             source = 'Ministries/Departments',
#                             target ='Detailed Head of Expenditure',
#                             edge_attr='Budget 2019-2020 Total')
#     net = Network(notebook = True)
#     net.from_nx(G4)
#     if physics:
#         net.show_buttons(filter_=['physics'])
#     net.show("Capital_Outlay_on_Defence_Services.html")

# def Central_Vigilance_func(physics):

#     #Central Vigilance Commission
#     df5 = df[df['Ministries/Departments']=='Central Vigilance Commission']
#     G5 = nx.from_pandas_edgelist(df5, 
#                             source = 'Ministries/Departments',
#                             target ='Detailed Head of Expenditure',
#                             edge_attr='Budget 2019-2020 Total')
#     net = Network(notebook = True)
#     net.from_nx(G5)
#     if physics:
#         net.show_buttons(filter_=['physics'])
#     net.show("Central_Vigilance_Commission.html")

# def Chandigarh_func(physics):
#     # Chandigarh
#     df6 = df[df['Ministries/Departments']=='Chandigarh']
#     G6 = nx.from_pandas_edgelist(df6, 
#                             source = 'Ministries/Departments',
#                             target ='Detailed Head of Expenditure',
#                             edge_attr='Budget 2019-2020 Total')
#     net = Network(notebook = True)
#     net.from_nx(G6)
#     if physics:
#         net.show_buttons(filter_=['physics'])
#     net.show("Chandigarh.html")

# def Dadra_func(physics):
#     # Dadra and Nagar Haveli and Daman and Diu
#     df7 = df[df['Ministries/Departments']=='Dadra and Nagar Haveli and Daman and Diu']
#     G7 = nx.from_pandas_edgelist(df7, 
#                             source = 'Ministries/Departments',
#                             target ='Detailed Head of Expenditure',
#                             edge_attr='Budget 2019-2020 Total')
#     net = Network(notebook = True)
#     net.from_nx(G7)
#     if physics:
#         net.show_buttons(filter_=['physics'])
#     net.show("Dadra_and_Nagar_Haveli_and_Daman_and_Diu.html")