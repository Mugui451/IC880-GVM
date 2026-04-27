import networkx as nx
import gurobipy as gb
from gurobipy import GRB

G = nx.Graph()
m = gb.Model("Árvore Geradora Máxima")


n = 5

def aresta(i,j):
    return(min(i,j),max(i,j))

custo = {}
custo[(1,2)] = 1
custo[(1,3)] = 2
custo[(1,5)] = 2

custo[(2,3)] = 1
custo[(2,4)] = 2

custo[(3,4)] = 3
custo[(3,5)] = 1

custo[(4,5)] = 3


for i,j in custo.keys():
    G.add_edge(i,j,custo = custo[(i,j)])
#print(G.edges(data=True))


x = {}
for i,j,data in G.edges(data=True):
    x[aresta(i,j)] = m.addVar(obj = data["custo"], lb = 0.0, ub = 1.0, vtype = gb.GRB.INTEGER,) # name = f"x{aresta(i,j)}"

#m.addConstr(gb.quicksum(x[aresta(i,j)] == n-1))

for s in range(1, 2**n - 1):
    m.addConstr(
        gb.quicksum(
            x[u,v]
            for (u,v) in custo
            if ((s >> u) & 1) != ((s >> v) & 1)
        ) >= 1
    )

m.setObjective(gb.quicksum(data["custo"]*x[(i,j)] for i,j,data in G.edges(data=True)),GRB.MAXIMIZE)

m.optimize()