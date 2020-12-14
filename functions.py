import networkx as nx

def cost(G, e):
    """
    Parameters
    ----------
    G : Graph
        Undirected graph
    e : tuple
        edge withing G

    Returns
    -------
    Type : int
        Weight of the specified edge.
    """
    return G.edges()[e[0], e[1]]['weight']

def readGraphFromFile(user_choice):
    """
    Parameters
    ----------
    user_choice : int
        User choice to implement Prim's algorithm to find MST of the graph

    Returns
    -------
    G : Graph()
        returns an undirected weigthed edgelist from the selected list of graphs
    """
    if user_choice == 1:
        graph_data = open("test-graphs/G1.txt", 'r')
    elif user_choice == 2:
        graph_data = open("test-graphs/G2.txt", 'r')
    else:
        graph_data = open("test-graphs/G3.txt", 'r')
        
    G = nx.read_weighted_edgelist(graph_data, nodetype = int)
                
    return G
                
                
            
            
def V(graph):
    """

    Parameters
    ----------
    graph : Graph()
        Undirected graph

    Returns
    -------
    set
        Set of graph vertices in graph

    """
    return set(graph.nodes())

def E(graph):
    """
    Parameters
    ----------
    graph : Graph()
        Undirected graph

    Returns
    -------
    set
        Set of graph edges in graph

    """
    return set(graph.edges())

def prims_initialize(graph, v):
    """
    Parameters
    ----------
    graph : Graph()
        Undirected graph
    v : int
        Integer representing a vertex within graph to start Prim's algorithm on

    Returns
    -------
    T : Graph()
        Contains the MST
    """
    if v not in V(graph):
        return 'Error vertex not found'
    else:
        T = nx.Graph()
        T.add_node(v)
    return T

def is_spanning(graph, subgraph):
    """
    Parameters
    ----------
    graph : Graph()
        Undirected graph
    subgraph : Graph()
        MST.

    Returns
    -------
    bool
        A spanning tree of G will need to include all the vertices in G
    """
    return V(graph) == V(subgraph)
        

def possible_edges(G, T):
    """
    Parameters
    ----------
    G : Graph()
        Undirected graph.
    T : Graph()
        MST.

    Returns
    -------
    list
        list of all edges in G that have vertices in T only when the 
        first and second endpoint is not in T.

    """
    return [e for e in list(G.edges(V(T))) 
             if e[0] not in V(T) or e[1] not in V(T)]

def min_cost_edge(G, T):
    """
    Parameters
    ----------
    G : Graph()
        Undirected graph
    T : Graph()
        MST

    Returns
    -------
    min_cost_edge : tuple
        The edge with the lowest weight.
    """
    temp_edges = possible_edges(G, T)
    min_cost_edge = temp_edges[0]
    
    for e in temp_edges:
        if cost(G, min_cost_edge) > cost(G, e):
            min_cost_edge = e
            
    return min_cost_edge
    
