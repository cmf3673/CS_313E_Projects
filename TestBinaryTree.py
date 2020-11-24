## Problem: In this assignment you will be adding to the classes Node and Tree 
# that we developed in class and testing them. There are several short methods 
# that you will have to write.

# Write a method is_similar() that takes as input two binary search trees and 
# returns true if the nodes have the same key values and are arranged in the 
# same order and false otherwise.

# Write a method print_level() that takes as input the level and prints out all 
# the nodes at that level. If that level does not exist for that binary search 
# tree it prints nothing. Use the convention that the root is at level 1.

# Write a method get_height() that returns the height of a binary search tree. 
# Recall that the height of a tree is the longest path length from the root to a leaf.

# Write a method num_nodes() that returns the number of nodes in the left subtree 
# from the root and the number of nodes in the right subtree from the root and the 
# root itself. This function will be useful to determine if the tree is balanced.



import sys
class Node (object):
    def __init__ (self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
    
    def __str__(self):
        return str(self.data)

class Tree (object):
    def __init__ (self):
        self.root = None

    # Insert data into the tree
    def insert (self, data):
        new_node = Node (data)

        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (data < current.data):
                    current = current.lchild
                else:
                    current = current.rchild

            # found location now insert node
            if (data < parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node

    # Returns true if two binary trees are similar
    def is_similar (self, pNode):
        def is_similar_recursive(node1, node2):
            if node1 == None and node2 == None:
                return True
            elif node1 == None or node2 == None:
                return False
            elif node1.data != node2.data:
                return False
            return is_similar_recursive(node1.rchild, node2.rchild) and is_similar_recursive(node1.lchild, node2.lchild)
        return is_similar_recursive(self.root, pNode.root)

    # Prints out all nodes at the given level
    def print_level (self, level): 
        def print_level_recursive(node, current_level, level):
            if node != None:
                if current_level == level:
                    print(node, end = ' ')
                else:
                    print_level_recursive(node.lchild, current_level + 1, level)
                    print_level_recursive(node.rchild, current_level + 1, level)
        print_level_recursive(self.root, 1, level)
        
    # Returns the height of the tree
    def get_height (self): 
        def get_height_recursive(node):
            if node == None:
                return 0
            return 1 + max(get_height_recursive(node.lchild), get_height_recursive(node.rchild))
        return get_height_recursive(self.root)

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):
        def num_nodes_recursive(node):
            if node == None:
                return 0
            return 1 + num_nodes_recursive(node.lchild) + num_nodes_recursive(node.rchild)
        return num_nodes_recursive(self.root)
            

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line)) 	# converts elements into ints
    tree1 = Tree()
    # Insert elements
    for i in tree1_input:
        tree1.insert(i)

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list (map (int, line)) 	# converts elements into ints
    tree2 = Tree()
    # Insert elements
    for i in tree2_input:
        tree2.insert(i)

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list (map (int, line)) 	# converts elements into ints
    tree3 = Tree()
    # Insert elements
    for i in tree3_input:
        tree3.insert(i)

    # Test your method is_similar()
    print(f'Trees 1 and 2 are the same? {tree1.is_similar(tree2)}.') # True
    print(f'Trees 2 and 3 are the same? {tree2.is_similar(tree3)}.') # False
    print()

    # Print the various levels of two of the trees that are different
    print('Tree 1: first 4 levels')
    tree1.print_level(1)
    print()
    tree1.print_level(2)
    print()
    tree1.print_level(3)
    print()
    tree1.print_level(4)
    print()
    print()

    print('Tree 3: first 3 levels')
    tree3.print_level(1)
    print()
    tree3.print_level(2)
    print()
    tree3.print_level(3)
    print()
    print()

    # Get the height of the two trees that are different
    print(f'Tree 1 height: {tree1.get_height()}.')
    print(f'Tree 3 height: {tree3.get_height()}.')
    print()

    # Get the total number of nodes a binary search tree
    print(f'Number of nodes in tree 1: {tree1.num_nodes()}.')
    print(f'Number of nodes in tree 2: {tree2.num_nodes()}.')
    print(f'Number of nodes in tree 3: {tree3.num_nodes()}.')

if __name__ == "__main__":
  main()