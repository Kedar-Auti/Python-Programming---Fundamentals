# Problem Statement : Reverse the given string (i.e. word) by using stack Data Structure

# Example : If 'Hello' is the given word , its reverse string form will be 'olleH'

from Stack import stack 


def reverse_string(stack, input_str):

	 # Loop through strings and push all characters in 'items' list created in Stack class
	 # Then add character by character into the another string until items list get empty

	for i in range(len(input_str)):
	 	 stack.push(input_str[i])
	
	rev_str = []

	while not stack.is_empty():
	 	rev_str += stack.pop()

	return rev_str

stack = stack()
input_str = "Kedar"

print(reverse_string(stack, input_str))


# NOTE : we can do it directly by using string indexing or slicing , But in given problem statement we must use stack data struture type. 
#input_str = "Hello"
#print(input_str[::-1])