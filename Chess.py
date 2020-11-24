## Problem: The Eight Queens Problem is a fairly old problem that has been well 
# discussed and researched. The first published reference to this problem was 
# in a German Chess magazine in 1848 by Max Bezzel. In 1850, Franz Nauck published 
# all 92 solutions of the problem for an 8x8 board. S. Gunther in 1874 suggested 
# a method for finding solutions by using determinants and J.W.L. Glaisher extended 
# this method. E. Dijkstra published a detailed description of the solution of the 
# problem as a depth-first backtracking algorithm.

# The original statement of the problem ran as follows - how can we place eight 
# queens on a regular chess board such that no queen can capture another. 
# It turns out there is no unique solution but 92 possible solutions of which only 
# 12 are distinct. The 12 distinct solutions can generate all other solutions through 
# reflections and / or rotations. Here is a table that gives the size of the board, 
# all possible solutions, and all distinct solutions.

# Read the size of the board. 
# The number n will between 1 and 12 inclusive. 
# Generate all possible solutions for a board 
# of that size. Keep a count of the number of solutions 
# and print the total number of solutions. For a board 
# of size 8 your output should be 92.



import sys
class Queens (object):
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()
    print ()

  # check if a position on the board is valid
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True
    
  # do the recursive backtracking
  def recursive_solve (self, col, counter):
    # base case: if at last col
    if (col == self.n):
      counter[0] += 1
      return True
    # recursive case: for each row in col, if good spot, place Q. 
    # The rec. check if there are spots for all other queens given the previous placement. 
    # if get to end, false returns and that spot gives no soln, thus, backtrack. 
    else:
      for i in range(self.n):
        if (self.is_valid (i, col)):
          self.board[i][col] = 'Q'
          self.recursive_solve(col + 1, counter)
          self.board[i][col] = '*'


  # if the problem has a solution print the board
  def solve (self, counter):
    self.recursive_solve(0, counter)


def main():
  # read the size of the board
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create a chess board
  game = Queens (n)
  
  # place the queens on the board and count the solutions
  counter = [0]
  game.solve(counter)

  # print the number of solutions
  print(counter[0])
 
if __name__ == "__main__":
  main()