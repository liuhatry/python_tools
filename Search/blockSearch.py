#!/usr/bin/env python

listIndex = [9,19,25,100,200,321]
mylist = [[],[],[],[],[],[],[]]

def findIndex(index,data):
    min = 0
    max = len(index) -1

    while(min <= max):
        mid = (max + min) // 2
        if data > index[mid]:
            min = mid + 1
        else: 
            max = mid -1
    return max + 1

def searchBlock(mylist,data):
    for i in range(0,len(mylist)):
        if data == mylist[i]:
            return i
    return -1

def insert(index,value):
    item = findIndex(index,value) 
    if searchBlock(mylist[item],value) >= 0:
        print value, 'is already exist in list',item
        return False
    else:
        mylist[item].append(value) 
    return True

def search(index,value):
    item = findIndex(index,value)
    location = searchBlock(mylist[item],value) 
    if location >= 0:
        print value,'is in block',item,'location:',location
    else:
        print 'can not find',value

if __name__=='__main__':
    data = [0,2,3,201,1,3,4,14,14,23,34,56,78,90,100,198,340,324,67,890,0,-123,45,67,89,3,5,90,45,67]
    for i in range(0,len(data)):
        insert(listIndex,data[i])

    print mylist[0] 
    print mylist[1] 
    print mylist[2] 
    print mylist[3] 
    print mylist[4] 
    print mylist[5] 
    print mylist[6] 

    search(listIndex, 0)
    search(listIndex, 7)
    search(listIndex, 56)
    search(listIndex, 11)
    search(listIndex, 324)
