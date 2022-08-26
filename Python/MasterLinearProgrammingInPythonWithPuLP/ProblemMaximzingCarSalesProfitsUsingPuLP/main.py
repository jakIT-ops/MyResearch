from pulp import *

problem = LpProblem('Car_Factory', LpMaximize)

A = LpVariable('Car_A', lowBound=0 , cat=LpInteger)
B = LpVariable('Car_B', lowBound=0 , cat=LpInteger)

#Objective Function
problem += 20000*A + 45000*B , 'Objective Function'

#Constraints
problem += 4*A + 5*B <= 30, 'Designer Constraint'
problem += 3*A + 6*B <=30, 'Engineer Constraint'
problem += 2*A + 7*B <=30, 'Machine Constraint'

print("Current Status: ", LpStatus[problem.status])

print("Solving the problem...")

# Solving the problem
# The argument suppresses the console output
problem.solve(PULP_CBC_CMD(msg=False))

print("Current Status: ", LpStatus[problem.status])

print("Number of Car A Made: ", A.varValue)
print("Number of Car B Made: ", B.varValue)
print("Total Profit: ", value(problem.objective))

'''
Current Status:  Not Solved
Solving the problem...
Current Status:  Optimal
Number of Car A Made:  1.0
Number of Car B Made:  4.0
Total Profit:  200000.0
'''
