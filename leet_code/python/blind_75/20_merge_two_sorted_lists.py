"""
https://neetcode.io/problems/merge-two-sorted-linked-lists?list=blind75
Solution found in under 20 minutes, very disorganized but covers all cases. It looks like you kept 
seeing new cases and just slapped on a catch for said case. Maybe acceptable, but never a good look
Wanted to save the original here before I try and go back and clean it up. And then we'll look at 
the solution. 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        res = ListNode()
        temp = res
        val1, val2 = 101, 101
        while list1 or list2:
            if list1:
                val1 = list1.val
            if list2:
                val2 = list2.val
            if val1 < val2:
                temp.val = val1
                if list1:
                    list1 = list1.next
                if not list1:
                    val1 = 101
                if not list1 and not list2:
                    break
                temp.next = ListNode()
                temp = temp.next
            else:
                temp.val = val2
                if list2:
                    list2 = list2.next
                if not list2:
                    val2 = 101
                if not list1 and not list2:
                    break
                temp.next = ListNode()
                temp = temp.next
        temp = None
        return res

"""
Heres what I came up with after messing around with it for another 20 minutes
I would say with what I know now this is my best solution
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        res = ListNode()
        temp = res
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    temp.val = list1.val
                    list1 = list1.next
                else:
                    temp.val = list2.val
                    list2 = list2.next
            elif list1:
                temp.val = list1.val
                list1 = list1.next
            else:
                temp.val = list2.val
                list2 = list2.next
            if list1 or list2:
                temp.next = ListNode()
                temp = temp.next
        return res

