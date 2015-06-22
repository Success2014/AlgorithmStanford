__author__ = 'Neo'



def countInv(array,n):
    """
    :param array: input array
    :param n: length of the array
    :return: sorted array and number of inversions
    """
    if n <= 1:
        return array, 0
    first_half = array[0:(n / 2)]
    second_half = array[(n / 2):]
    first_half_len = len(first_half)
    second_half_len = len(second_half)
    first_half, numInv_1 = countInv(first_half, first_half_len)
    second_half, numInv_2 = countInv(second_half, second_half_len)
    newArray, numInvSplit = countSplit(first_half, second_half, first_half_len, second_half_len)
    return newArray, (numInv_1 + numInv_2 + numInvSplit)

def countSplit(firstArray, secondArray, faLen, saLen):
    """
    :param firstArray:
    :param secondArray:
    :param faLen: length of the first array
    :param saLen: length of the second array
    :return: combined and sorted array: array; number of inversions: invCount
    """
    i = 0
    j = 0
    invCount = 0
    array = []
    firstArray.append(999999999999)
    secondArray.append(999999999999)
    for k in range(faLen + saLen):
        if firstArray[i] <= secondArray[j]:
            array.append(firstArray[i])
            i += 1
        else:
            array.append(secondArray[j])
            j += 1
            invCount += faLen - i
    return array, invCount



# testarray = [4, 3, 2, 1]


#fhand = open('IntegerArray.txt')
fhand = open('test1.txt')
testarray = []
count = 0
for line in fhand:
    line = int(line)
    testarray.append(line)
    count += 1
#print testarray
print type(testarray)
x,y = countInv(testarray, count)
print y