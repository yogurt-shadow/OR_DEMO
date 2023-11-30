import gurobipy as gp
from gurobipy import GRB
import numpy as np

# men[i][j]: with length j and consider first i demands, calculate all patterns

def Recursion(length, demands, item, mem):
    print("item: ", item)
    print("mem: ", mem)
    if length == 0:
        return [[0 for i in range(item)]]
    if item == 1:
        return [[length // demands[0]]]
    # memory
    if mem[item][length] != None:
        return mem[item][length]
    else:
        res = []
        max_ele = length // demands[item - 1]
        print("max ele: ", max_ele)
        curr_ele = 0
        while curr_ele <= max_ele:
            curr_pattern = Recursion(length - curr_ele * demands[item - 1], demands, item - 1, mem)
            print("curr pattern: ", curr_pattern)
            for ele in curr_pattern:
                ele.append(curr_ele)
                res.append(ele)
            curr_ele += 1
        mem[item][length] = res
        return res

"""
Given a roll of with lenghth `length`
Calculate all patterns with demand `demands`
"""
def CalculatePatterns(length, demands):
    mem = [[None for j in range(length + 1)] for i in range(len(demands) + 1)]
    return Recursion(length, demands, len(demands), mem)

"""

"""
def TraditionalSolve(demands, quants, length):
    # sorted by increasing order
    z = zip(demands, quants)
    z = sorted(z, reverse=False)
    demands, quants = zip(*z)
    model = gp.Model("Traditional")
    patterns = CalculatePatterns(length, demands)
    pass
    
if __name__ == "__main__":
    res = CalculatePatterns(10, [2, 3, 5])
    print(res)