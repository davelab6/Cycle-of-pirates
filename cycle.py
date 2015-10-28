"""
def answer(number, y=None):
	if y is None:
		y = [0]
	
	if len(y) <= len(number) + 1:
		if y[-1] in y[:-1]:
			cycle_length = (len(y) - 1) - y[:-1].index(y[-1])
			return cycle_length
		else:
			y.append(number[y[-1]])
			return answer(number, y)
	else:
		return "Error! You went to too many pirates."
		
"""

def answer(numbers):
	y = [0]
	
	for j in range(0, len(numbers) + 1):
		y.append(numbers[y[-1]])
	
	print "y: ",y
	print "y[-(len(y) - 2)]: ",y[-(len(y) - 2)]
	for k in range(-(len(y) - 2), 0):
		print "y[",k,"]: ",y[k]
		print "y[:",k,"]: ",y[:k]
		if y[k] in y[:k]:
			print "len(y[:k]): ",len(y[:k])
			print "y[:k].index(y[k]): ",y[:k].index(y[k])
			return len(y[:k]) - y[:k].index(y[k])

		
		
		
print "x = [1, 3, 0, 1]: ", answer([1,3,0,1])
print "x = [1, 0]: ", answer([1, 0])
print "x = [1, 2, 1]: ", answer([1, 2, 1])
print "x = [1,2,3,4,0]", answer([1,2,3,4,0])
print "x = [1,2,3,4, 5, 6, 7, 8, 9, 10, 11, 12,0]", answer([1,2,3,4, 5, 6, 7, 8, 9, 10, 11, 12,0])
