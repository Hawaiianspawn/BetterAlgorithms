__author__ = 'Hawaiian_spwn'
#u0892608

# 1- Write a merge sort. Again, don't look at code online,
# but instead, train you mind so see steps and processes
# and translate them into code. Here is an excellent video
# to show you the process of a merge sort.
# https://www.youtube.com/watch?v=EeQ8pwjQxTM


EXList1 = [79, 94, 10, 38, 80, 94, 13, 73, 84, 86]
EXList2 = [40, 8, 66, 100, 67, 18, 22, 40, 12, 94]
EXList3 = [67, 85, 77, 28, 20, 30, 97, 40, 49, 5]


#I went with the second sorting algorithm that breaks up all the elements then merges them together
#https://www.youtube.com/watch?v=TzeBrDU-JaY
#I can't integrate my merge function


#Merge merges and sorts Left List and Right List
def Merge(L,R):
    LL = L
    RL = R
    for i in LL:
        RO = False
        for j in RL:
            if j<i and RO==False:
                RO = True
                temp = j
                RL.remove(temp)
                LL.insert((LL.index(i)), temp)
            elif len(RL)==1:
                temp = j
                LL.append(temp)
                del RL[:]
    #             temp = RL[j]
    #     LL.insert[i,temp]
    print( "Right list is" + str(RL))
    print("Left list is " + str(LL))
    return LL

print(Merge([1,2,4],[3,5,1]))
FiniteList = [[[79], [94], [10], [38], [80], [94], [13], [73], [84], [86]]]


#splitList breaks any list into n sized sub lists(this is for breaking them down into the single variables).
def splitList(data, n):
    n = max(1, n)
    return [data[i:i + n] for i in range(0, len(data), n)]
print(splitList([1,2,3,4,5,6,7],2))




def mergeSort(data):
    #Fought the good fight, EXTREMELY Close to solving the solution this way... I'll just give up on this method and move on to the TA assisted method...
    #I thought I could optimize it instead of making many many many lists(which would just bog down the serach with non vital lists
    #########################################################################################################################################
    # ML = splitList(data, 1)
    # LL = [] #Loop List
    # print("THIS IS "+ str(ML))
    # while len(ML)>1:
    #     for i in range(0,len(ML[0]), 2):
    #         LL = Merge(ML[i][0],ML[i+1][0])
    #         var1 = ML[i]
    #         var2 = ML[i+1]
    #         ML.remove(ML[var1], ML[va2])
    #         print(ML[i])
    #         print(LL)
    #         j += 1
    #
    # print(ML)
    # return True
###########################################################################
    #Discussed with TA, given this map to finish up the job.
    #https://imgur.com/O4Cwe2x
      if len(data)>1:
        mid = len(data)//2
        low = data[:mid]
        high = data[mid:]

        mergeSort(low)
        mergeSort(high)

        i=0
        j=0
        k=0
        while i<len(low) and j<len(high):
            if low[i]<high[j]:
                data[k]=low[i]
                i=i+1
            else:
                data[k]=high[j]
                j=j+1
            k=k+1

        while i<len(low):
            data[k]=low[i]
            i=i+1
            k=k+1

        while j<len(high):
            data[k]=high[j]
            j=j+1
            k=k+1
        print(data)
        return True

assert mergeSort(EXList1)




# 2- Write a quick sort. Same rules as #1. Video:
# https://www.youtube.com/watch?v=aQiWF4E8flQ

def quickSort(data):
    R = data
    L = []
    M = []
    if len(data) <=1:
        return data
    else:
        pivot = R[0]
        for i in R:
            if i < pivot:
                L.append(i)
            if i > pivot:
                M.append(i)
        L = quickSort(L)
        M = quickSort(M)
        return (L+[pivot]*R.count(pivot)+M)

assert quickSort(EXList2) != False



#assert quickSort(SortList)

# 3- Fill in/finish the LinkedList below:

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


#Run a mid reference
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  # Inserts value into a new node
  # after the given node
  def insertAfter(self, node, value):
    newNode = Node(value)
    newNode.next = node.next
    node.next = newNode
    runner = self.head
    while runner is not None:
        if(runner.data == value):
            tempNode = runner
            newNode.next = runner.next
            runner.next = newNode
    runner = runner.next
    if(newNode.next is None):
      self.tail = newNode

  # Inserts value into a new node
  # before the given node
  def insertBefore(self, node, value):
      newNode = node(value)
      runner = self.head
      #used next to insert at the spot.
      while runner.next is not None:
          if(runner.next.data == value):
              newNode.next = runner.next
              runner.data = newNode
              return True
          elif(runner.next.next is None):
              return False
          else:
              runner = runner.next

  # Adds the given value as the first
  # value in the list
  def addFirst(self, value):
      newNode = Node.data(value)
      newNode.next = self.Head
      self.Head = newNode

  # Adds the given value as the last
  # value in the list
  def addLast(self, value):
    node = Node(value)
    if(self.head is None):
      self.head = node
    if(self.tail is not None):
      self.tail.next = node
    self.tail = node
    return node
  # Returns the node that contains
  # the given value

  def find(self, value):
      runner = self.head
      Outcome = None
      while runner.data is not None:
          if(runner.data == value):
              return runner
          else:
                runner = runner.next
      return False



  # Removes the given node
  # from the list
  def remove(self, node):
      tempNode = None
      runner = self.head
      while runner != None:
          if(runner == node):
              runner.node
      # while runner != None:
      #     tempnode = runner
      #     runner = runner.next
      #     if(tempNode == None):
      #         self.head = node.next
      #       else:
      #           tempNode.next = runner.next

  # Returns the first node
  def first(self):
      NewNode = node.data(self.data)
      return NewNode

  # Returns the last node
  def last(self):
      runner = self.head
      if runner.next is None:
          return runner
      elif runner != None:
          runner = runner.next


  # Returns the number of items in the list
  def count(self):
      runner = self.head
      count = 1
      while runner != None:
          runner = runner.next
          count += 1
      return count




  # Allows the user to iterate over
  # the values (not the nodes)
  #walk through the values like a for loop
  def __iter__(self):
    pass

# 4- Write test cases for all functionality
# in your list. Be sure to test for boundary
# conditions such as but not limited to:
#   1- Inserting at the end/beginning
#   2- Removing at the end/begging
#   3- Inserting into an empty list
#   4- Removing from the end/beginning when
#      list only has one node.
#   5- Adding at the begin/end into an empty list.
#   6- What else can you come up with???
# Comment each test thoroughly as to what you
# are testing for to make it easier on the TAs.


def printSort(data):
    Length = 0
    while data.next is not None:
        Length += 1
    return Length

def LengthData(data):
    Length = 0
    while data.next is not None:
        Length += 1
    return Length


LL = LinkedList()
LL.addFirst(5)
LL.addFirst(6)
LL.addFirst(7)

print(printSort(LL))
