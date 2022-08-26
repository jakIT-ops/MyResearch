matrix = [
    ["3", "1", "1"], ["6", "2", "1"], ["1", "3", "1"],
    ["8", "1", "2"], ["5", "2", "2"], ["2", "3", "2"],
    ["7", "1", "3"], ["4", "2", "3"], ["3", "3", "3"]
]

def display_sudoku(matrix , sudokuout , numbers):
    for r in numbers:
        if int(r)<4:
            if r == "1" or r == "4" or r == "7":
                sudokuout.write("+-------+\n")
            for c in numbers:
                if int(c)<4:
                    for v in numbers:
                        if value(matrix[v][r][c]) == 1:
                            if c == "1" or c == "4" or c == "7":
                                sudokuout.write("| ")
                            sudokuout.write(v + " ")
                            if c == "3":
                                sudokuout.write("|\n")
    sudokuout.write("+-------+\n")
