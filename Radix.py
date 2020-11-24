## Problem: In this assignment you will modify the Radix Sort algorithm so that 
# it sorts strings that have a mix of lower case letters and digits - 
# similar to your UT EIDs.

# Input:
# You will be given a file radix.in in the following format. 
# The first line in the input will be a single integer n that 
# states the number of strings to follow. This will be followed
# by n lines where there will be a single string per line. Each 
# string will have between 1 and 10 characters inclusive. The characters 
# will be either the digits 0 through 9 or the letters 'a' through 'z'.

# Output:
# You will output a list having the strings in sorted order.



import sys
class Queue (object):
  def __init__ (self):
    self.queue = []

    # print the queue
  def __str__(self):
    return str(self.queue)

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))


# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
  # Create queue list and char. dict.
  queues = [Queue() for i in range(37)]
  char_dict = {'*': 0}

  # Add keys and values
  for i in range(1, 37):
    if i <= 10:
      char_dict[chr(47 + i)] = i
    else:
      char_dict[chr(86 + i)] = i

  # Get longest string
  long_len = get_longest_string(a)

  # Pad strings in a
  a_pad = []
  for s in a:
    while len(s) < long_len:
      s += '*'
    a_pad.append(s)

  # Cycle through and add each string to a queue based on their first letter
  # Then dequeue into list
  ordered_ls = a_pad
  for i in range(-1, -(long_len + 1), -1):

    # Add to queue
    for s in ordered_ls:
        queues[char_dict[s[i]]].enqueue(s)

    # Dequeue into ordered_ls
    ordered_ls = []
    for q in queues:
      while not q.is_empty():       
        ordered_ls.append(q.dequeue())
  
  # Take out padding
  for i in range(len(ordered_ls)):
    ordered_ls[i] = ordered_ls[i].replace('*', '')

  return ordered_ls


# Gets the int for the len of the longest string. 
def get_longest_string(a):
  long_len = len(a[0])
  for string in a:
    if len(string) > long_len:
      long_len = len(string)
  return long_len


def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()