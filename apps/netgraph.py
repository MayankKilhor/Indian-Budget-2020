import networkx as nx
from pyvis.network import Network
import pandas as pd

df4 = pd.read_csv("Datasets/Expenditure.csv")



def graph_func(option2):
    df1 = df4[df4['Ministries/Departments']==str(option2)]
    G = nx.from_pandas_edgelist(df1, 
                            source = 'Ministries/Departments',
                            target ='Head of Expenditure',
                            edge_attr='Budget 2019-2020 Total')
    nt = Network(notebook = True)

    nt.from_nx(G)
    nt.show("Graph.html")

def graph2_func(option2):
    df1 = df4[df4['Ministries/Departments']==str(option2)]
    G = nx.from_pandas_edgelist(df1, 
                            source = 'Ministries/Departments',
                            target ='Detailed Head of Expenditure',
                            edge_attr='Budget 2019-2020 Total')
    nt = Network(notebook = True)

    nt.from_nx(G)

    nt.show("Graph2.html")

def All_func(physics1):
    G = nx.from_pandas_edgelist(df4, 
                            source = 'Head of Expenditure',
                            target ='Detailed Head of Expenditure',
                            edge_attr='Budget 2019-2020 Total')
    nt = Network(notebook = True)

    nt.from_nx(G)
    
    if physics1:
        nt.show_buttons(filter_=['physics'])
    nt.show("All.html")
