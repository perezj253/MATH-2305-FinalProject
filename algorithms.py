"""
The algorithms module will make use of the helper functions in the functions.py


"""

from functions import readGraphFromFile
from functions import min_cost_edge, prims_initialize, is_spanning, cost, E
from drawing import show_weighted_graph, draw_subtree


def prims(G, starting_vertex, show_steps = False):
    """Makes use of the helper functions in functions.py to implement Prim's
    algorithm on user specified graph. 
    

    Parameters
    ----------
    user_choice : int
        user choice for graph to implement Prim's algorithm

    Returns
    -------
    G: Graph
        The minimum spanning tree of a weigthed graoh.

    """
    if show_steps == True:
        show_weighted_graph(G)
        
    T = prims_initialize(G, starting_vertex)
    
    if show_steps == True:
        show_weighted_graph(G)
        
    while is_spanning(G, T) == False:
        e = min_cost_edge(G, T)
        T.add_edge(e[0], e[1])
        if show_steps == True:
            draw_subtree(G, T)
            
  
            
    return T
    
    
