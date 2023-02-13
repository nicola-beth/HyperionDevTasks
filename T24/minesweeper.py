start_grid = [["-", "-", "-", "#", "#"],
              ["-", "#", "-", "-", "-"],
              ["-", "-", "#", "-", "-"],
              ["-", "#", "#", "-", "-"],
              ["-", "-", "-", "-", "-"]
              ]


def minesweep(grid):
    hash_num = 0
    # for row in range(len(start_grid)):
    #     for column in range(len(start_grid[row])):
    row = 2
    column = 1
    if grid[row][column] == "-":
        if grid[row - 1][column] == "#":
            hash_num += 1
        if grid[row - 1][column + 1] == "#":
            hash_num += 1
        if grid[row][column + 1] == "#":
            hash_num += 1
        if grid[row + 1][column + 1] == "#":
            hash_num += 1
        if grid[row + 1][column] == "#":
            hash_num += 1
        if grid[row + 1][column - 1] == "#":
            hash_num += 1
        if grid[row][column - 1] == "#":
            hash_num += 1
        if grid[row - 1][column - 1] == "#":
            hash_num += 1
    grid[row][column] = hash_num
    print(grid)

minesweep(start_grid)
