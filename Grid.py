## Problem: ssume that you have square grid of positive integers. 
# You want to start at the top left corner in the grid and work your 
# way down to the bottom right corner. The contraint that you have is 
# that you can only move either to the right or down from your current 
# position in the grid. You want to take the path that gives you the 
# greatest sum.

# Input: You will read your data from standard input.
#  The first line in input will be the dimension n of this square grid. 
# The dimension of the grid will be between 5 and 40 inclusive. It will 
# be followed by n lines of data. Each line will have n positive integers 
# between 1 and 99 inclusive.

# Output: First you will print to standard out the total number of paths in 
# the grid and then you will output the greatest path sum in the grid. You do
#  NOT have to output the actual path.



# counts all the possible paths in a grid 
def count_paths(n):
    # Create an n x n list with 1s in the last row and column.
    path_grid = [[0 if (j != n - 1) else 1 for j in range(n)] if (i != n - 1) else [1 for k in range(n)] for i in range(n)]
    
    # Fill grid with int representing number of paths to get to the bottom right element. 
    for row in range(n - 2, -1, -1):
        for col in range(n - 2, -1, -1):
            path_grid[row][col] = path_grid[row][col + 1] + path_grid[row + 1][col]
    
    return path_grid[0][0]


# gets the greatest sum of all the paths in the grid
def path_sum(grid, n):

    # Create sun grid. 
    sum_grid = [[0 for j in range(n)] for i in range(n)]

    # Put last row and col element from grid. 
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            
            # If bottom right element
            if i == n - 1 and j == n - 1:
                
                sum_grid[i][j] = grid[i][j]
                
            # If in last row 
            elif i == n - 1:
                sum_grid[i][j] = sum_grid[i][j + 1] + grid[i][j]
            # If last col
            elif j == n - 1:
                sum_grid[i][j] = sum_grid[i + 1][j] + grid[i][j]
            # If not in either, compare right and down elements and add the higher one.
            else:
                sum_grid[i][j] = max(sum_grid[i + 1][j], sum_grid[i][j + 1]) + grid[i][j]
            
    return sum_grid[0][0]


def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end =' ')
        print()


def main():
    # read data from standard input
    # read the dimension of the grid
    dim = int(input())
    grid = [[int(num) for num in input().split()] for i in range(dim)]
    
    # get the number of paths in the grid and print
    num_paths = count_paths(dim)
    print(num_paths)

    # get the maximum path sum and print
    max_path_sum = path_sum(grid, dim)
    print (max_path_sum)

if __name__ == "__main__":
    main()