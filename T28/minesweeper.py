start_grid = [["-", "-", "-", "#", "#"],
              ["-", "#", "-", "-", "-"],
              ["-", "-", "#", "-", "-"],
              ["-", "#", "#", "-", "-"],
              ["-", "-", "-", "-", "-"]
              ]

#function to replace - with number of hashtags in surrounding positions (N, NE, E, SE, S, SW, W, NW) using index numbers representing these positions
#out of range resolved by only running where values will be in range using row/column index values in if statement
def minesweep(grid):
    #loop through height(rows) and length(columns) of grid
    for row in range(len(start_grid)):
        for column in range(len(start_grid[row])):
            hash_num = 0            #counter for each for loop
            if grid[row][column] == "-":
                if row > 0 and grid[row - 1][column] == "#":
                    hash_num += 1
                if row > 0 and column < 4 and grid[row - 1][column + 1] == "#":
                    hash_num += 1
                if column < 4 and grid[row][column + 1] == "#":
                    hash_num += 1
                if row < 4 and column < 4 and grid[row + 1][column + 1] == "#":
                    hash_num += 1
                if row < 4 and grid[row + 1][column] == "#":
                    hash_num += 1
                if row < 4 and column > 0 and grid[row + 1][column - 1] == "#":
                    hash_num += 1
                if column > 0 and grid[row][column - 1] == "#":
                    hash_num += 1
                if row > 0 and column > 0 and grid[row - 1][column - 1] == "#":
                    hash_num += 1
                grid[row][column] = hash_num        #replcae - with counter value calculated above
    for row in grid:
        print(row)

#call function with argument defined above
minesweep(start_grid)