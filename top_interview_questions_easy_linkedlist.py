"""
1. Delete Node in a Linked List

Write a function to delete a node in a singly-linked list. 
You will not be given access to the head of the list, 
instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, 
the linked list should become 4 -> 1 -> 9 after calling your function.
"""

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def deleteNode(node):
	node.val = node.next.val
	node.next = node.next.next


"""
2. Remove Nth Node From End of List

Given the head of a linked list, 
remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""
# Definition for singly-linked list.

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
