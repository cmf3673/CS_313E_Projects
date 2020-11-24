## Problem: An interval on the number line is denoted by a pair of values like so: (3, 8). 
# Our intervals are closed. So this interval represents all numbers between 3 and 8 inclusive. 
# The first number is always going to be strictly less than the second number. 
# Normally in mathematics we represent a closed interval with square brackets. 
# But in our program we will represent an interval by means of a tuple and tuples 
# in Python are represented with parentheses.

# If we have two intervals like (7, 12) and (4, 9), they overlap. 
# We can collapse overlapping intervals into a single interval (4, 12). 
# But the following two intervals (-10, -2) and (1, 5) are non-intersecting 
# intervals and cannot be collapsed.

# The aim in this assignment is take a set of intervals and collapse all the overlapping intervals 
# and print the smallest set of non-intersecting intervals in ascending order of the lower end of 
# the interval and then print the intervals in increasing order of the size of the interval.



# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples (tuples_list):
    i = 0
    while i < (len(tuples_list) - 1):
        can_increment = True
        if i < len(tuples_list): # Inbounds check 
            curr_tuple = tuples_list[i]
            for j in range(i + 1, len(tuples_list)):
                next_tupl = tuples_list[j]
                # Compare and see if pair intersects. 
                if is_intersecting(curr_tuple, next_tupl):
                    can_increment = False
                    new_tuple = collapse_tuples(curr_tuple, next_tupl)
                    # Remove current and next tuples
                    del tuples_list[i]
                    del tuples_list[j - 1]
                    tuples_list.insert(i, new_tuple)
                    i = 0 # To start over
                    break
        if can_increment: 
            i += 1

    # Insertion sort by lower interval values.
    for i in range(1, len(tuples_list)):
        j = i
        # While the element to the left of me tuples_list[j]
        # has a higher interval_min, I am not the first element.
        while (j > 0 and tuples_list[j][0] < tuples_list[j - 1][0]):
            # Now swap element j with element to left of it:
            tuples_list[j], tuples_list[j - 1] = tuples_list[j - 1], tuples_list[j]
            j -= 1

    return tuples_list


# This function takes two tuples and checks if they intersect.
def is_intersecting(current_tuple, next_tuple):
  # Getting the lowest tuple.
  low_tuple, high_tuple = assign_range(current_tuple, next_tuple)
  # Return true if they intersect, false if they don't. (1, 4), (2, 8)
  return (high_tuple[0] >= low_tuple[0]) and (low_tuple[1] > high_tuple[0]) or (low_tuple[1] == high_tuple[0])


# This function takes two tuples and collapses them.
def collapse_tuples(current_tuple, next_tuple):
  # First get the new interval min and max.
  maxi = current_tuple[0]
  mini = current_tuple[0]
  maxi, mini = update_min_max(current_tuple, next_tuple, maxi, mini)
  collapsed_tuple = (mini, maxi)
  return collapsed_tuple
  

def update_min_max(current_tuple, next_tuple, maxi = 0, mini = 0):
  for num in current_tuple:
    if num < mini:
      mini = num
    if num > maxi:
      maxi = num
  for num in next_tuple:
    if num < mini:
      mini = num
    if num > maxi:
      maxi = num
  return maxi, mini


def assign_range(current_tuple, next_tuple):
  if current_tuple == next_tuple:
    return current_tuple, next_tuple
  if current_tuple[0] < next_tuple[0]:
    low_tuple = current_tuple
    high_tuple = next_tuple
  elif current_tuple[0] == next_tuple[0]:
    if current_tuple[1] < next_tuple[1]:
      low_tuple = current_tuple
      high_tuple = next_tuple
    else:
      low_tuple = next_tuple
      high_tuple = current_tuple
  else:
    low_tuple = next_tuple
    high_tuple = current_tuple
  return low_tuple, high_tuple


# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):
    # Insertion sort
    # While the element to the left has a bigger interval size, swap.
    for i in range(1, len(tuples_list)):
        j = i
        while j > 0 and get_interval_size(tuples_list[j]) < get_interval_size(tuples_list[j - 1]):
            tuples_list[j], tuples_list[j - 1] = tuples_list[j - 1], tuples_list[j]
            j -= 1
    return tuples_list


# Gets the interval size.
def get_interval_size(tuple):
    return tuple[1] - tuple[0]


def get_tuples(file_name):
  master_ls = []
  infile = open(file_name)
  get_lines(infile, master_ls)
  tuple_ls = []
  for i in range(1, len(master_ls)):
    tuple_ls.append((int(master_ls[i][0]), int(master_ls[i][1])))
  return tuple_ls, master_ls[0][0]


# This function gets the individual lines for the get_tuples function.
def get_lines(infile, tuples):
  for line in infile:
    line_tuple = line.split()
    tuples.append(line_tuple)


def main():
    # read the input data and create a list of tuples
    file_name = 'egde_case.in'
    tuples, num_lines = get_tuples(file_name)
    # merge the list of tuples
    merged_ls = merge_tuples(tuples)
    # print the merged list
    print(merged_ls)
    # sort the list of tuples according to the size of the interval
    sorted_ls = sort_by_interval_size(merged_ls)
    # print the sorted list
    print(sorted_ls)

if __name__ == "__main__":
  main()