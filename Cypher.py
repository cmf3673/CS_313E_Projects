## Problem: Here is a simple and clever way to encrypt plain text. 
# Assume that the message contains only upper case and lower case letters 
# and digits from a to z. Let L be the length of the original message, and 
# M the smallest square number greater than or equal to L. Add (M-L) asterisks 
# to the message, giving a padded message with length M. Use the padded message 
# to fill a table of size K x K, where K**2 = M. Fill the table in row-major order 
# (left to right in each column, top to bottom for each row).

# Now to encrypt, rotate the table 90° clockwise. The encrypted message comes from 
# reading the message in row-major order from the rotated table, omitting any asterisks.



import math
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string
def encrypt (strng):
    # Create new string (with '*')
    new_string = add_astricks(strng)
    # Package updated string into nxn matrix (s.t. n**2 = req_len)
    mat = get_initial_mat(new_string)
    # Create encrypted string 
    encr_str = get_encr_string(mat, False)
    return encr_str


# Adds astricks until the len of string is a perfect square. 
def add_astricks(string):
    while math.sqrt(len(string)) % 1 != 0:
        string += '*'
    return string 


# Populates a nxn mat with the chars of a string.
def get_initial_mat(new_string):
    str_num = 0
    n = int(math.sqrt(len(new_string)))
    initial_mat = [['.' for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            initial_mat[i][j] = new_string[str_num]
            str_num += 1
    return initial_mat


# Gets encrypted string from the matrix.
def get_encr_string(mat, keep_astrick):
    encr_str = ''
    for col in range(len(mat)):
        for row in range(len(mat) - 1, -1, -1):
            if keep_astrick or mat[row][col] != '*':
                encr_str += mat[row][col]
    return encr_str


# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt (strng):
    # Get nxn matrix dimensions.
    n = int(math.sqrt(len_req(strng)))
	# Get astricks matrix.
    astricks_mat = get_astricks_mat(n, len(strng))
    # Put string into astricks matrix.
    d_mat = create_mat(astricks_mat, strng)
    # Get message from matrix.
    decry_str = get_decry_str(d_mat)
    return decry_str

# Gets the length of the word with astricks added. 
def len_req(string):
    return len(add_astricks(string))

# Creates and rotates a matrix of dashes and astricks.
def get_astricks_mat(n, string_len):
    astricks_mat = [['-' for j in range(n)] for i in range(n)]
    num_of_astricks = n**2 - string_len

    # Create matrix.
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if num_of_astricks > 0:
                astricks_mat[i][j] = '*'
                num_of_astricks -= 1
    print(astricks_mat)

    # Rotate matrix.
    r_string = get_encr_string(astricks_mat, True)
    astricks_mat = get_initial_mat(r_string)
    print(astricks_mat)
         
    return astricks_mat

# Creates and rotates a matrix to prepare to decrypt. 
def create_mat(astricks_mat, string):
    # Add letters
    str_count = 0
    for i in range(len(astricks_mat)):
        for j in range(len(astricks_mat[i])):
            if astricks_mat[i][j] != '*':
                astricks_mat[i][j] = string[str_count]
                str_count += 1 
    print(astricks_mat)
    
    # Rotate 3 times 
    # 1
    first_str = get_encr_string(astricks_mat, True)
    # 2, 3
    for num in range(3):
        d_mat = get_initial_mat(first_str)
        first_str = get_encr_string(d_mat, True)
    print(d_mat)
    return d_mat


def get_decry_str(d_mat):
    string = ''
    for i in range(len(d_mat)):
        for j in range(len(d_mat[i])):
            if d_mat[i][j] != '*':
                string += d_mat[i][j]
    return string


def test_cases():
    print('Testing....')
    # --Testing encrypt()--
    # Given cases. 
    assert encrypt('gonewiththewind') == 'itwgnhiodetnwhe'
    assert encrypt('thecontestisover') == 'osotvtnheitersec'
    # Single letter.
    assert encrypt('a') == 'a'
    # Misc. 
    assert encrypt('letsdoit') == 'isltdeot'
    assert encrypt('aaaaaaaaaa') == 'aaaaaaaaaa'
    # Lots of '*'
    assert encrypt('helloiamincs') == 'iohniecalsml'

    # --Testing decrypt()--
    # Given cases.
    assert decrypt('itwgnhiodetnwhe') == 'gonewiththewind'
    assert decrypt('osotvtnheitersec') == 'thecontestisover'
    # Single letter. 
    assert decrypt('c') == 'c'
    # Misc.
    assert decrypt('isltdeot') == 'letsdoit'
    assert decrypt('aaaaaaaaaa') == 'aaaaaaaaaa'
    # Lots of '*'
    assert decrypt('iohniecalsml') == 'helloiamincs'
    print('Passed all tests!')

def main():
    # read the strings P and Q from standard input
    P = input()
    Q = input()
    encrypt(P)
    # encrypt the string P
    encrypted_P = encrypt(P)
    # decrypt the string Q
    decrypted_Q = decrypt(Q)
    # print the encrypted string of P
    # and the decrypted string of Q
    print(encrypted_P)
    test_cases()
    print(decrypted_Q)


if __name__ == "__main__":
  main()





