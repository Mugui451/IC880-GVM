import gurobipy as gb
from gurobipy import GRB

m =  gb.Model("problema_da_mochila")

quantidade_itens = 6
capacidade = 15

item = {}
item[1] = {"peso":2.0, "valor":10.0}
item[2] = {"peso":4.0, "valor":12.0}
item[3] = {"peso":5.0, "valor":14.0}
item[4] = {"peso":7.0, "valor":18.0}
item[5] = {"peso":9.0, "valor":20.0}
item[6] = {"peso":1.0, "valor":5.0}

x = {}

for i in item.keys():
    x[i] = m.addVar(obj = item[i]["valor"], lb = 0.0, ub = 1.0, vtype = gb.GRB.BINARY, name = f"x{i}")
    (item[i]["peso"])

print(x[3])

m.addConstr(gb.quicksum(item[i]["peso"] * x[i] for i in item.keys())<=capacidade, name = "capacidade")

m.setObjective(gb.quicksum(item[i]["valor"] * x[i] for i in item.keys()),GRB.MAXIMIZE)

m.optimize()
