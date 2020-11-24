## Problem: In this assignment you will be writing helper methods for the 
# LinkedList class that we developed and test them. The following is the 
# outline of the code that you will be submitting. For the time being assume 
# that the data that you are handling are integers.



import random
class Link (object):

  def __init__ (self, data, nextLink = None):
    self.data = data
    self.nextLink = nextLink
  
  def __str__ (self):
    return str(self.data)


class LinkedList (object):
  # create a linked list
  def __init__ (self):
    self.first = None
    self.last = None


  # get number of links 
  def get_num_links (self):
    num = 0
    current = self.first
    while current != None:
      current = current.nextLink
      num += 1
    return num 
    

  # add an item at the beginning of the list
  def insert_first (self, data): 
    new_link = Link(data)
    if self.first == None:
      self.last = new_link
    
    new_link.nextLink = self.first
    self.first = new_link
    

  # add an item at the end of a list
  def insert_last (self, data): 
    new_link = Link(data)
    if self.first == None:
      self.first = new_link
      self.last = new_link
    else:
      self.last.nextLink = new_link
      self.last = new_link


  # add an item in an ordered list in ascending order
  def insert_in_order (self, data): 
    new_link = Link(data)
    if self.first == None or new_link.data < self.first.data:
      self.insert_first(data)
    elif new_link.data > self.last.data:
      self.insert_last(data)
    else:
      current = self.first
      while current != self.last and new_link.data > current.nextLink.data:
        current = current.nextLink 
      new_link.nextLink = current.nextLink
      current.nextLink = new_link
    

  # search in an unordered list, return None if not found
  def find_unordered (self, data): 
    current = self.first 
    while current != None:
      if current.data == data:
        return current
      current = current.nextLink 
    return None


  # Search in an ordered list, return None if not found
  def find_ordered (self, data): 
    current = self.first
    while current != None and current.data <= data:
      if current.data == data:
        return current
      current = current.nextLink
    return None
    

  # Delete and return Link from an unordered list or None if not found
  def delete_link (self, data):
    if self.first.data == data:
        link = self.first
        self.first = self.first.nextLink
        return link

    current = self.first
    while current != self.last:
      if current.nextLink.data == data and current.nextLink == self.last:
        link = self.last
        current.nextLink = None
        self.last = current
        return link
      elif current.nextLink.data == data:
        link = current.nextLink 
        current.nextLink = current.nextLink.nextLink
        return link
      current = current.nextLink
    return None


  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    if self.first == None:
        return 'Empty list'
    i = 0
    string = ''
    current = self.first
    while current != None:
      if i == 10:
        string += '\n'
      string += str(current.data) + '  '
      i += 1
      current = current.nextLink
    return string 


  # Copy the contents of a list and return new list
  def copy_list (self):
    copy = LinkedList()
    current = self.first
    while current != None:
      copy.insert_last(current.data)
      current = current.nextLink
    return copy


  # Reverse the contents of a list and return new list
  def reverse_list (self): 
    copy = LinkedList()
    current = self.first
    while current != None:
      copy.insert_first(current.data)
      current = current.nextLink
    return copy


  # Sort the contents of a list in ascending order and return new list
  def sort_list (self): 
    ls = []
    sorted_copy = LinkedList()
    current = self.first
    while current != None:
      ls.append(current.data)
      current = current.nextLink
    ls.sort()
    for data in ls:
        sorted_copy.insert_last(data)
    return sorted_copy
    

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    current = self.first
    while current != self.last:
      if current.data > current.nextLink.data:
        return False
      current = current.nextLink
    return True 


  # Return True if a list is empty or False otherwise
  def is_empty (self): 
    if self.first == None:
      return True
    else:
      return False
    

  # Merge two sorted lists and return new list in ascending order
  def merge_list (self, other): 
    new_ls = LinkedList()
    current1 = self.first
    current2 = other.first 

    while current1 != None:
      new_ls.insert_last(current1.data)
      current1 = current1.nextLink
    while current2 != None:
      new_ls.insert_last(current2.data)
      current2 = current2.nextLink
    
    return new_ls.sort_list()


  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    if self.get_num_links() != other.get_num_links():
      return False
    current1 = self.first
    current2 = other.first
    while current1 != None and current2 != None: 
      if current1.data != current2.data:
        return False
      current1 = current1.nextLink
      current2 = current2.nextLink
    return True
      

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def remove_duplicates (self):
    data_set = set()
    new_ll = LinkedList()
    current = self.first
    while current!= None:
      if current.data not in data_set:
        # Add to set
        data_set.add(current.data)
        # Add to new ll
        new_ll.insert_last(current)
      current = current.nextLink
    return new_ll


def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
  LinkLS = LinkedList()
  for i in range(20):
    LinkLS.insert_first(i)
  print(f'list: {LinkLS}')
  print(f'first: {LinkLS.first}')
  print(f'last: {LinkLS.last}')
  print()

  
  # Test method insert_last()
  LinkLS = LinkedList()
  for i in range(20):
    LinkLS.insert_last(i)
  print(f'list: {LinkLS}')
  print(f'first: {LinkLS.first}')
  print(f'last: {LinkLS.last}')
  print()


  # Test method insert_in_order()
  LinkLS.insert_in_order(-20)
  LinkLS.insert_in_order(13)
  LinkLS.insert_in_order(1.3)
  print('inserted -20 in order')
  print('inserted 13 in order')
  print('inserted 1.3 in order')

  print(f'list: {LinkLS}')
  print(f'first: {LinkLS.first}')
  print(f'last: {LinkLS.last}')


  # Test method get_num_links()
  print(f'num of links: {LinkLS.get_num_links()}')
  print()


  # Test method find_unordered() 
  # Consider two cases - data is there, data is not there 

  UnLinkLS = LinkedList()
  ls = [1, 5, 3, 8, 20, -345, 71]
  for e in ls:
    UnLinkLS.insert_first(e)
  print(f'list: {UnLinkLS}')
  print()

   # Case 1: data is there:
  print(f'prints 20 if found: {UnLinkLS.find_unordered(20)}')
  print(f'prints -345 if found: {UnLinkLS.find_unordered(-345)}')
  print(f'prints 71 if found: {UnLinkLS.find_unordered(71)}')

  # Case 2: data is not there:
  print(f'prints 21 if found: {UnLinkLS.find_unordered(21)}')
  print(f'prints 0 if found: {UnLinkLS.find_unordered(0)}')
  print()
  

  # Test method find_ordered() 
  # Consider two cases - data is there, data is not there 
  ordered_ls = LinkedList()
  ls = [-8, -1, 0, 7, 12, 30, 72, 73, 105]
  for e in ls:
    ordered_ls.insert_last(e)
  print(f'list: {ordered_ls}')
  print()

  # Case 1: data is there: 
  print(f'prints -1 if found: {ordered_ls.find_ordered(-1)}')
  print(f'prints 12 if found: {ordered_ls.find_ordered(12)}')
  print(f'prints 105 if found: {ordered_ls.find_ordered(105)}')
  print(f'prints -8 if found: {ordered_ls.find_ordered(-8)}')

  # Case 2: data is not there: 
  print(f'prints -2 if found: {ordered_ls.find_ordered(-2)}')
  print(f'prints 71 if found: {ordered_ls.find_ordered(71)}')
  print()


  # Test method delete_link()
  # Consider two cases - data is there, data is not there 
  print(f'list: {ordered_ls}')

  # Case 1: data is there:
  print('deleting 7...')
  print(f'should print 7: {ordered_ls.delete_link(7)}')
  print(f'list: {ordered_ls}')
  print()
  print('deleting 105...')
  print(f'should print 105: {ordered_ls.delete_link(105)}')
  print(f'list: {ordered_ls}')
  print()
  print('deleting -8...')
  print(f'should print -8: {ordered_ls.delete_link(-8)}')
  print(f'list: {ordered_ls}')
  print()
  print(f'new first: {ordered_ls.first} ')
  print(f'new last: {ordered_ls.last}') 
  print()

  # Case 2: data is not there:
  print('deleting 105...')
  print(f'should print None: {ordered_ls.delete_link(105)}')
  print(f'list: {ordered_ls}')
  print()


  # Test method copy_list()
  ls = [1, 8, 10, -200, -1, 0, 3, 8]
  Link_ls = LinkedList()
  for e in ls:
    Link_ls.insert_last(e)
  print(f'list: {Link_ls}')
  print(f'first: {Link_ls.first}')
  print(f'last: {Link_ls.last}')
  copy = Link_ls.copy_list()
  print(f'copy: {copy}')
  print(f'copy first: {copy.first}')
  print(f'copy last: {copy.last}')
  print()

  Link_ls = LinkedList()
  print(f'list: {Link_ls}')
  print(f'first: {Link_ls.first}')
  print(f'last: {Link_ls.last}')
  copy = Link_ls.copy_list()
  print(f'copy: {copy}')
  print(f'copy first: {copy.first}')
  print(f'copy last: {copy.last}')
  print()


  # Test method reverse_list()
  ls = [1, 8, 10, -200, -1, 0, 3, 8]
  Link_ls = LinkedList()
  for e in ls:
    Link_ls.insert_last(e)
  print(f'list: {Link_ls}')
  print(f'first: {Link_ls.first}')
  print(f'last: {Link_ls.last}')
  rev = Link_ls.reverse_list()
  print(f'reversed: {rev}')
  print(f'rev first: {rev.first}')
  print(f'rev last: {rev.last}')
  print()

  Link_ls = LinkedList()
  print(f'list: {Link_ls}')
  print(f'reversed: {Link_ls.reverse_list()}')
  print()


  # Test method sort_list()
  ls = []
  ll = LinkedList()
  for i in range(10):
    ls.append(random.randint(1, 300))
  
  for e in ls:
    ll.insert_first(e)
  print(f'list: {ll}')
  print(f'sorted list: {ll.sort_list()}')
  print()
    

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  # Case 1: Sorted:
  ls = [-1, 1, 2, 3, 4, 7]
  ll = LinkedList()
  for e in ls:
    ll.insert_last(e)

  print(f'is the list sorted? should be true: {ll.is_sorted()}')

  # Case 2: Not sorted:
  ls = [2, 1, 2, 3, 4, 7]
  ll = LinkedList()
  for e in ls:
    ll.insert_last(e)

  print(f'is the list sorted? should be false: {ll.is_sorted()}')
  print()


  # Test method is_empty()
  ll = LinkedList()
  print(f'is ll empty? should be true: {ll.is_empty()}')
  ll.insert_first(8)
  print(f'is ll empty? should be false: {ll.is_empty()}')
  print()


  # Test method merge_list()
  ls1 = [1, 2, 3]
  ls2 = [3, 4, 1]
  ll1 = LinkedList()
  ll2 = LinkedList()
  for e in ls1:
    ll1.insert_last(e)
  for e in ls2:
    ll2.insert_last(e)
  print(f'list 1: {ll1}')
  print(f'list 2: {ll2}')
  print(f'merged: {ll1.merge_list(ll2)}')
  print()


  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal

  # Case 1: equal:
  newLL1 = LinkedList()
  newLL2 = LinkedList()

  ls1 = [1, 8, 9, 10]
  ls2 = [1, 8, 9, 10]
  for e in ls1:
    newLL1.insert_first(e)
  for e in ls2:
    newLL2.insert_first(e)

  print(f'are linked list the same? Should be true: {newLL1.is_equal(newLL2)}')
  print()

  # Case 2: not equal:
  newLL1 = LinkedList()
  newLL2 = LinkedList()

  for e in ls1:
    newLL1.insert_last(e)
  for e in ls2:
    newLL2.insert_first(e)

  print(f'are linked list the same? Should be false: {newLL1.is_equal(newLL2)}')
  print()
  

  # Test remove_duplicates()
  ll = LinkedList()
  ls = [1, 6, 7, 6, 6, 6, 3, 7, 3]
  for e in ls:
    ll.insert_last(e)

  print(f'list: {ll}')
  print(f'list with dup\'s removed: {ll.remove_duplicates()}') 


if __name__ == "__main__":
  main()