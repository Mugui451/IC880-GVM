import networkx as nx
import gurobipy as gb
import matplotlib.pyplot as mpl
from gurobipy import GRB

def aresta(i,j):
    return(min(i,j),max(i,j))

m = gb.Model("atribuição grafo")
G = nx.Graph()

custo = {}
custo[(1,4)] = 10
custo[(1,5)] = 8
custo[(1,6)] = 9
custo[(2,4)] = 7
custo[(2,5)] = 5
custo[(2,6)] = 6
custo[(3,4)] = 14
custo[(3,5)] = 13
custo[(3,6)] = 11

for i,j in custo.keys():
    G.add_edge(i,j,custo = custo[(i,j)])

#print(G.edges(data=True))



x = {}

for i,j,data in G.edges(data=True):
    x[aresta(i,j)] = m.addVar(obj = data["custo"], lb = 0.0, ub = 1.0, vtype = gb.GRB.BINARY, name = f"x{aresta(i,j)}")

#print(list(G.nodes()))

for k in G.nodes():
    m.addConstr(gb.quicksum(x[aresta(i,j)] for i,j in G.edges(k))==1)

m.setObjective(gb.quicksum(data["custo"] * x[aresta(i,j)] for i,j,data in G.edges(data=True)),GRB.MAXIMIZE)

m.optimize()

#for v in m.getVars():
#    print(f"{v.VarName} -> {v.x}")

print(G.edges)

nx.draw(G, with_labels=True)
mpl.show()