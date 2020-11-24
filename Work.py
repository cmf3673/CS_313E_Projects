## Problem: Vyasa has to complete a programming assignment overnight. 
# He has to write n lines of code before morning. He is dead tired and 
# he tries drinking some black coffee to keep him awake. But each time he 
# drinks a cup of coffee he stays awake for a short amount of time but his
# productivity goes down by a constant factor k

# This is how he plans to write the program. He will write the first v lines of code, 
# then drink his first cup of coffee. Since his productivity has gone down by a factor 
# of k he will write v // k lines of code. He will have another cup of coffee and then 
# write v // k**2 lines of code. He will have another cup of coffee and write v // k**3 
# lines of code and so on. He will collapse and fall asleep when v // k ** p becomes 0.

# Now Vyasa does want to complete his assignment and maximize on his sleep. So he wants to 
# figure out the minimum allowable value of v for a given productivity factor that will allow 
# him to write at least n lines of code before he falls asleep.

#Input: You will read your input from standard input as given in the following format:
# 2
# 300 2
# 59 9
# The first line is T the number of test cases. This will be followed by T lines of input. 
# Each line of input will have two numbers n and k. n is the number of lines of code to 
# write and k is the productivity factor, where 1 ≤ n ≤ 106 and 2 ≤ k ≤ 10.

# Output: For each test case write your result to standard out as shown in work.out. 
# In your output there will be v lines of code the Vyasa has to write, as well as the 
# time it took for each function. For the above two test cases, the output will be:

# Binary Search: 152
# Time: 9.512901306152344e-05

# Linear Search: 152
# Time: 0.0005910396575927734


# Binary Search: 54
# Time: 4.696846008300781e-05

# Linear Search: 54
# Time: 9.012222290039062e-05

# Do not worry if your times don't match exactly. 
# For this assignment, main has been written completely 
# for you, and nothing needs to be changed in it.



import time
# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
    total = 0
    exp = 0
    current_term = v
    while current_term > 0:
        current_term = v // (k ** exp)
        total += current_term
        exp += 1
    return total


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
    for i in range(2, n + 1):
        if sum_series(i, k) >= n:
            return i
    return i

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
    high = n
    low = 0
    while high > low:
        # print(f'high: {high}')
        # print(f'low: {low}')
        m = (high + low) // 2 
        m_val = sum_series(m, k)
        # print(f'm: {m}')
        # print(f'm_val: {m_val}')
        # print('----------------')
        # Error occurs when I need the low or 
        if m_val == n:
            break
        elif m_val < n:
            low = m + 1 
        elif m_val > n:
            high = m - 1
    # Check if low or high is closer to the desired number:
    m = low if 0 <= sum_series(low, k) - n < m_val - n else m
    m = high if 0 <= sum_series(high, k) - n < m_val - n or m_val < n else m
    # print(f'Lines got: {m_val}')
    # print(f'Line need: {n}')
    return m


def main():
  in_file = open("work.in", "r")
  num_cases = int((in_file.readline()).strip())

  for i in range(num_cases):
    inp = (in_file.readline()).split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))
    print()
    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))
    print()
    print()

if __name__ == "__main__":
  main()