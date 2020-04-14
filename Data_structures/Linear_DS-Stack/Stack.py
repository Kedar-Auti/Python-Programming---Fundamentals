

# Stack Data Structures (Last In First Out)

# Push >> Insertion of  an element in stack.
# pop >> Deletion of element from stack.


# A B C D  >> Suppose this are the elements of our stack

# D >>> In this way, elements will look in Stack Data Structure format 
# C
# B
# A

# We knoe that stack works on principle of 'LIFO'
# i.e. Last In First Out 

# Let's crete a class for Data-Structure type - Stack >>

class stack():
	# intialiser block of class-Stack
	def __init__(self):
		self.items = []   # 'items' - attribute is created which is basically an empty list

	def push(self,item):  # This 'push' method will append the 'item' element in empty list named 'items'
		self.items.append(item)  

	def pop(self):	 # This 'pop' method deletes by default last element added in a list which is nothing but a stack
		return self.items.pop() 

	def is_empty(self): # 'is_empty' method will return True if stack i.e. 'Items' named list is empty
		return self.items == []
		 

	def peek(self): # This 'Peek' method will return the last element in the 'items' list.
		if not self.is_empty(): 
			return self.items[-1] 

	def get_stack(self): # It will return all the elements in the stack.
		return self.items 









