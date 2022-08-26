from pulp import *

numbers = [str(i) for i in range(1,10)]
Rows = numbers
Cols = numbers
Values = numbers

choices = LpVariable.dicts("Choice",(Values,Rows,Cols),0,1,LpInteger)

'''
    Creating the Problem
'''
prob = LpProblem("Sudoku_Problem",LpMinimize)

'''
 Objective Function, set to 0 since Sudoku doesn't have an optimal solution
'''
prob += 0, "Arbitrary Objective Function"

'''
    Constraint: Only One number can be present in a box
'''
for r in Rows:
    for c in Cols:
        prob += lpSum([choices[v][r][c] for v in Values]) == 1, ""

'''
  Constraint: A row should have all the numbers from 1-9 and
  no number can be repeated
'''
for v in Values:
    for r in Rows:
        prob += lpSum([choices[v][r][c] for c in Cols]) == 1, ""

'''
    Constraint: A column should have all the numbers from 1-9 and no
    number can be repeated
'''
for v in Values:
    for c in Cols:
        prob += lpSum([choices[v][r][c] for r in Rows]) == 1, ""

'''
    Sub Grids, i.e the 9 boxes inside the sudoku Board
'''
Subgrids =[]
for i in range(3):
    for j in range(3):
        Subgrids += [[(Rows[3*i+k],Cols[3*j+l]) for k in range(3) for l in range(3)]]

'''
    Constraint: The sub-grids, i.e the 9 boxes, should have all the
     numbers from 1-9 and no number can be repeated
'''
for v in Values:
    for b in Subgrids:
        prob += lpSum([choices[v][r][c] for (r, c) in b]) == 1, ""

sudoku_problem = [
    ["5","1","1"], ["6","2","1"], ["8","4","1"],
    ["4","5","1"], ["7","6","1"], ["3","1","2"],
    ["9","3","2"], ["6","7","2"], ["8","3","3"],
    ["1","2","4"], ["8","5","4"], ["4","8","4"],
    ["7","1","5"], ["9","2","5"], ["6","4","5"],
    ["2","6","5"], ["1","8","5"], ["8","9","5"],
    ["5","2","6"], ["3","5","6"], ["9","8","6"],
    ["2","7","7"], ["6","3","8"], ["8","7","8"],
    ["7","9","8"], ["3","4","9"], ["1","5","9"],
    ["6","6","9"], ["5","8","9"]
]

# The starting numbers are entered as constraints
for num in sudoku_problem:
    prob += choices[num[0]][num[1]][num[2]] == 1, ""

def display_sudoku(matrix , sudokuout , numbers):
    print('\n --------- Sudoku Game Output  --------- \n')
    for r in numbers:
        if r == "1" or r == "4" or r == "7":
            sudokuout.write("+-------+-------+-------+\n")
        for c in numbers:
            for v in numbers:
                if value(matrix[v][r][c]) == 1:

                    if c == "1" or c == "4" or c == "7":
                        sudokuout.write("| ")

                    sudokuout.write(v + " ")

                    if c == "9":
                        sudokuout.write("|\n")


    sudokuout.write("+-------+-------+-------+")


# The problem is solved using PuLP's choice of Solver
prob.solve(PULP_CBC_CMD(msg=False))

# The status of the solution is printed to the screen
# print ("Status:", LpStatus[prob.status])

# Print the output
f = open("sudokuout.txt", "w")

display_sudoku(choices, f , numbers)

f.close()

f = open("sudokuout.txt", "r")
print(f.read())
f.close()
