def Count(array):
	
	n = len(array)
	
	if (n == 0) or (n == 1):
		global c 
		c = 0;
		nArray = array
	else:
		m = n / 2
		F = array[0:m]
		S = array[m:]
		
		(tmpa, x) = Count(F)
		array[0:m] = tmpa
		
		(tmpb, y) = Count(S)
		array[m:] = tmpb
		
		(nArray, z) = CountSplitInv(array)
		c = x + y + z
	
	return (nArray, c)
	
def CountSplitInv(array):
	global cc 
	cc = 0
	n = len(array)
	m = n / 2
	
	F = [None] * (m + 1)
	S = [None] * (n - m + 1)
	F[0:m] = array[0:m]
	S[0:(n-m)] = array[m:]
	F[-1] = 99999999999999
	S[-1] = 99999999999999
	
	i = 0
	j = 0
	
	for k in range(0,n):
		if F[i] <= S[j]:
			nArray[k] = F[i]
			i += 1
		else:
			nArray[k] = S[j]
			j += 1
			cc = cc + (m - i)
	return (nArray, c)
array = [6,5,3,2]
nArray = [None] * len(array)
(result_a, result_b) = Count(array)
print result_b
