#!/usr/bin/python3

def sequentialSearch(A, key):
    n = len(A)
    for i in range(0, n):
        if A[i] == key:
            return i
    return -1


a = [0,1,2,3,4,5,6,7,8,9,10]
print(sequentialSearch(a,5))
