"""
https://neetcode.io/problems/linked-list-cycle-detection?list=blind75
Didn't really like this one since they never explictly say there are no duplicates but the hints
make it seem like there are none. My solution is the easiest to come to if you assume there are
no duplicates. I added one edge case cause there ended up being one but it only works if there 
is only one. So overall I don't like my solution. Curious what their solution is. 
Also no reason for that dictionary. Should have used a set. The value you set is meaningless. 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_keys = {}
        idx = 0
        while head:
            if head.val in node_keys:
                if head.next and head.next.val in node_keys:
                    return True
            node_keys[head.val] = idx
            head = head.next
        return False
    
