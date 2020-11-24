## Problem: In this assignment you will create a simple encryption scheme using a binary search tree. 
# To encode a sentence, insert each letter into a binary tree using the ASCII value as a comparative measure.

# To encode the sentence meet me, start by inserting the letters "m", followed by "e" and followed by "t" into 
# the binary tree. In the first insertion, the binary tree is empty, so "m" becomes the root node of the tree. 
# The "e" is inserted next. Since "e" is less than "m", it becomes the left child of "m" node. The second "e" is 
# not inserted as there is an "e" in the tree already. The "t" becomes the right child of the "m" node. The next
# character is the space character and is considered less than any letter and becomes the left most leaf.

# To encode, use the following convention: assign the root node of the tree a "*" character. Every other character 
# in the tree, assign a character string based on how many "lefts" and how many "rights" are involved in the tree 
# traversal. For "left" traversals, use a "<", for "right" traversals use a ">". In the above example, "e" will be 
# represented as "<" and "t" will become ">". The space character will become "<<". To complete the code, every 
# character must be separated by a marker called the delimiter. Use "!" (the exclamation mark) as a delimiter for the code.

# Using these conventions, the string "meet me" when encrypted becomes "*!<!<!>!<<!*!<". 
# The encryption key for this assignment is "the quick brown fox jumps over the lazy dog".



import sys
class Node (object):
  def __init__ (self, ch):
    self.ch = ch
    self.lchild = None
    self.rchild = None

class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__ (self, encrypt_str):
        self.root = Node(encrypt_str[0])
        for c in encrypt_str[1:]:
            self.insert(c)
    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert (self, ch):
        new_node = Node(ch)
        if self.root == None:
            self.root = new_node
            return
        # Get parent of new_node
        current = self.root
        parent = self.root
        while current != None:
            parent = current
            if current.ch == ch:
                return
            elif ch < current.ch:
                current = current.lchild
            else:
                current = current.rchild
        # Insert new_node
        if ch < parent.ch:
            parent.lchild = new_node
            return
        parent.rchild = new_node


    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search (self, ch):
        string = ''
        current = self.root
        if current.ch == ch:
            return '*'
        while current != None and current.ch != ch:
            if ch < current.ch:
                string += '<'
                current = current.lchild
            else:
                string += '>'
                current = current.rchild
        return string


    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding 
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse (self, st):
        current = self.root
        for c in st:
            if c == '*':
                return current.ch
            elif c == '<':
                current = current.lchild
            elif c == '>':
                current = current.rchild
        return current.ch


    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt (self, st):
        encrypted_string = ''
        ignore = ''
        for i in range(33, 65):
            ignore += chr(i)
        st = st.lower().strip(ignore)

        # Create tree
        for c in st:
            self.insert(c)

        # Get string
        for c in st:
            encrypted_string += self.search(c)
            encrypted_string += '!'

        return encrypted_string[:-1]


    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt (self, st):
        decrypted_string = ''
        st = st.split('!')
        for c in st:
            decrypted_string += self.traverse(c)
        return decrypted_string


def main():
    # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()

    # create a Tree object
    the_tree = Tree (encrypt_str)

    # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()

    # print the encryption
    print (the_tree.encrypt(str_to_encode))

    # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()
  
    # print the decryption
    print (the_tree.decrypt(str_to_decode))
 
if __name__ == "__main__":
    main()