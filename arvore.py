import networkx as nx
import gurobipy as gb
from gurobipy import GRB

G = nx.DiGraph()
m = gb.Model("Fluxo em rede de custo mínimo")

vertices = {
    1:{"entrada":4,"saida":0},
    2:{"entrada":0,"saida":1},
    3:{"entrada":0,"saida":1},
    4:{"entrada":0,"saida":1},
    5:{"entrada":0,"saida":1}
    }

G.add_nodes_from((node, attrs) for node, attrs in vertices.items())
#print(G.nodes[1])

custo = {}
custo[(1,2)] = 1
custo[(1,3)] = 2
custo[(1,5)] = 2
custo[(2,1)] = 1
custo[(2,3)] = 1
custo[(2,4)] = 2
custo[(3,1)] = 2
custo[(3,2)] = 1
custo[(3,4)] = 3
custo[(3,5)] = 1
custo[(4,2)] = 2
custo[(4,3)] = 3
custo[(4,5)] = 3
custo[(5,1)] = 2
custo[(5,2)] = 1
custo[(5,3)] = 3

for i,j in custo.keys():
    G.add_edge(i,j,custo = custo[(i,j)])
#print(G.edges(data=True))

x = {}
y = {}
for i,j,data in G.edges(data=True):
    x[(i,j)] = m.addVar(obj = data["custo"], lb = 0.0, vtype = gb.GRB.INTEGER,name=f"x{i}{j}")
    y[(i,j)] = m.addVar(obj = data["custo"],vtype=gb.GRB.BINARY,name=f"x{i}{j}")


#Restrição: x(i,v) - x(v,j) = (Saída de v) - (Entrada de v)

for v in list(G.nodes()):
    m.addConstr(gb.quicksum(x[(i,j)] for i,j in G.in_edges(v))- 
                gb.quicksum(x[(i,j)] for i,j in G.out_edges(v)) == G.nodes[v]["saida"] - G.nodes[v]["entrada"])
#Restrição: Capacidade = 15
for(i,j) in G.edges():
    m.addConstr(x[(i,j)] <= 4)
    m.addConstr(y[(i,j)] <= x[(i,j)])
    m.addConstr(y[(i,j)] >= (x[(i,j)]/4))

#Objetivo: Minimizar custo total
m.setObjective(gb.quicksum(data["custo"]*y[(i,j)] for i,j,data in G.edges(data=True)),GRB.MINIMIZE)

m.optimize()

for v in m.getVars():
    print(f"{v.VarName} -> {v.x}")