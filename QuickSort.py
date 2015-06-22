__author__ = 'Neo'

def QuickSort(array, n):
    """
    :param array: list
    :param n: length of the array
    :return: sorted array and number of comparison
    """
    if n <= 1:
        return array, 0
    pivot = ChoosePivot2(array, n)
    pivot_idx = array.index(pivot)
    array = Partition(array, pivot_idx)
    pivot_idx = array.index(pivot)
    first_array = array[0: pivot_idx]
    second_array = array[pivot_idx + 1:]
    first_array_new, facNum = QuickSort(first_array, len(first_array))
    second_array_new, secNum = QuickSort(second_array, len(second_array))
    return first_array_new + [pivot] + second_array_new, (n - 1) + facNum + secNum

def Partition(array, index):
    """

    :param array:
    :param index: index of the pivot
    :return: partitioned array
    """
    if len(array) <= 1:
        return array
    i = 1
    array[0], array[index] = array[index], array[0]
    for j in range(1,len(array)):
        if array[j] < array[0]:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[0], array[i - 1] = array[i - 1], array[0]
    return array

def ChoosePivot1(array, n):
    """
    choose the first item as the pivot
    :param array:
    :param n: length of the array
    :return: pivot
    """
    return array[0]
def ChoosePivot2(array, n):
    """
    :param array:
    :param n: length of the array
    :return: pivot
    """
    return array[-1]
def ChoosePivot3(array, n):
    """
    use the median-of-three
    :param array:
    :param n: length of the array
    :return: pivot
    """
    if n % 2 == 0:
        median = array[n / 2 - 1]
    else:
        median = array[n / 2]

    comArray = [array[0], median, array[-1]]
    max = -100000000
    maxSec = -200000000

    for value in comArray:
        if value > max:
            maxSec = max
            max = value
        elif value > maxSec:
            maxSec = value
    return maxSec


fhand = open('QuickSort.txt')
testarray = []
count = 0
for line in fhand:
    line = int(line)
    testarray.append(line)
    count += 1
#print testarray
print type(testarray)
x,y = QuickSort(testarray, count)
print y


