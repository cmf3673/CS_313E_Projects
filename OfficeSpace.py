## Problem: The company that you work for is moving to a larger building. 
# The new office is rectangular and will be subdivided into cubicles. 
# Your employees want to request particular positions for their cubicles. 
# You want to set up a system that lets them make their requests.

# You have expressed the new office space as a coordinate system where each unit is one foot. 
# The south-west corner of this space is assigned the coordinate (0, 0). The positive X axis 
# is aligned with the inner edge of the building's south wall. The positive Y axis is aligned 
# with the west wall. Employees request a position for their cubicle by giving the coordinates 
# of the cubicle's south-west corner and the cubicle's north-east corner.

# Input Format: 
# 33 26
# 3
# Alice 2 3 10 11
# Ted 7 2 18 8
# GreedyBob 17 11 30 24
# Each input starts with a line containing a pair of integers w and h giving the size of the new 
# office space (w is the number of feet west-to-east, h is the number of feet south-to-north). 
# Both of these numbers are in the range 1 to 100.



# Get person-tuple dict and 2D list of 0's of specified dim.
def get_input():
    persons = {}
    dimensions = input().split()
    area = int(dimensions[0]) * int(dimensions[1])
    building = get_matrix(int(dimensions[0]), int(dimensions[1]))
    num_lines = eval(input())
    for i in range(num_lines):
        input_list = input().split()
        name = input_list[0]
        tuple_list = (int(input_list[1]), int(input_list[2]), int(input_list[3]), int(input_list[4]))
        persons[name] = tuple_list
    return area, building, persons


# Creates matrix of zeros of the specified dim.
def get_matrix(dim1, dim2):
    return [[0 for i in range(dim1)] for j in range(dim2)]
    

# Create the main list from which we count the spaces.
def fill_office(building, persons):
    for person in persons: 
        start, end = tuple_splitter(persons[person]) #XD
        print(start, end)
        # Go through the matrix
        for i in range(start[1], end[1]):
            for j in range(start[0], end[0]):
                building[i][j] += 1


# Used for testing. 
def print_mat(building):
    for i in range(len(building)):
        print()
        for j in range(len(building[i])):
            print(building[i][j], end ='')


# Splits a tuple of 4 objects into 2 tuples of 2 objects. 
def tuple_splitter(tuple):
    start = (tuple[0], tuple[1])
    end = (tuple[2], tuple[3])
    return start, end


# Counts unallocated space.
def unallocated_space(building):
    # The counter is the area.
    counter = 0
    for i in range(len(building)):
        for j in range(len(building[i])):
            if building[i][j] == 0:
                counter += 1
    return counter


# Counts contested space.
def contested_space(building):
    # The counter is the area, G.
    counter = 0
    for i in range(len(building)):
        for j in range(len(building[i])):
            if building[i][j] > 1:
                counter += 1
    return counter


# Counts uncontested space for a specified person.
def uncontested_space(building, person_space):
    # CoUnTeR is ThE aREa.
    counter = 0
    start, end = tuple_splitter(person_space)
    for i in range(start[1], end[1]):
        for j in range(start[0], end[0]):
            if building[i][j] == 1:
                counter += 1
    return counter


# Main function.
def main():
    # read the data
    area, building, persons = get_input()

    # run your test cases

    # Fill building 
    fill_office(building, persons)

    # print the following results after computation

    # compute the total office space
    print(f'Total {area}')

    # compute the total unallocated space
    area_unallocated = unallocated_space(building)
    print(f'Unallocated {area_unallocated}')

    # compute the total contested space
    area_contested = contested_space(building)
    print(f'Contested {area_contested}')

    # compute the uncontested space that each employee gets
    for person in persons:
        area = uncontested_space(building, persons[person])
        print(f'{person} {area}')

if __name__ == "__main__":
    main()
