"""Class to implement a linked list and test the functions"""

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
    self.listSize = 0
    
  def addNode(self,node):
    if (self.head is None):
      self.head = node
      self.listSize = 1
    else:
      n = self.head
      while(n.next != None):
        n = n.next
      n.next = node
      listSize += 1
  
  def printList(self):
    node = self.head
    while(node != None):
      print(node.data, sep=" ")
      node = node.next
      
  def getSize(self):
    return self.listSize
  
  
      
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

ll = LinkedList()
ll.addNode(n1); ll.addNode(n2); ll.addNode(n3); ll.addNode(n4)

