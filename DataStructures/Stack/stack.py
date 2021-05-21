"""Implement a stack and test its functions"""

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    
    
class Stack:
  def __init__(self):
    self.nodes = []
    self.size = 0
    
  def peek(self):
    print(self.nodes[self.size - 1])
    
  
  def pop(self):
     node = self.nodes[self.size - 1]
    return 
  
  def push(self):
    pass
