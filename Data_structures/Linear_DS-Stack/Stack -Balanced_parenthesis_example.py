# Problem Statement : Check whether the given set of paranthesis is balanced or not.


# Balanced : {[]}
# Non-balanced : {{[]}

from Stack import stack
# from Stack module , stack class is imported to current programming file 

def is_match(p1,p2):
	if p1 == "{" and p2 == "}":
		return True
	elif p1 == "[" and p2 == "]":
		return True
	elif p1 == "(" and p2 == ")":
		return True
	else:
		return False

def is_paren_balanced (paren_string):
	s = stack()
	is_balanced = True ## initial variables la default nav dile 
	index = 0 # initial variables la default nav dile 

	while index < len(paren_string) and is_balanced:
		paren = paren_string[index]
		if paren in "{[(":
			s.push(paren)
		else:
			if s.is_empty():
				is_balanced = False
			else:
				top = s.pop()
				if not  is_match(top , paren):
					is_balanced = False
		index += 1

		if s.is_empty() and not is_balanced:
			return False
		else:
			return True

print(is_paren_balanced("({}{()][]}) "))
 