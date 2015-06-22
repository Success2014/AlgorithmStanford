"""
Implement Min Heap
"""
__author__ = 'Neo'

class MinHeap():
    def __init__(self):
        self.myheap = []
    def __str__(self):
        return str(self.myheap)
    def __getitem__(self, key):
        return self.myheap[key]
    def __len__(self):
        return len(self.myheap)

    def insert(self, value):
        self.myheap.append(value)
        index_of_new_key = len(self.myheap) # virtual index, real index should subtract 1
        index_of_new_key_parent = index_of_new_key / 2 # virtual index, real index should subtract 1

        while index_of_new_key > 1 and self.myheap[index_of_new_key - 1] < self.myheap[index_of_new_key_parent - 1]:
            self.myheap[index_of_new_key - 1], self.myheap[index_of_new_key_parent - 1] = self.myheap[index_of_new_key_parent - 1], self.myheap[index_of_new_key -1]
            index_of_new_key = index_of_new_key_parent
            index_of_new_key_parent = index_of_new_key / 2

    def extractmin(self):
        if len(self.myheap) == 0:
            raise ValueError

        minvalue = self.myheap[0]
        if len(self.myheap) <= 2:
            self.myheap.remove(minvalue)
            return minvalue
        if len(self.myheap) == 3:
            self.myheap.remove(minvalue)
            if self.myheap[0] > self.myheap[1]:
                self.myheap[0], self.myheap[1] = self.myheap[1], self.myheap[0]
            return minvalue

        # move the last leaf to the root and swap down with smaller child
        self.myheap[0] = self.myheap[-1]
        self.myheap = self.myheap[:-1]

        index_of_key = 1
        flag = False
        while(not flag):
            index_of_key_left_child = 2 * index_of_key
            index_of_key_right_child = 2 * index_of_key + 1
            if (len(self.myheap) < 2 * index_of_key): # 0 child
                flag = True
            elif (len(self.myheap) == 2 * index_of_key): # only left child
                if self.myheap[index_of_key - 1] > self.myheap[index_of_key_left_child - 1]:
                    self.myheap[index_of_key - 1],self.myheap[index_of_key_left_child - 1] = self.myheap[index_of_key_left_child - 1],self.myheap[index_of_key - 1]
                    index_of_key = index_of_key_left_child
                else:
                    flag = True
            else: # two children
                if self.myheap[index_of_key_left_child - 1] < self.myheap[index_of_key_right_child - 1]:
                    smaller_child = self.myheap[index_of_key_left_child - 1]
                    if self.myheap[index_of_key - 1] > smaller_child:
                        self.myheap[index_of_key - 1], self.myheap[index_of_key_left_child - 1] = self.myheap[index_of_key_left_child - 1],self.myheap[index_of_key - 1]
                        index_of_key = index_of_key_left_child
                    else:
                        flag = True
                else:
                    smaller_child = self.myheap[index_of_key_right_child - 1]
                    if self.myheap[index_of_key - 1] > smaller_child:
                        self.myheap[index_of_key - 1], self.myheap[index_of_key_right_child - 1] = self.myheap[index_of_key_right_child - 1],self.myheap[index_of_key - 1]
                        index_of_key = index_of_key_right_child
                    else:
                        flag = True
        return minvalue

    def minheapify(self, pos):
        pass
    def buildminheap(self, alist):
        pass




class MaxHeap():
    def __init__(self):
        self.myheap = []
    def __str__(self):
        return str(self.myheap)
    def __getitem__(self, key):
        return self.myheap[key]
    def __len__(self):
        return len(self.myheap)


    def insert(self, value):
        self.myheap.append(value)
        index_of_new_key = len(self.myheap) # virtual index, real index should subtract 1
        index_of_new_key_parent = index_of_new_key / 2 # virtual index, real index should subtract 1

        while index_of_new_key > 1 and self.myheap[index_of_new_key - 1] > self.myheap[index_of_new_key_parent - 1]:
            self.myheap[index_of_new_key - 1], self.myheap[index_of_new_key_parent - 1] = self.myheap[index_of_new_key_parent - 1], self.myheap[index_of_new_key -1]
            index_of_new_key = index_of_new_key_parent
            index_of_new_key_parent = index_of_new_key / 2

    def extractmax(self):
        if len(self.myheap) == 0:
            raise ValueError

        maxvalue = self.myheap[0]
        if len(self.myheap) <= 2:
            self.myheap.remove(maxvalue)
            return maxvalue
        if len(self.myheap) == 3:
            self.myheap.remove(maxvalue)
            if self.myheap[0] < self.myheap[1]:
                self.myheap[0], self.myheap[1] = self.myheap[1], self.myheap[0]
            return maxvalue

        # move the last leaf to the root and swap down with smaller child
        self.myheap[0] = self.myheap[-1]
        self.myheap = self.myheap[:-1]

        index_of_key = 1
        flag = False
        while(not flag):
            index_of_key_left_child = 2 * index_of_key
            index_of_key_right_child = 2 * index_of_key + 1
            if (len(self.myheap) < 2 * index_of_key): # 0 child
                flag = True
            elif (len(self.myheap) == 2 * index_of_key): # only left child
                if self.myheap[index_of_key - 1] < self.myheap[index_of_key_left_child - 1]:
                    self.myheap[index_of_key - 1],self.myheap[index_of_key_left_child - 1] = self.myheap[index_of_key_left_child - 1],self.myheap[index_of_key - 1]
                    index_of_key = index_of_key_left_child
                else:
                    flag = True
            else: # two children
                if self.myheap[index_of_key_left_child - 1] > self.myheap[index_of_key_right_child - 1]:
                    larger_child = self.myheap[index_of_key_left_child - 1]
                    if self.myheap[index_of_key - 1] < larger_child:
                        self.myheap[index_of_key - 1], self.myheap[index_of_key_left_child - 1] = self.myheap[index_of_key_left_child - 1],self.myheap[index_of_key - 1]
                        index_of_key = index_of_key_left_child
                    else:
                        flag = True
                else:
                    larger_child = self.myheap[index_of_key_right_child - 1]
                    if self.myheap[index_of_key - 1] < larger_child:
                        self.myheap[index_of_key - 1], self.myheap[index_of_key_right_child - 1] = self.myheap[index_of_key_right_child - 1],self.myheap[index_of_key - 1]
                        index_of_key = index_of_key_right_child
                    else:
                        flag = True
        return maxvalue

    def maxheapify(self, pos):
        pass
    def buildmaxheap(self, alist):
        pass


def createlist(filename):
    num = []
    fhand = open(filename)
    for line in fhand:
        num.append(int(line))
    return num

def solution(num, length):
    min_heap = MinHeap() # store the larger numbers
    max_heap = MaxHeap() # store the smaller numbers
    median_dic = {}
    for i in xrange(length):
        if len(max_heap) == 0:
            max_heap.insert(num[i])
        elif num[i] <= max_heap[0]: # if the new number is smaller than the maximum of the left max_heap
            max_heap.insert(num[i])
            if len(max_heap) - len(min_heap) > 1:
                max_num_to_transfer = max_heap.extractmax()
                min_heap.insert(max_num_to_transfer)
        else:
            min_heap.insert(num[i])
            if len(min_heap) - len(max_heap) > 0:
                min_num_to_transfer = min_heap.extractmin()
                max_heap.insert(min_num_to_transfer)

        # record median
        median_dic[i+1] = max_heap[0]
    return sum(median_dic.values()) #% length




# heap1 = MinHeap()
# heap1.insert(15)
# heap1.insert(2)
# heap1.insert(10)
# heap1.insert(7)
# heap1.insert(6)
# heap1.insert(9)
# print heap1
# heap1.extractmin()
# print heap1
# heap1.extractmin()
# print heap1
# heap1.extractmin()
# print heap1
# heap1.extractmin()
# print heap1
# heap1.extractmin()
# print heap1
# heap1.extractmin()
# print heap1


# heap2 = MaxHeap()
# heap2.insert(15)
# heap2.insert(2)
# heap2.insert(10)
# print MaxHeap[0]

# heap2.insert(7)
# heap2.insert(6)
# heap2.insert(9)
# print heap2
# heap2.extractmax()
# print heap2
# heap2.extractmax()
# print heap2
# heap2.extractmax()
# print heap2
# heap2.extractmax()
# print heap2
# heap2.extractmax()
# print heap2
# heap2.extractmax()
# print heap2


num = createlist('Median.txt')
result = solution(num, 10000)
print result
print result % 10000