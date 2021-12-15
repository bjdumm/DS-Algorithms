from DataStructures/node import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
      print("Adding {} to the stack!".format(value))
    else:
      print("No room for {}!".format(value))

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      print("Popping " + item_to_remove.get_value())
      return item_to_remove.get_value()
    print("Stack is empty.")

  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()
    print("Empty stack")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  
# Defining an empty stack
stack = Stack(6)
# Adding items to stack 
stack.push("First")
stack.push("Second")
stack.push("Third")
stack.push("Fourth")
stack.push("Fifth")
stack.push("Sixth")


stack.push("Seventh")

# Removing items from the top of the stack down
print("The top of the stack is " + stack.peek())
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
