# Problem Statement : Use a stack data structure to covert integer into its euivalent 

# binary no.
# We know that we can convert integer number into its binary equivalent using simple 'Division by 2 Method'.

# Example : 242 to binary code
# 242 / 2  = 121 --> 0 
# 121/2 = 60  --> 1         
# 60/2 = 30 --> 0
# 30/2 = 15 --> 0
# 15/2 = 7 --> 1
# 7/2 = 3 --> 1
# 3/2 = 2 --> 1
# 1/2 = 0 --> 1
# 11110010

# Hence, binary equivalent of 242' integer is 11110010

from Stack import stack
# from Stack module , stack class is imported to current programming file 

def div_by_2(dec_num):
	s = stack()        # 's' instance is created for class 'stack()'

	while dec_num>0:
		r = dec_num % 2
		s.push(r)
		dec_num = dec_num//2    
	bin_num = ""
	while not s.is_empty():
		bin_num += str(s.pop())
	return bin_num

print(div_by_2(242))
