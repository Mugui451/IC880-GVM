import networkx as nx
import numpy as np
import matplotlib.pyplot as mpl
#edge_list = [(1,4),(1,5),(1,6),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6)]
G = nx.from_numpy_array(np.array([[0,0,0,1,1,1],
                                  [0,0,0,1,1,1],
                                  [0,0,0,1,1,1],
                                  [1,1,1,0,0,0],
                                  [1,1,1,0,0,0],
                                  [1,1,1,0,0,0]]))

#nx.draw_spring(G, with_labels=True)
#mpl.show()
print(nx.density(G))
print(nx.diameter(G))