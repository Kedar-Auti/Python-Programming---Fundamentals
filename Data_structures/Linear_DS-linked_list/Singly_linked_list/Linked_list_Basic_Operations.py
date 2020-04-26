################### Concept of Insertion ###################

# Code for appending the new node to the linked list at end. 	
# Code for prepend the item in linked list.
# Insert after the node

# Node - consists of a 'data elements' & a pointer 'Next'


# class-Node is used for Single individual node consist of data element and pointer-Next.
class Node: 
	def __init__(self,data): # This is called as a constructor
		
		# Every node has two components data & pointer-next
		self.data = data
		self.next = None   # pointer that points to next node


class Linkedlist: 
	def __init__(self):
			self.head = None 
# First node of linked-list is said to be head , at start head is None.
	
	# Method to print the created linked-list
	def print_list(self):  
		cur_node = self.head
		 
		while cur_node:
			print(cur_node.data)
			cur_node = cur_node.next
	
	# 'append' method is used to insert a new node to the linked-list at end.
	def append(self,data):  
		new_node =Node(data)
	
		if self.head is None:   
			self.head = new_node
			return 

		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node   # Here, New node gets attatched to last node
	
	# 'prepend' method is used to insert new node at start of linked-list
	def prepend (self,data):
		new_node = Node(data) # new node which is to be inserted
		
		new_node.next = self.head  # 'next' pointer of new node is attatched to head-node of linked-list
		self.head = new_node # new_node is assigned to be head of linked-list
	
	# 'insert_after_node' method is used to insert a new node after a specified present node in data 
	def insert_after_node(self, prev_node, data):
		if not prev_node:
			print("Previous node is not in the list")
			return 
		
		new_node = Node(data)
		new_node.next = prev_node.next    
		# next pointer of prev_node is erased and instead of that next pointer of new node is showing to its succeding node
		prev_node.next = new_node
		# next pointer of previous node is directing to data of new_node

################### Concept of Deletion ###################
	
	# Delete the node with given data element:   
	def del_node(self,key):
		cur_node = self.head
		

		if cur_node and cur_node.data == key:
			self.head = cur_node.next             # head is pointed to next node
			cur_node = None
			return
		
		prev = None
		while cur_node and cur_node.data != key:
			prev = cur_node
			cur_node = cur_node.next

		prev.next = cur_node.next
		cur_node = None

		if cur_node is None:
			return
		
		
	# Delete the node at given position:
	def del_node_at_pos(self,pos):
		cur_node = self.head
		
		if pos == 0:
			self.head = cur_node.next  # head is moved to next node
			cur_node = None   # cur_node made None 
			return
		
		prev = None
		count = 0
		while cur_node and count != pos:
			prev = cur_node
			cur_node = cur_node.next
			count +=1
		
		if cur_node is None:
			return 

		prev.next = cur_node.next # prev node's next is directly pointing to succeding node of cur_node
		cur_node = None 
	

	
################### Length of Linked-list  ###################
	def len_iterative(self):

		count = 0
		cur_node = self.head
		while cur_node:
			count += 1
			cur_node = cur_node.next
		return count
	def len_recursive(self,node):
		if node is None:
			return 0
		return 1 +self.len_recursive(node.next)

################### Swapping of nodes ###################
	def swap_nodes(self,key_1, key_2):
		if key_1 == key_2:
			return
		
		prev_1 = None
		curr_1 = self.head

		while curr_1 and curr_1.data != key_1:
			prev_1 = curr_1
			curr_1 = curr_1.next
		
		prev_2 = None
		curr_2 = self.head
		while curr_2 and curr_2.data != key_2 :
			prev_2 = curr_2
			curr_2 = curr_2.next

		if not curr_1 or not curr_2:
			return

		if prev_1:
			prev_1.next = curr_2
		else:
			self.head = curr_2
		
		if prev_2:
			prev_2.next = curr_1
		else:
			self.head = curr_1

		curr_1.next , curr_2.next = curr_2.next , curr_1.next


################### Reverse the list ###################	
	def print_helper(self, node, name):
		if node is None:
			print(name + ": None")
		else:
			print(name + ":" + nodee.data)		

		# A -> B -> C -> D -> 0
		# D -> C -> B -> A -> 0
		# A <- B <- C <- D <- 0

	def reverse_iterative(self) :
		
		prev = None
		cur = self.head 
		while cur:
			nxt = cur.next 
			cur.next = prev 
				
				
				#self.print_helper(prev, "PREV")
				#self.print_helper(cur, "CUR")
				#self.print_helper(nxt, "NXT")


			prev = cur
			cur = nxt
		self.head = prev 




llist = Linkedlist() # linkedlist object e ha ...
llist.append("A")
llist.append("B")
llist.append("C") 
llist.append("D")

#print(llist.len_recursive(llist.head))
#print(llist.len_iterative())
#llist.prepend("E")
#llist.insert_after_node(llist.head.next,"E")
#llist.del_node("B")
# llist.del_node("C")

#llist.del_node_at_pos(2)
#llist.del_node("A")
#llist.swap_nodes("A","B")
llist.reverse_iterative()
llist.print_list()



