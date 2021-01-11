#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
from collections import deque

#ListNode Class
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
    
    
    def addTwoNumbers(self, l1:ListNode, l2: ListNode) -> ListNode:
        #Flip value of l1
        l1Value = int("".join([str(i) for i in reversed(l1)]))
        
        #Flip value of l2
        l2Value = int("".join([str(i) for i in reversed(l2)]))

        tempsum = l1Value + l2Value

        return [int(x) for x in reversed(str(tempsum))]
        

        


l1 = [2,4,3]
l2 = [5,6,4]
objvar = Solution(l1, l2)
testAnswer = []
testAnswer = objvar.addTwoNumbers(l1, l2)
print(testAnswer)