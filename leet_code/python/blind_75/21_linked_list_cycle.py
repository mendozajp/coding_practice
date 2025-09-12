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


"""
Okay their solution with the set is cool and I want to talk about it
"""


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        cur = head
        while cur:
            if cur in seen:
                return True
            seen.add(
                cur
            )  # really the only interesting part is adding a whole node to the list, which will only ever already be in the set if you loop back
            # which gets you around the problem of potentally having duplicates. Very smart.
            cur = cur.next
        return False


"""
Then just for the hell of it I'll throw in the 2 pointers one, but I don't actually like the 
solution cause it kinda involves looping over until they just so happen to match up, since if 
there is a loop, you can keep going forever.
"""
