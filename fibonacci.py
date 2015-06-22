# fibonacci

def fibonacci(n1,n2):
	global index, num
	print n1+n2
	index += 1
	
	if index <= num:
		fibonacci(n2, n1+n2)

index = 0
num = 4

fibonacci(0,1)