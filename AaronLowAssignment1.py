# __author__ = 'u0892608'
# Lab #1 Due monday 1/19/2015

# Be sure to write unit tests and use assert for each
# exercise. In some cases, I have provide some tests
# for you. Add to them. Be sure to write your solution
# for each problem directly below the question.
from random import randint
from functools import reduce
import random
import math

# EXERCISE 1: Write code that checks if two integers are
# equal without using comparison operators.
print("EX1 Started")
def equalWithoutEquals(val1, val2):
    TempVal = val1 - val2

    try:
        1 / TempVal
        return False
    except ZeroDivisionError:
        return True

assert equalWithoutEquals(5,5)
assert equalWithoutEquals(3241,5) == False

# EXERCISE 2: Write a toBinary() function that takes a single
# 32-bit integer and returns its binary format as a string.
# For example, if I called toBinary(897267474), the program
# would return "00110101011110110011011100010010"

print("EX2 Started")
def toBinary(Val1):


    OutPutString = ""
    RemainderVal = Val1
    BitLimit = 31
    while -1 != BitLimit:
        #print (BitLimit)
        if ((RemainderVal//2**BitLimit)==1):
            OutPutString += str(1)
        else:
            OutPutString += str(0)
        BitLimit -= 1 #Each iteration
    return str(OutPutString)

assert toBinary(4)

# EXERCISE 3: Write an indexOf(list, value) and contains(list, value).
# indexOf() returns the zero-based index of value. contains() returns
# true if the item is in the list.
print("EX3 Started")
EX3List = [2,3,4,5,6,7]


def indexOf(list, value):
    for i in range(0,len(list)):
        if(list[i]==value) is True:
            return i
    return False

def contains(list, value):
    for i in list:
        if(list[i]==value):

            return True
    return False
assert indexOf(EX3List, 4)
assert contains(EX3List, 4)





# EXERCISE 4: Write an any(list, condition), all(list, condition),
# and count(list, condition) function. any() returns true if
# any item in the list satisfies the condition. all() returns
# true if all of the items in the list satisfy the condition.
# count() returns the number of items that satisfy the condition.
# Be sure to write several test cases for each of these, and also
# use lambda functions when calling these procedures.

dummyList = [1,1,1,1,1,1,1,1]
EX4List = [4,5,6,2,3,4]

print("EX4 Started")

#Functions
def any(list, condition):
    val = 0
    for i in list:
        if(condition(i)):
            val += 1
    if(val > 0):
        return True
    return False



def all(list, condition):
    ValBool = True
    if any(list, condition) is False:
            return False
    else:
        return True

def count(list, condition):
    val = 0
    for i in list:
        if(condition(i)):
            val += 1
    if(val > 0):
        return int(val)
    return False



assert any(EX4List, lambda i: i < 4)
assert any(EX4List, lambda i: i > 100) == False
assert all(dummyList, lambda i: i == 1)
assert all(dummyList, lambda i: i == 3) == False
assert count(dummyList, lambda i: i == 1)



# EXERCISE 5: Write a genOrdered(numElements) function
# that generates a sequence of random but ordered
# elements of numElements.

print("EX5 Started")
def genOrdered(numElements):
    i = numElements
    InputList = []
    for j in range(0, i):
        InputList.append(randint(0,100))
    j = len(InputList)
    instances = 0
    for i in range(len(InputList)-1,0,-1):
       for j in range(i):
           if(InputList[j]>InputList[j+1]):
               val = InputList[j]
               InputList[j] = InputList[j+1]
               InputList[j+1] = val
               instances += 1
    print("The list shifted " + str(instances))
    print(InputList)
    return InputList

assert genOrdered(10)





# EXERCISE 6: Write a binarySearch(). Use your generator
# from the previous exercise to create a sorted sequence
# to search. Be sure to test that your algorithm reports
# appropriate success and fail conditions. Be sure to test
# searching for every number in the list.

#Its unclear what information im parsing. So im going to go with my expected parameters.
print("EX6 Started")
newlist = genOrdered(100)
Testlist = [1,1,2,2,3,4,4,5,5]

def binarySearch(list,val):
    Lowmark = 0
    Halfmark = 0 #To be determined
    Highmark = len(list)
    while True:
        if Highmark < Lowmark:
            return -1
        Halfmark = (Lowmark + Highmark)//2
        if list[Halfmark] > val:
            Lowmark = Halfmark + 1
        elif list[Halfmark] > val:
            Highmark = Halfmark - 1
        else:
            return Halfmark
    print(Halfmark)

assert binarySearch(Testlist, 3)
assert binarySearch(newlist, 55)





# EXERCISE 7: Write a where(list, predicate) (returns a sequence
# of items that satisfies the predicate). Write a select(list, transform)
# that converts each item in the sequence using transform.
meValues = [3,9,2,7,1,4,3]
OutValues = []
print("EX7 Started")

#Functions:
def where(list, predicate):
    for i in list:
        if(predicate(i)):
            yield i

def select(list, transform):
    for i in list:     #if(transform(i)):
            yield transform(i)

#clean up list
def CleanList(list):
    while len(list) > 0:
        list.pop(0)


#Searches

for each in where(meValues, lambda i : i < 5):
    OutValues.append(each)
    #print(each)
print(OutValues)
CleanList(OutValues)


for each in select(meValues, lambda i : i + 5):
    if(len(OutValues)== 0):
        OutValues.append(each)

print(OutValues)
CleanList(OutValues)



# EXERCISE 8: Write code to demonstrate the use of filter(), map(), and reduce().
# Explain how these functions are similar to functions we have already written.
print("EX8 Started")
EX8List = [2,2,4,5,6,7,7,7,8,9,9,10]
#Filter uses a predicate such as lambda to go through the list and returns only the values that match the predicate but does not alter the original unless stated
printme = filter(lambda x: x == 2, EX8List)
print(printme)

#Map() applies the a condition to all in the list, the length of the lists are always the same since its not removing any new instances, only changing them
printmap = map(lambda x : x+1, EX8List)
print(printmap)

#reduce works with a condition throughout the entire list. Using almost a recursive style process you can multiply or divide or find strings related. Just a forloop that uses the condition and puts it into one non list output
printReduce = reduce((lambda x, y: x*y), EX8List)
print(printReduce)

# EXERCISE 9: Attached with the assignment is a Particles.py file. Download
# Panda 3D (https://www.panda3d.org/) and get Particles.py working on your machine.

