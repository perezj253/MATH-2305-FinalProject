import networkx as nx

def cost(G, e):
    return G.edges()[e[0], e[1]]['weight']

def readGraphFromFile(user_choice):
    """

    Parameters
    ----------
    user_choice : int
        user choice to implement Prim's algorithm to find MST of the graph

    Returns
    -------
    G : Graph()
        returns an undirected weigthed edgelist from the selected graph
    """
    
    if user_choice == 1:
        graph_data = open("G1.txt", 'r')
    elif user_choice == 2:
        graph_data = open("test-graphs/G2.txt", 'r')
    else:
        graph_data = open("test-graphs/G3.txt", 'r')
        
    G = nx.read_weighted_edgelist(graph_data, nodetype = int)
                
    return G
                
                
            
            
def V(graph):
    return set(graph.nodes())

def E(graph):
    return set(graph.edges())

def prims_initialize(graph, v):
    if v not in V(graph):
        return 'Error vertex not found'
    else:
        T = nx.Graph()
        T.add_node(v)
    return T

def is_spanning(graph, subgraph):
    return V(graph) == V(subgraph)
        

def possible_edges(G, T):
    """
    Parameters
    ----------
    G: graph()
        user specified graph
    T: graph()
        Minimum spanning tree of the user specified weighted graph
    Returns
    -------
    list of possible edges
    """
    list(G.edges(V(T)))
    return [e for e in list(G.edges(V(T))) 
             if e[0] not in V(T) or e[1] not in V(T)]

def min_cost_edge(G, T):
    temp_edges = possible_edges(G, T)
    min_cost_edge = temp_edges[0]
    
    for e in temp_edges:
        if cost(G, min_cost_edge) > cost(G, e):
            min_cost_edge = e
            
    return min_cost_edge
    
