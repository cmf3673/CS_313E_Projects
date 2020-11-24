## Problem: A magic square is a square of numbers from 1 to n2 such that the 
# sum of every row, the sum of every column, and the sum of the two main diagonals 
# is the same number. There are many algorithms to generate odd magic squares of 
# order 3 or greater. There are also algorithms to generate even magic squares of 
# order 4 or greater. But the algorithms to generate even order magic squares are 
# more complicated and you cannot get all magic squares of a given order using these 
# algorithms.

# Your input will be a single integer n that will be 3 or greater. For this assignment 
# you will generate all magic squares through permutation. We will test you for order 
# 3 magic squares but your code should be general enough that it can do higher order \
# magic squares. The process is straight forward but time consuming. Here are the steps:

# 1. Create a 1-D list of integers 1 through n2.
# 2. Permute this list of integers.
# 3. For each permutation check if this 1-D list is a magic square if converted to a 2-D list. If it is, then print the 1-D list.
# 4. Stop when you have gone through all the permutations.



import math
# checks if a 1-D list if converted to a 2-D list is magic
# a is 1-D list of integers
# returns True if a is magic and False otherwise
def is_magic ( a ):
  n = int(math.sqrt(len(a)))
  MAGIC_CONST = (n ** 3 + n) / 2

  # Check rows
  for i in range(n):
    sum = 0
    for j in range(n):
      sum += a[j + (n * i)]
    if sum != MAGIC_CONST:
        return False

  # Check col
  for i in range(n):
      sum = 0
      for j in range(n):
        sum += a[i + (n * j)]
      if sum != MAGIC_CONST:
          return False
  
  # Check main diag.
  sum = 0
  for i in range(0, n**2, n + 1):
    sum += a[i]
  if sum != MAGIC_CONST:
      return False
  
  # Check secondary diag.
  sum = 0
  for i in range(n - 1, n ** 2 - (n - 1), n - 1):
    sum += a[i]
  if sum != MAGIC_CONST:
      return False

  return True


# this function recursively permutes all magic squares
# a is 1-D list of integers and idx is an index in a
# it stores all 1-D lists that are magic in the list all_magic
def permute ( a, idx, all_magic ):
  hi = len(a)
  if is_magic(a):
    all_magic.append(a[:])
  else:
      for i in range(idx, hi):
          a[idx], a[i] = a[i], a[idx]
          permute(a, idx + 1, all_magic)
          a[idx], a[i] = a[i], a[idx]
    

def main():
  # read the dimension of the magic square
  in_file = open ('magic.in', 'r')
  line = in_file.readline()
  line = line.strip()
  n = int (line)
  in_file.close()

  # create an empty list for all magic squares
  all_magic = []
  # create the 1-D list that has the numbers 1 through n^2
  a = [i for i in range(1, n**2 + 1)]
  # generate all magic squares using permutation 
  permute(a, 0, all_magic)
  # print all magic squares
  for i in range(len(all_magic)):
    print(all_magic[i])

if __name__ == "__main__":
  main()
