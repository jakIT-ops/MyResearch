import numpy as np

Z = np.arange(9).reshape(3,3) # 0 - 8 hurtel toonii 3x3 MATRIX

# Get the First Value
print(Z[0,0])

# Get the Last Value
print(Z[-1,-1])

# Get a row from a Grid
# Z[row_index]
print(Z[1])

# Get a Column from a Grid
# Z[:,column_index]
print(Z[:,2])

# Get a Mini-grid from a Grid
# Z[row_index:, column_index:]
print(Z[1:,1:])

# Arrange Values from a Grid in a Mini-grid
# Z[::row_size-1,::column_size-1]
print(Z[::2,::2])