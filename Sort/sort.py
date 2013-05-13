import random
from copy import copy

#插入排序

#1.直接插入排序 稳定
#原理：将数组分为无序区和有序区两个区，然后不断将无序区的第一个元素按大小顺序插入到有序区中去，
#      最终将所有无序区元素都移动到有序区完成排序。
#有序区在左
def directInsertSort(seq):
    size = len(seq)
    for i in range(1,size):
        tmp,j = seq[i],i
        while j>0 and tmp < seq[j-1]:
            seq[j],j = seq[j-1],j-1
        seq[j] = tmp
    return seq

#2.希尔排序 不同分组，会破坏稳定性，不稳定排序
#原理：他的主要思想借用了合并排序的思想。不过他不是左边一半右边一半，而是按照步长来分，随着步长减少，分成的组也越少。然后进行各组的插入排序。
#步长=分组数

def shellSort(seq):
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq):
            k = i
            while k >= inc and seq[k-inc] > el:
                seq[k] = seq[k-inc]
                k -= inc
            seq[k]= el
        inc = round(inc / 2.2)
    return seq

#选择排序

#1.直接选择排序 不稳定(交换造成不稳定)
#原理：将序列划分为无序和有序区，寻找无序区中的最小值和无序区的首元素(无序区的最左面)交换，
#      有序区扩大一个，循环最终完成全部排序。
#有序区在左
#和冒泡相反， 先找到最小的放的左面，只不过并不像冒泡那样以此往上冒，而是只交换一次
def directSelectSort(seq):
    size = len(seq)
    for i in range(0,size-1):
        k = i; j = i+1  #k:最小值的坐标 i:无序区首元素的坐标
        while j <size:
            if seq[j] < seq[k]:
                k = j
            j += 1
        seq[i],seq[k] = seq[k],seq[i]
    return seq

#2.堆排序 不稳定
#大顶堆 小顶堆
#此例为大顶堆
def maxHeapify(A, parent, heapsize):
    left = 2*parent + 1 #left child
    right = 2*parent + 2 #right child
    largest = parent 

    if left < heapsize and A[left] > A[largest]:
        largest = left
    if right < heapsize and A[right] > A[largest]:
        largest = right

    if largest != parent:
        A[parent], A[largest] = A[largest], A[parent]
        maxHeapify(A, largest, heapsize)

def buildHeap(A):
    heapsize = len(A)
    for i in range(heapsize//2 - 1 , -1, -1):
        maxHeapify(A, i, heapsize)

def heapSort(A):
    heapsize = len(A)
    buildHeap(A)

    for i in range(heapsize-1, 0, -1):
        #print(A)
        A[0], A[i] = A[i], A[0]
        heapsize -= 1
        maxHeapify(A, 0, heapsize)
    


#交换排序

#1.冒泡排序 稳定
#原理：将序列划分为无序和有序区，不断通过交换较大元素至无序区尾完成排序,
#      先将最大的移动到最右边，依次进行
#无序区在左面
def bubbleSort(seq):
    size = len(seq)
    for i in range(1,size):
        for j in range(0,size-i):
            if seq[j+1] < seq[j]:
                seq[j+1],seq[j] = seq[j],seq[j+1]
    return seq

#2.快排 不稳定(当相等的两个中的一个作为临界值时，会造成不稳定)
#quick sort
#原理：不断寻找一个序列的中点，然后对中点左右的序列递归的进行排序，
#      直至全部序列排序完成，使用了分治的思想。
# 先分治，再排序
# 冒泡的改进，
#分治一次后，左边的都比右边的小,并且中间的那个值实际上已经排好
def _divide(seq, low, high):
    tmp = seq[low] #将第一个值作为中间的临界值
    while low!=high:
        while low<high and seq[high]>=tmp:
            high -= 1
        if low < high:
            seq[low] = seq[high]
            low += 1
        while low<high and seq[low]<=tmp:
            low+=1
        if low<high:
            seq[high] = seq[low]
            high -= 1
    seq[low] = tmp
    return low

def _quickSort(seq, low, high):
    if low>= high:
        return
    mid = _divide(seq,low,high)
    _quickSort(seq,low ,mid-1)
    _quickSort(seq,mid+1,high)

def quickSort(seq):
    size = len(seq)
    _quickSort(seq,0,size-1)
    return seq

#归并排序 稳定排序
#原理：将两个（或两个以上）有序表合并成一个新的有序表，即把待排序序列分为若干个子序列，每个子序列是有序的。
#      然后再把有序子序列合并为整体有序序列。
#merge sort
#先排序 再归并

def merge(seq,left,mid,right):
    tmp = []
    i,j = left , mid
    while i<mid and j<= right:
        if seq[i] <= seq[j]:
            tmp.append(seq[i])
            i+=1
        else:
            tmp.append(seq[j])
            j+=1
    while i<mid:
        tmp.append(seq[i])
        i+=1
    while j<=right:
        tmp.append(seq[j])
        j+=1
    for i in range(left,right+1):
        seq[i] = tmp.pop(0)


def _mergeSort(seq,left,right):
    if left == right:
        return
    else:
        mid = int((left + right) / 2)
        _mergeSort(seq,left,mid)
        _mergeSort(seq,mid+1,right)
        merge(seq,left,mid+1,right)

def mergeSort(seq):
    size = len(seq)
    _mergeSort(seq,0,size-1)
    return seq


s = [2,3,23,1,34,67,34,456,12,90,345,78,0]
#print(bubbleSort(s))
#print(directSelectSort(s))
#print(quickSort(s))
#print(directInsertSort(s))
#print(mergeSort(s))
#print(shellSort(s))
heapSort(s)
print(s)
