__author__ = 'u0892608'

from random import randint
import math
#Three randomly generated lists from the previous assignment function\
#BECAUSE APPARENLTY RUNNING THE FUNCTION DESTORYS THE LIST COMPLETELY

#https://i.imgur.com/YgXNL6g.jpg
#Literally me


EXList1 = [79, 94, 10, 38, 80, 94, 13, 73, 84, 86]
EXList2 = [40, 8, 66, 100, 67, 18, 22, 40, 12, 94]
EXList3 = [67, 85, 77, 28, 20, 30, 97, 40, 49, 5]
EXList4 = [79, 94, 10, 38, 80, 94, 13, 73, 84, 86]
EXList5 = [40, 8, 66, 100, 67, 18, 22, 40, 12, 94]
EXList6 = [67, 85, 77, 28, 20, 30, 97, 40, 49, 5]
EXList7 = [79, 94, 10, 38, 80, 94, 13, 73, 84, 86]
EXList8 = [40, 8, 66, 100, 67, 18, 22, 40, 12, 94]
EXList9 = [67, 85, 77, 28, 20, 30, 97, 40, 49, 5]


#1 - Selectionsort:
#Find the smallest of the current list, then append it to the OutputList
def Selectionsort(list):
    IL = list
    OL = []
    while IL:
        min = IL[0]
        for i in IL:
            if(i<min):
                min = i
        OL.append(min)
        IL.remove(min)
    print(OL)
    return OL



assert Selectionsort(EXList1)
assert Selectionsort(EXList2)
assert Selectionsort(EXList3)

#I sort I figured out after doing the first assignment
def bubblesort(list):
    IL = list
    j = len(IL)
    instances = 0
    for i in range(len(IL)-1,0,-1):
       for j in range(i):
           if(IL[j]>IL[j+1]):
               val = IL[j]
               IL[j] = IL[j+1]
               IL[j+1] = val
               instances += 1
    #print("The list shifted " + str(instances))
    print(IL)
    return IL

assert bubblesort(EXList4)
assert bubblesort(EXList5)
assert bubblesort(EXList6)

def Isort(list):
    IL = list
    #integrate a new element every iteration
    for i in range(0,len(IL)):
        var = IL[i]
        j = i #This is so we dont have to recount through the whole list again only at the interation I is
        #Search through the sorted set and arrange if necessary,

        #Could not find a way to integrate a for loop instead of a while loop
        while j>0 and (IL[j-1]>var):
            IL[j]=IL[j-1]
            j -= 1
        IL[j] = var
    print IL
    return IL





assert Isort(EXList7)
assert Isort(EXList8)
assert Isort(EXList9)