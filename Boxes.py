## Problem: Imagine a room full of boxes. Each box has a length, width, and height. 
# Since the boxes can be rotated those terms are inter- changeable. The dimensions 
# are integral values in a consistent system of units. The boxes have rectangular 
# surfaces and can be nested inside each other. A box can nest inside another box 
# if all its dimensions are strictly less than the corresponding dimensions of the 
# other. You may only nest a box such that the corresponding surfaces are parallel 
# to each other. A box may not be nested along the diagonal. You cannot also put two 
# or more boxes side by side inside another box.

# You will read your input from standard input. 
# The list of boxes will be in a file called boxes.in. 
# The first line gives the number of boxes n. The next n 
# lines gives a set of three integers separated by one or 
# more spaces. These integers represent the 3 dimensions of 
# a box. Since you can rotate the boxes, the order of the 
# dimensions does not matter. It may be to your advantage to 
# sort the dimensions in ascending order.

# There will be just two lines in your output. 
# The first line will be an integer giving the largest number 
# of boxes that can fit inside each other. The second line 
# will give the number of such sets of boxes that do fit.



# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
  if idx == len(box_list):
    all_box_subsets.append(sub_set)
  else:
    copy = sub_set[:]
    sub_set.append(box_list[idx])

    sub_sets_boxes(box_list, sub_set, idx + 1, all_box_subsets)
    sub_sets_boxes(box_list, copy, idx + 1, all_box_subsets)


# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets (all_box_subsets, largest_size, all_nesting_boxes):
    largest_nesting_boxes = []
    # Get all nesting subsets and largest nesting size
    for subset in all_box_subsets:
        if subset_nest(subset):
            all_nesting_boxes.append(subset)
            if len(subset) > largest_size:
                largest_size = len(subset)
    # Take out all subsets smaller than largest subset size.
    for subset in all_nesting_boxes:
        if len(subset) == largest_size:
            largest_nesting_boxes.append(subset)
            
    num_of_max_nests = len(largest_nesting_boxes)

    return largest_size, num_of_max_nests, largest_nesting_boxes
    

# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])


def subset_nest (subset):
  for i in range(len(subset) - 1):
    if not does_fit(subset[i], subset[i + 1]):
      return False
  return True
    

def main():
  # read the number of boxes 
  in_file = open ('boxes.in', 'r')
  line = in_file.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = in_file.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # close the file
  in_file.close()

  # print to make sure that the input was read in correctly
  print (box_list)
  print()
  
  # sort the box list
  box_list.sort()

  # print the box_list to see if it has been sorted.
  print (box_list)
  print()
  
  # create an empty list to hold all subset of boxes
  all_box_subsets = []

  # create a list to hold a single subset of boxes
  sub_set = []

  # generate all subsets of boxes and store them in all_box_subsets
  sub_sets_boxes(box_list, sub_set, 0, all_box_subsets)

  # initialize the size of the largest sub-set of nesting boxes
  largest_size = 0

  # create a list to hold the largest subsets of nesting boxes
  all_nesting_boxes = []

  # go through all the subset of boxes and only store the
  # largest subsets that nest in all_nesting_boxes
  largest_size, num_of_max_nests, all_nesting_boxes = largest_nesting_subsets(all_box_subsets, largest_size, all_nesting_boxes)

  # print the largest number of boxes that fit
  print(largest_size)
  # print the number of sets of such boxes
  print(num_of_max_nests)

  for subset in all_nesting_boxes:
    for box in subset:
      print(box)
    print()
    

if __name__ == "__main__":
  main()
