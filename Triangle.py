## Problem: This assignment is a variation of a problem from Project Euler. 
# You are required to find the greatest path sum starting at the top of the 
# triangle and moving only to adjacent numbers on the row below.

#    3
#   7 4
#  2 4 6
# 8 5 9 3
#In the above triangle, the maximum path sum is 3 + 7 + 4 + 9 = 23.

# You will read your input from the file triangle.in. 
# The first line indicates n the number of rows in the triangle. 
# This will be followed by n lines of data. Each line of data will 
# have only positive integers greater than 0. The first line of data 
# in the triangle will have one number, the second line in the triangle 
# will have two numbers and so on. The nth line will have n integers.

# You will apply two different approaches to problem solving to this single 
# problem - greedy and dynamic programming.



import sys
from timeit import timeit
# returns the greatest path sum using greedy approach
def greedy (grid):
  total_sum = grid[0][0]
  col = 0
  for i in range(0, len(grid) - 1):
    # check the two cells below for maximum
    temp_tuple = (grid[i + 1][col], grid[i + 1][col + 1])
    max_value = max(temp_tuple)
    total_sum += max_value
    col = grid[i + 1].index(max_value)
  return total_sum


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
    copy = grid[:]
    # print_grid(copy)
    max_col = len(copy) - 1

    for i in range(len(copy) - 1, 0, -1):
        for j in range(max_col):
            maximum = max(copy[i][j], copy[i][j + 1])
            copy[i - 1][j] += maximum
        max_col -= 1
    return copy[0][0]


def print_grid(grid):
    print()
    for row in grid:
        for num in row:
            print(num, end = ' ')
        print()

    
# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]
  return grid 


def main ():
  
  # read triangular grid from file
  grid = read_file()

  # print the output from greedy
  print(greedy(grid))
  # print(dynamic_prog(grid))
  #print(divide_conquer(grid))
  
  # check that the grid was read in properly
  # print (grid)
  
  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach


if __name__ == "__main__":
  main()