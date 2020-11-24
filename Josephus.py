## Problem: The problem that you are going to solve is known as Josephus problem and it is stated as follows. 
# There is a group of soldiers surrounded by an overwhelming enemy force. There is no hope for victory without 
# reinforcements, so they make a pact to commit suicide.

# They form a circle and a number n is picked from a hat. One of their names is picked at random. 
# Beginning with the soldier whose name is picked, they begin to count clockwise around the circle. 
# When the count reaches n, that soldier is executed, and the count begins again with the next man. 
# The process continues so that each time the count reaches n, a man is removed from the circle. Once 
# a soldier is removed from the circle he is no longer counted. The last soldier remaining was supposed 
# to take his own life. According to legend the last soldier remaining was Josephus and instead of taking 
# his own life he joined the enemy forces and survived.

# The problem is: given a number n, the ordering of the men in the circle, and the man from whom the count begins, 
# to determine the order in which the men are eliminated from the circle and which man escapes. For example, suppose 
# that n equals 3 and there are five men named A, B, C, D, and E. We count three men, starting at A, so that C is 
# eliminated first. We then begin at D and count D, E, and back to A, so that A is eliminated next. Then we count B, 
# D, and E (C has already been eliminated) and finally B, D, and B, so that D is the man who escapes.

# You will use a circular linked list. You have worked on the linear linked list in your previous home work. 
# To make a circular linked list you need to make the next field in the last link of the linked list point 
# back to the first link instead of being null. From any point in a circular list it is possible to reach any 
# other point in the list. Thus any link can be the first or last link. One useful convention is to let the 
# external pointer to the circular list point to the last link and to allow the following link be the first link. 
# We also have the convention that a null pointer represents an empty circular list.

# Instead of giving the soldiers names you will assign them numbers serially starting from 1 (one). This way you can 
# use the Link class that we discussed. In your program you will read the data from a file called josephus.in. 
# The first line gives the number of soldiers. The second line gives the soldier from where the counting starts. 
# The third line gives the elimination number.

# You will create a circular linked list having the number of soldier specified. 
# Your program will print out the order in which the soldiers get eliminated.


import sys
class Link(object):
  
  def __init__(self, data):
    self.data = data
    self.next = None

  def __str__(self):
    return str(self.data)

class CircularList(object):
  # Constructor
  def __init__(self): 
    self.first = None 
    self.last = None 
		
  # Insert an element (value) in the list
  def insert(self, data):
    new = Link(data)
    if self.first == None:
      self.first = new 
      self.last = new
    self.last.next = new
    self.last = new
    self.last.next = self.first

  # Find the link with the given data (value)
  def find(self, data):
    current = self.first
    while current != self.last:
      if current.data == data:
        return current
      current = current.next 
    if self.last.data == data:
      return self.last
    return None

  # Delete a link with a given data (value)
  def delete(self, data):
    # Find.
    current = self.first
    # While not at the last link.
    while current != self.last:
      # If the last link is element.
      if current.next == self.last and current.next.data == data:
        self.last = current
        break
      # If find link in middle.
      elif current.next.data == data:
        break
      current = current.next
    else:
      # If first link is not element, link not found.
      if current.next.data != data:
        return None
      else:
        self.first = current.next.next

    # Reassign.
    deleted_link = current.next
    current.next = current.next.next
    return deleted_link
		
  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def delete_after(self, start, n):
    # Get to start
    current = self.first
    while current.data != start:
      current = current.next
    
    # get to link to delete
    i = 1
    while i != n:
      i += 1
      current = current.next

    # Delete link
    deleted_link = current
    self.delete(current.data)
    print(deleted_link)
    return current.next
     
  # Return a string representation of a Circular List
  def __str__(self):
    line = ''
    current = self.first
    while current != self.last:
      line += str(current) + '> '
      current = current.next
    line += str(self.last)
    return line + '> ' + str(self.first) + '> ' + str(self.first.next) + '>...'


def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int(line)
  
  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int(line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int(line)

  # your code
  circle = CircularList()
  # Add to circle
  for i in range(1, num_soldiers + 1):
    circle.insert(i)

  for i in range(num_soldiers):
    start_count = circle.delete_after(start_count, elim_num)
    start_count = start_count.data

	#########################
	# Testing circular list
    
  # 1. Test insert
  print()
  print('Test insert')
  CirList = CircularList()
  for i in range(12):
    CirList.insert(i)
  print(CirList)
  print(f'first: {CirList.first}')
  print(f'last: {CirList.last}')
  print()
  print()

  # 2. Test delete 
  print('Test delete.')
  print('delete 5')
  CirList.delete(5)
  print('delete 11')
  CirList.delete(11)
  print('delete 0')
  CirList.delete(0)
  print()
  print(CirList)
  print(f'first: {CirList.first}')
  print(f'last: {CirList.last}')
  print()
  print()

  # 3. Test find
  print('Test find.')
  print(CirList.find(1))
  print(CirList.find(300))
  print(CirList.find(10))
  print(CirList.find(4))
  print()
  print()

  # 4. Test delete_after 
  print('Test delete_after.')
  print('deleting the 5th link (6)..')
  CirList.delete_after(0, 5)
  print(CirList)
  print('deleting the 20th link (4)..')
  CirList.delete_after(0, 20)
  print(CirList)


if __name__ == "__main__":
  main()