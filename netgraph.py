import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.traversal.depth_first_search import dfs_edges

import pyvis
from pyvis import physics
from pyvis.network import Network
import pandas as pd
from pyvis.physics import Physics
import streamlit as st

df = st.cache(pd.read_csv)("Datasets/Expenditure.csv")



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
