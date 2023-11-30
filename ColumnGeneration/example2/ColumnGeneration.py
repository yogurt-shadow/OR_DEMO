import gurobipy as gp
from gurobipy import GRB
import numpy as np

Length = 20
Demands = [3, 7, 9, 16]
Quants = [25, 30, 14, 8]

def ColumnGeneration():
    # Master Problem
    master_id, sub_id = 1, 1
    patterns = [[Length // Demands[j] if j == i else 0 for j in range(len(Demands))] for i in range(len(Demands))]
    Master = gp.Model("Master" + str(master_id))
    master_id += 1
    x = Master.addVars(len(patterns), vtype=GRB.CONTINUOUS, name = 'x')
    Master.setObjective(gp.quicksum(x[i] for i in range(len(x))))
    Master.addConstrs((gp.quicksum([patterns[j][i] * x[j] for j in range(len(patterns))]) >= Quants[i] for i in range(len(Demands))))
    Master.write(Master.ModelName + ".lp")
    Master.optimize()
    dual = Master.getAttr(GRB.Attr.Pi, Master.getConstrs())
    
    # Sub Problem
    Sub = gp.Model("Subproblem" + str(sub_id))
    sub_id += 1
    y = Sub.addVars(len(Demands), vtype=GRB.INTEGER, name='y')
    Sub.setObjective(1 - gp.quicksum(dual[i] * y[i] for i in range(len(y))))
    Sub.addConstr(gp.quicksum(Demands[i] * y[i] for i in range(len(y))) <= Length)
    Sub.write(Sub.ModelName + ".lp")
    Sub.optimize()
    obj = Sub.ObjVal
    new_pattern = [v.x for v in Sub.getVars()]
    Iter = 1
    while obj < 0:
        Iter += 1
        Master = gp.Model("Master" + str(master_id))
        master_id += 1
        patterns.append(new_pattern)
        print("patterns: ", patterns)
        x = Master.addVars(len(patterns), vtype=GRB.CONTINUOUS, name = 'x')
        Master.setObjective(gp.quicksum(x[i] for i in range(len(x))))
        Master.addConstrs((gp.quicksum([patterns[j][i] * x[j] for j in range(len(patterns))]) >= Quants[i] for i in range(len(Demands))))
        Master.write(Master.ModelName + ".lp")
        Master.optimize()
        dual = Master.getAttr(GRB.Attr.Pi, Master.getConstrs())
        Sub = gp.Model("Subproblem" + str(sub_id))
        sub_id += 1
        y = Sub.addVars(len(Demands), vtype=GRB.INTEGER, name='y')
        Sub.setObjective(1 - gp.quicksum(dual[i] * y[i] for i in range(len(y))))
        Sub.addConstr(gp.quicksum(Demands[i] * y[i] for i in range(len(y))) <= Length)
        Sub.write(Sub.ModelName + ".lp")
        Sub.optimize()
        obj = Sub.ObjVal
    # Convert Into Integer
    for v in Master.getVars():
        v.setAttr("VType", GRB.INTEGER)
    Master.optimize()
    print("Iter: ", Iter)
    print("Best obj: ", Master.ObjVal)
    print("Best pattern number: ", [v.x for v in Master.getVars()])

if __name__ == "__main__":
    ColumnGeneration()