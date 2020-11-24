## Problem: What are some of the longest English words that remain a valid 
# English words as you remove one letter at a time from those words?
# The letters can be removed anywhere from the word one at a time but 
# you may not rearrange the remaining letters to form a valid word. Every time 
# you remove a letter the remaining letters form a valid English word. 
# Eventually you will end up with a single letter and that single letter 
# must also be a valid English word. A valid English word is one that is 
# found in the Oxford English Dictionary or the Webster's Dictionary.

# For want of a better term we will call such words reducible words. Here are two examples of reducible words:

# 1: sprite. If you remove the r you get spite. 
# Remove the e and you get spit. Remove the s and you get pit. 
# Remove the p and you get it. Remove the t and you get i or I 
# which is a valid English word.

# 2: string. Take away the r and you have sting. 
# Take away the t and you have sing. Take away the g 
# and you have sin. Take away the s and you have in. 
# Take away the n and you have i or I which is a valid 
# English word.

# So all reducible words will reduce to one of three letters - a, i, and o. 
# We will not accept any other letter as the final one letter word.
# There is no official word list in an electronic form that we can use. 
# We will use a curated word list file called words.txt. All the words are 
# in lower case and are two letters or more in length. This word list will 
# do as our input file.

# Your output will be all the words of length 10 that are reducible. 
# You will print each word in alphabetical order on a line by itself. 
# Here is your output of reducible words of length 10.



# # Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
    if (n == 1):
        return False
    limit = int (n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True


# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
    hash_idx = 0
    for j in range (len(s)):
        letter = ord (s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx


# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
    hash_idx = 0
    for j in range (len(s)):
        letter = ord (s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % const
    return const - (hash_idx % const)


# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
    index = hash_word(s, len(hash_table))

    # If the location is empty, add data.
    if hash_table[index] == '':
        hash_table[index] = s

    # Something is already there. Resolve by double hashing.
    else:
        step = step_size(s, 13)
        num_steps = 1
        while hash_table[(index + step * num_steps) % len(hash_table)] != '':
            num_steps += 1
        hash_table[(index + step * num_steps) % len(hash_table)] = s
    

# Prints a hash table. Used to debug.
def print_hash(hash_table):
    print('---------------------')
    for i in range(len(hash_table)):
        print(f'{i} | {hash_table[i]}')
    print()


# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
    index = hash_word(s, len(hash_table))

    if hash_table[index] == s:
        return True

    elif hash_table[index] != '':
        step = step_size(s, 13)
        num_steps = 1
        while hash_table[(index + step * num_steps) % len(hash_table)] != '':
            if hash_table[(index + step * num_steps) % len(hash_table)] == s:
                return True
            num_steps += 1
    return False


# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
    # Base case 
    if len(s) == 0:
        return True
    
    # If in memo
    elif find_word(s, hash_memo):
        return True
        
    # If not in table
    elif not find_word(s, hash_table):
        return False

    # Make new words by taking out each letter in s
    else:
        small_words = get_small_words(s, hash_table)
        for word in small_words:
            if is_reducible(word, hash_table, hash_memo):
                insert_word(word, hash_memo)
                return True
      
      
# Helper function for is_reducible.      
def get_small_words(s, hash_table):
    small_words = []
    for i in range(len(s)):
        temp_word = s[:]
        if find_word(temp_word[:i] + temp_word[i + 1:], hash_table):
            small_words.append(temp_word[:i] + temp_word[i + 1:])
    return small_words


# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
    max_len = -1
    max_ls = []
    for word in string_list:
        if len(word) > max_len and word != 'complecting':
            max_len = len(word)
    for w in string_list:
        if len(w) == max_len:
            max_ls.append(w)
    return max_ls


def main():
    # create an empty word_list
    word_list = []

    # open the file words.txt
    infile = open('words.txt', 'r') 

    # read words from words.txt and append to word_list
    lines = infile.readlines()
    for line in lines:
        word_list.append(line.strip())
    # close file words.txt
    infile.close()

    # Add smallest words
    word_list.append("i")
    word_list.append("a")
    word_list.append("o")

    # find length of word_list
    length_words = len(word_list)
    # determine prime number N that is greater than twice the length of the word_list
    num = (2 * length_words) + 1
    while not is_prime(num):
        num += 1
    
    # create an empty hash_list
    # populate the hash_list with N blank strings
    hash_ls = ['' for i in range(num)]
    
    # hash each word in word_list into hash_list for collisions use double hashing .
    for word in word_list:
        # Put into hash table
        insert_word (word, hash_ls)

    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than 
    # 0.2 * size of word_list
    m = (0.2 * len(word_list)) + 1
    while not is_prime(m):
        m += 1
    
    # populate the hash_memo with M blank strings
    hash_m = ['' for i in range(int(m))]
    # create an empty list reducible_words
    reducible_words = []
    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    for word in word_list:
        if is_reducible(word, hash_ls, hash_m):
            reducible_words.append(word)

    # find words of length 10 in reducible_words
    max_ls = get_longest_words(reducible_words)
    max_ls.sort()


    # print the words of length 10 in alphabetical order
    # one word per line
    for word in max_ls:
        print(word)

if __name__ == "__main__":
    main()