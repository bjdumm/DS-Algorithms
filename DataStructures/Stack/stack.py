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
      print("Adding {} to the pizza stack!".format(value))
    else:
      print("No room for {}!".format(value))

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      print("Delivering " + item_to_remove.get_value())
      return item_to_remove.get_value()
    print("All out of pizza.")

  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  
# Defining an empty pizza stack
stack = Stack(6)
# Adding pizzas as they are ready until we have 
stack.push("pizza #1")
stack.push("pizza #2")
stack.push("pizza #3")
stack.push("pizza #4")
stack.push("pizza #5")
stack.push("pizza #6")

# Uncomment the push() statement below:
stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + stack.peek())
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
