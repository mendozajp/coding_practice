"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
I don't have a ton to say about this one. Linked list are seemingly always very restrictive when I see any questions about them.
Started timing myself until solved submission, after 30 minutes I close it out. I reset the timer too quickly but I think this one 
was around 20 minutes. Only took that long cause I forgot that with LLs the order is reversed if you manually put it back together as
you unstring it. Did that first thinking I wouldn't have to do the obvious solution of just putting it into a list and then putting it
back together. Which is what I ended up doing. Bottom like 7% for preformance. Which was expected.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = None
        values_from_linked_list = []
        last_value = -1
        while head:
            if head.val not in values_from_linked_list:
                values_from_linked_list.append(head.val)
            head = head.next
        for value in values_from_linked_list[::-1]:
            result = ListNode(value,result)

        return result
    

"""
Editorial solutions below
Check this out this ones kinda nutty
"""

class Solution(object):
    def deleteDuplicates(self, head):
        temp = head
        while (temp and temp.next):
            print(head)
            if (temp.next.val == temp.val):
                temp.next = temp.next.next
                continue
            temp = temp.next
        return head
    
"""
so while temp and temp next are availble, checking next as well, we check the val of next and current val,
if they match, you asign next node right then and there and then you continue, skipping over that last one. if its good, then you 
move on to the next node. There you really are only iterating once. Actually you're iterating a bit less then the original len
so its even better.

Its funny every time I do a new problem the solution ends up seeming obvious after seeing what it was. Though I haven't done as 
as many hard problems, but they are probably just more math heavy. 

But I guess it's all about learning new patterns at the end of the day, which is why the timer is so important. Wasted way to much time
on 11. As long as you check out the editorial and do an introspective I guess then it's good. Next linked list question you 
better believe I'm pulling this out. Well I suspect it'll be a new pattern so who knows really.  
"""