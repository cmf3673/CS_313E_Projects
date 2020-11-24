## Problem: Given an m by n grid of letters, and a list of words, 
# find the location in the grid where the word can be found. 
# A word matches a straight, contiguous line of letters in the grid. 
# The match could either be done horizontally (left or right) or vertically 
# (up or down). It is not guaranteed that every word in the grid has the 
# same orientation and direction. Moreover the word may not exist in the grid.



def read_input():
    # open file to read
    in_file = open('word.in', 'r')
    # read m and n
    coords = in_file.readline().strip().split()
    m = int(coords[0])
    n = int(coords[1])

    # skip blank line
    in_file.readline()

    # read the grid of characters
    word_grid = []
    for _ in range(m):
        word_grid.append(list(map(lambda x: x[0], in_file.readline().rstrip().split())))

    # skip blank line
    in_file.readline()
    k = int(in_file.readline().strip())

    # read the list of words
    word_list = []
    for _ in range(k):
        word_list_item = in_file.readline().strip()
        word_list.append(word_list_item)
    
    # close the input file
    in_file.close()

    return word_grid, word_list

def main():
    # read input from file
    word_grid, word_list = read_input()

    #### do NOT change anything above this line ####
    #### make changes in this section only      ####

    # call word_search() using the word_grid and word_list parameters
    for word in word_list:
        word_coordinates = word_search(word_grid, word)
        print(str(word_coordinates[0]) + " " + str(word_coordinates[1]))
    

#  Input: word_grid is a 2-D list of characters
#         word_to_search is a SINGLE word to look for in the word_grid
#  Output: function RETURNS a TUPLE representing the
#          indices (row, col) of the first letter of the word_to_search
#          if word does not exist, return (-1, -1)
def word_search (word_grid, word_to_search):
    # Begins by iterating through each letter in thew word grid.
    # Deltas: Up, Top Right, Right, Bottom Right, Down, Bottom Left, Left, Top Right.
    word_coordinates = (-1, -1)
    deltas = [[-1,  0], [-1,  1], 
              [ 0,  1], [ 1,  1], 
              [ 1,  0], [ 1, -1], 
              [ 0, -1], [-1, -1]]
    for i in range(len(word_grid)):
        for j in range(len(word_grid[i])):
            # Simple Case: find the one letter word.
            if word_grid[i][j] == word_to_search:
                return (i, j)

            # The word is not one letter and its vertical,
            # horizontal, or diagonal.
            if word_grid[i][j] == word_to_search[0]:
                word_coordinates = (i, j)
                # Now, check the neighboring letters.
                for delta in deltas:
                    current_str = ''
                    row = i
                    col = j
                    current_location = [row + delta[0], col + delta[1]]
                    if inbounds(word_grid, current_location[0],
                        current_location[1]):
                        if (word_grid[current_location[0]][current_location[1]]
                         == word_to_search[1]):
                            # Gets string from word_grid, so it can
                            # get checked against the word.
                            while inbounds(word_grid, row, col):
                                current_str += word_grid[row][col]
                                row += delta[0]
                                col += delta[1]
                                if current_str == word_to_search:
                                    return word_coordinates       
    # The word was not found.            
    return (-1, -1)


# This function checks to make sure the checker is inbounds.
def inbounds(word_grid, row, col):
    return (0 <= row < len(word_grid)) and (0 <= col < len(word_grid[row]))


# This function stress tests the main function and 
# its helper functions.
def test_cases():
    print('***STARTING TEST CASES***')
    # Basic tests 
    assert word_search([['a']], 'a') == (0, 0)
    
    assert word_search([['a']], 'z') == (-1, -1)
    assert word_search([['i', 't'], ['n', 'o']], 'to') == (0, 1)
    assert word_search([['i', 't'], ['n', 'o']], 'it') == (0, 0)
    # Given test
    assert word_search([['a', 'b', 'c', 'd', 'e', 'f'],['h', 'c', 'a', 'r', 'a', 'a'],['h', 'i', 'p', 'p', 'o', 'x']], 'car') == (1, 1)
    # Vertical grid

    # Bigger word_grid
    assert word_search([['a', 'd', 'l'],['p', 'a', 'q'],['p', 't', 'b']], 'app') == (0,0)
    assert word_search([['a', 'c', 't'],['o', 'a', 't'],['p', 't', 'b']], 'act') == (0,0)
    # Small diag. AND horz. 
    assert word_search([['i', 't'], ['o','n']], 'in') == (0, 0)
    # Backwards diagonal
    assert word_search([['t', 'd', 'm'],['p', 'a', 'e'],['p', 't', 'c']], 'cat') == (2, 2)
    # Backwards diag.
    assert word_search([['a', 'b', 'd'],['d', 'o', 'f'],['g', 'h', 'i']], 'dog') == (0, 2)
    # Backwards horz. AND backwards diag.
    assert word_search([['a', 'd', 'm'],['p', 'e', 'e'],['g', 't', 'x']], 'meg') == (0, 2)

    # Stress Test: Words in neighboring areas where it SHOULD be out of bounds.
    assert word_search([['A', 'B', 'C', 'D', 'E', 'F'], ['G', 'H', 'I', 'J', 'K', 'L'], ['X', 'N', 'O', 'P', 'Q', 'R']], 'AX') == (-1, -1)
    assert word_search([['W', 'W', 'P', 'A'], ['A', 'W', 'A', 'W'], ['W', 'A', 'W', 'A']], 'WAP') == (2,2)
    print('**ALL TESTS PASSED**')


#################### do not change anything below this line ###################

if __name__ == "__main__":
    main()




