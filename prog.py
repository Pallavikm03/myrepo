def example():
	"""Example for filter and lambda expression"""
	exp = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
	print exp
	
if __name__=="__main__":
	example()
print 'Hello world !'