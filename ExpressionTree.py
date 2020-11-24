## Problem: For this assignment you will read a file expression.in and create an expression tree. 
# The expression will be a valid infix expression with the all the necessary parentheses so that 
# there is no ambiguity in the order of the expression. You will evaluate the expression and print 
# the result. You will also write the prefix and postfix versions of the same expression without 
# any parentheses.

# In an expression tree the nodes are either operators or operands. The operators will be in the 
# set ['+', '-', '*', '/', '//', '%', '**']. The operands will be either integers or floating point 
# numbers. All the operand nodes will be leaves of the expression tree. All the operator nodes will 
# have exactly two children.

# You will take the expression string and break it into tokens. 
# There are four different kinds of tokens - left parenthesis, 
# right parenthesis, operator, and operand. When we read a left 
# parenthesis we are starting a new expression and when we read 
# a right parenthesis we are ending an expression.

# For the expression ( ( 8 + 3 ) * ( 7 - 2 ) ), this is what your program will output:

# ( ( 8 + 3 ) * ( 7 - 2 ) ) = 55.0

# Prefix Expression: * + 8 3 - 7 2

# Postfix Expression: 8 3 + 7 2 - *



import sys
class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item on the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack is empty
  def is_empty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))


class Node (object):
    def __init__ (self, data = None, lchild = None, rchild = None):
      self.data = data
      self.lchild = lchild
      self.rchild = rchild
    def __str__ (self):
      return '(' + str(self.data) + ')'


class Tree (object):
  def __init__ (self):
    self.root = Node()

  def create_tree (self, expr):
    operators = {'-', '+', '*', '/', '//', '%', '**'}
    expr = expr.split(' ')
    stack = Stack()
    current = self.root
    for c in expr:    
      if c == '(':
        node = Node()
        current.lchild = node
        stack.push(current)
        current = current.lchild
      elif c in operators:
        current.data = c
        stack.push(current)
        node = Node()
        current.rchild = node
        current = current.rchild
      elif c == ')':
        if not stack.is_empty():
          current = stack.pop()
      elif c != ' ':
        current.data = c
        current = stack.pop()

  def evaluate (self, aNode):
    if aNode.lchild == None and aNode.rchild == None:
      return str(aNode.data)
    else:
      return eval(f'{self.evaluate(aNode.lchild)} {aNode.data} {self.evaluate(aNode.rchild)}')

  def pre_order (self, aNode):
    if aNode.lchild == None and aNode.rchild == None:
      return str(aNode.data)
    else:
      return f'{aNode.data} {self.pre_order(aNode.lchild)} {self.pre_order(aNode.rchild)}'

  def post_order (self, aNode):
    if aNode.lchild == None and aNode.rchild == None:
      return str(aNode.data)
    else:
      return f'{self.post_order(aNode.lchild)} {self.post_order(aNode.rchild)} {aNode.data}'

def main():
  # read infix expression
  line = sys.stdin.readline()
  expr = line.strip()

  # create expression tree
  expr_tree = Tree()
  expr_tree.create_tree(expr)

  # evaluate the expression and print the result
  result = expr_tree.evaluate(expr_tree.root) 
  print(f'{expr} = {float(result)}', end = '\n\n')

  # get the prefix version of the expression and print
  print(f'Prefix Expression: {expr_tree.pre_order(expr_tree.root)}', end = '\n\n')

  # get the postfix version of the expression and print
  print(f'Postfix Expression: {expr_tree.post_order(expr_tree.root)}')

if __name__ == "__main__":
  main()