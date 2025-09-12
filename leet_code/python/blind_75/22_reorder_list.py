"""
https://neetcode.io/problems/reorder-linked-list?list=blind75
So my first thought was to do this. Which I've never done before since I typically don't import
anything for these questions.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = deque()
        temp = head
        while temp:
            nodes.append(temp.val)
            temp = temp.next

        while nodes:
            if nodes:
                head.val = nodes.popleft()
                head = head.next
            if nodes:
                head.val = nodes.pop()
                head = head.next


"""
Very simple, very clear whats going on, and it works. Its around 33% eff. but pretty close.
I didn't actually do that above first, I instead reversed the list and then with head and the 
reverse of it, made a new list. That didnt end up working cause I was improperly changing the 
values in place and I ran out of time. That did work though. I tried the above just to get 
something working. 

The solution has that sort of 2 pointers solution again. 
Don't like this type of solution, hard to keep track of things in my head. Wanted to get it down 
here and see if we can go through it. 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = (
            head,
            head.next,
        )  # 2 pointers setup, interesting enough they start right after the other, since you cant start from both ends, best you can do.
        while (
            fast and fast.next
        ):  # The concept of one being faster then the other I don't entirly get in this context. In the previous one, they eventually loop
            # to touch all values, but here we need to alternate beginning and ends.
            slow = slow.next
            fast = fast.next.next  # case [2,4,6,8], after this loop slow = 4, fast = 8

        second = slow.next  # second = 6
        prev = slow.next = (
            None  # prev = second = 6 = None - not sure whats going on here.
        )
        while second:  #
            tmp = second.next  # tmp = 8
            second.next = prev  # second.next = None
            prev = second  # prev = 6
            second = tmp  # second = None
            # so only thing that changed there was prev, to second, which is 6

        first, second = head, prev  # second is now 6 which is what it was eariler
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


# yeah still not following. Lets come back to this later. I want to shift focus to math and geo for now.
