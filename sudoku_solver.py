"""
Approach:

1. Create the board
    a. Need rows and columns
        >Columns: letters, rows: numbers
    b. Need to create rows and columns
    c. Need to create squares
2. Populate the board
    a. Naive approach: manually input starting values
    b. Better approach: find a dataset and download.
3. Write an algorithm to solve
    a. Check 'iteratively':
        >Check within the square, row, column
            -This order shouldn't matter
"""

# Setting up the names of each cell
row = 'ABCDEFGHI'
col = '123456789'

# This function gives all the cells for the grid
def set_up(row, col):

    board = []
    for i in row:
        for j in col:
            board.append(i + j)

    return board

board = set_up(row, col)
# print(board)

row_unit = [set_up(row, i) for i in col]
col_unit = [set_up(i, col) for i in row]
sq_unit = [set_up(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ['123',
'456', '789']]

grid = (row_unit + col_unit + sq_unit)

print(len(grid))


