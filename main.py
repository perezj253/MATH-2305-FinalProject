"""


"""

from functions import readGraphFromFile, V
from drawing import draw_subtree, show_weighted_graph
from algorithms import prims

# Ask user whihch graph they would like to run Prim's algorithm on
print("Which graph would you like to implement Prim's algorithm on? ")
print("1. G1.txt")
print("2. G2.txt")
print("3. G3.txt")

user_graph = int(input("Enter 1 - 3: "))

# validate that the user picked a correct graph
while not(user_graph >= 1 and user_graph <= 3):
    user_graph = int(input("Enter a valid file index. 1 - 3: "))

G = readGraphFromFile(user_graph)



# Promt user for inital vector 
valid_vector = True
while valid_vector:
    print(V(G))
    initial_vector = int(input("Enter a vector from the list to begin:  "))
    if initial_vector in V(G):
        valid_vector = False
        
show_steps = False

user_input = input("Would you like to see the steps? (yes) or (no)")

if user_input.lower() == "yes":
    show_steps = True

    
#show_weighted_graph(G)

# Start running Prim's algorithm
T = prims(G, initial_vector, show_steps)

# show MST
if show_steps == False:
    draw_subtree(G, T)
