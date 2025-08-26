"""
https://leetcode.com/problems/reverse-linked-list/
We've done this one before, not sure if I remember the best way to do it. Lets give it
a try. The classic interview question.
We got it without much issue. Very nice. 
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head: return None
        reversed_list = ListNode(head.val)
        temp = head.next
        while temp:
            reversed_list = ListNode(val=temp.val, next=reversed_list)
            temp = temp.next
        return reversed_list
    

"""
Their solution is below.
They didn't need to check for an empty head, looks like its just cause of how I init-ed the res.
besides that its as we did, reassign to next, set old val to next and continue. 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev