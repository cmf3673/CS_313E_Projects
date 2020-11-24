## Problem: A Fibonacci string is a sequence of bit strings defined as follows:
# f(n) = '0' if n = 0
# f(n) = '1' if n = 1
# f(n) = f(n - 1) + f(n - 2) if n > 1
# The '+' operator denotes string concatenation.

# Here are the first 6 terms in the series:
# 0 | 0
# 1 | 1
# 2 | 10
# 3 | 101
# 4 | 10110
# 5 | 10110101

# Input: You will read your data from standard input. 
# The format of the input will be as follows: There will be two lines of input. 
# The first line will have an integer n where 0 ≤ n ≤ 30. The second line of 
# input will have a bit string p where 1 ≤ length of p ≤ 20 characters. The 
# length of p may exceed the length of the bit string returned by the 
# fibonacci function.

# Output: You will output a single integer that will be the number of times 
# the bit string p occurs in f(n). The occurrences of p may overlap.



import sys
# Input: n a positive integer
# Output: a bit string
def f(n, memo):
    if n == 0 or n == 1:
        return str(memo[n])
    else:
        if n >= len(memo):
            a = f(n - 1, memo) + f(n - 2, memo)
            memo.append(a)
            return a
        else:
            return str(memo[n])


# Input: s and p are bit strings
# Output: an integer that is the number of times p occurs in s
def count_overlap (s, p):
    count = 0
    for i in range(0, len(s)):
        if len(s[i:]) >= len(p) and s[i: i + len(p)] == p:
            count += 1
    return count


def main():
  # read n and p from standard input
  n = sys.stdin.readline()
  n = int (n.strip())
  p = sys.stdin.readline()
  p = p.strip()

  # compute the bit string f(n)
  s = f(n, [0,1])
  # determine the number of occurrences of p in f(n)
  c = count_overlap(s, p)
  # print the number of occurrences of p in f(n)
  print(c)

if __name__ == "__main__":
  main()