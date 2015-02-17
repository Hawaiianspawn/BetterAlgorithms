#Created = Aaron Low
#  Homework
#Old tricks I learned from Algorithems CS
import Timeit
#


# 1- Write a binary search tree with the following functions:
#   add(value) - Adds the value to the tree.
#   contains(value) - Determines if the value is in the tree.
#   display() - Displays the contents of the tree in order.
#
#   Be sure to use recursion in all of these functions.

# 2- What is the complexity of bubble sort? Why?
#
#The bubble sort checks its neighbor from the list and switches places with the subject, does that over and over again until every element cannot be changed without changing the comparison. Like a bubble through the ocean, it pushes everything aside and strives for the top(except it doesnt if its low....)
#
#Python lists are just arrays that get restructured.
#lg(x) = log_2(x)
#
#
# 3- What is the complexity of selection sort? Why?
#Selection sort is based on finding the lowest variable in the list, and appending it to the sorted list until every element hase been added. Potentially taking n^2 [Drop the mike]
#
#
# 4- What is the complexity of a linear search? Why?
#The linear search goes through every element in order, the O(n) is the possible amount of operations. This is a simple format that is the basis of majority of our search methods. The Operation, we are checking eqality of a given key.[Drop the mike]
#
# 5- What is the complexity of a binary search? Why?
#Binary search uses operations to bisect a sorted list cutting the big O Notation to (log_2(n)), this is due to cutting the useless data out of the list. The division of the data list gives you a smaller and smaller sample size. Has a potential to be a constant given a big enough data structure. [Drop the mike]
#
# 6- What is the complexity of a merge sort? Why?
#Merge sort breaks down all the elements in a list into their base components. Then merges each one while sorting using a Linear search method every merge. This allows for the maximum of NLogN iterations as the worse case. [Drop the mike]
#
# 7- What is the complexity of a quick sort? Why?
#Quick sort is sort of an enigma, it feels like a selection sort, choosing a random pivot and sorts the elements in the list , picking an element and changing. The best case in sorting is to use a random index instead of the left most or right most.
#
# 8- What is the complexity of a list?
#A list based on what we know in python is basically a dynamic array... but we wont talk about that. Lists are dynamic arrays with index values that allow us to keep track or pull a specific element from a list.
#     -Access an item?
#As simple as selecting the index you like, only takes 1 operation to get to it.
#     -Insertion?
#insertion is easy again because of the indexing, allowing of just throwing it in, and it pushes all elements after back one on the index.
#     -Deletion?
#Deletion is pretty much the same, except it moves every element after the operation forward to fill in the gap.
#     -Append to the end?
#Appending basically adds a new element to the list from the very last item in the list len(list). Computationally simple.

#
# 9- What is the complexity of a linked list?
#Linked list is based on references to other nodes through what can be best described is "links of a chain", Sadly the index plays a problem in getting the information indexed as fast as possible.
#  If you want the list to be faster to search you have to categorize special portions of the list, examples we used is Head and Tail of a linked list, a mid point would be a viable one to use but would be computationally heavy on a big list in changing.
#     -Access an item?
#Accessing an item requires going though a certain starting point and looking through each next search until  you come up with the element you want. They do not index anything for the list can be referenced anywhere.
#     -Insertion?
#Insertion in a specific point requires a search which is again... slow
#     -Deletion?
#Deletion requires separating, affected node from both its parent and its child, then relinking those two components together.
#     -Append to the end?
#Based on  if you used the .tail parameter in your link list node, you will either just add to the tail's next and make it next or search through everyone until you find a none element(Which is usually tail if you did it right).
# 10- Write an expression parser that will evaluate the
#   following expression respecting operator precedence:

  #  5 + 2 * 3 - 8 / 4 + 8

  Store the expression as follows:
    expression = ["5", "+", "2", "*", "3", "-", "8", "/", "4", "+", "8"]

def solve(list):
    Everything = 0

    CashList = list

#Append == Push
#Pop =
#Always, push operand.
#Separate operations and operands into separate lists.

#Operations can be considered an operand

#Node, and recursion
#lowest priority at the very last of the list will be the root of the tree


    # for i in range(0, len(list):
    #     if(list[i] is "*"):
    #         Everything = list[i-1]*list[i+1]
    #         list.remove(i-1)
    #     list.remove
    #     list.remove(i+1)
    #     if(list[i])


string = "4+3"
print(int(string))

