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

"""
Went and checked out the solution, one big difference
They check only if both list 1 and list 2. You'd think, well then how are they making sure
they are not making null comparisons? Well, the linked list is already sorted, so they just 
reassign the remaining list to the end of the res list. No need to keep iterating, which means
you don't need to check if one or the other is available. If one isnt then your pretty much done,
just add the other to the end.  
"""

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1                                               # assinging the whole node instead of just the value just makes way more sense then taking it all apart and putting it back together which is what you did.
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next                                                       # returning dummy.next is interesting too, as you can start with a listnode and not worry about populating the first val
                                                                                # and then moving on to the next, they just keep going from there, not caring about that first val and just returning next at the end. 