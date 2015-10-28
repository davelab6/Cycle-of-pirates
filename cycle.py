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
