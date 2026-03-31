import gurobipy as gb
from gurobipy import GRB

m = gb.Model("problema de Atribuição")

P = [1,2,3]

T = [1,2,3]

custo = {}
custo[(1,1)] = 10
custo[(1,2)] = 8
custo[(1,3)] = 9
custo[(2,1)] = 7
custo[(2,2)] = 5
custo[(2,3)] = 6
custo[(3,1)] = 14
custo[(3,2)] = 13
custo[(3,3)] = 11

x = {}
for i,j in custo.keys():
    x[(i,j)] = m.addVar(obj = custo[(i,j)], lb = 0.0, ub = 1.0, vtype = gb.GRB.BINARY, name = f"x{i}_{j}")

for i in P:
    m.addConstr(gb.quicksum(x[(i,j)] for j in T)==1, name = "unicidade_pessoas")

for j in T:
    m.addConstr(gb.quicksum(x[(i,j)] for i in P)==1, name = "unicidade_tarefas")

m.setObjective(gb.quicksum(custo[(i,j)] * x[(i,j)] for i,j in custo.keys()),GRB.MAXIMIZE)

m.optimize()


for v in m.getVars():
    print(f"{v.VarName} -> {v.x}")