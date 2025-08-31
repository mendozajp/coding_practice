"""
https://neetcode.io/problems/find-target-in-rotated-sorted-array?list=blind75
Just did a runback with the og binary search question, figured I'd knock the other one out now
to fully solidify the concept within us. Since this is just the previous question but with more
complixety, it works out perfectly.

After working on it for a while, I got to the point where I kinda just needed to figure out the
conditional but I couldnt get it in a reasonable time, After looking at the solution, (tried not
to look to hard, was hoping for a hint) I realized they were comparing things I didn't think about.
The goal was to find where that pivot point was, I orignally didnt think about it like that, mostly
just thinking were the number was, after that I spend a bit more time and came up with this.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        idx = l + ((r - l) // 2)
        while l < r:
            if nums[idx] == target:
                return idx
            if nums[idx] > nums[r]:
                if target > nums[idx] or target <= nums[r]:
                    l = idx + 1
                else:
                    r = idx - 1
            else:
                if target > nums[r] or target < nums[idx]:
                    r = idx - 1
                else:
                    l = idx + 1
            idx = l + ((r - l) // 2)
        if nums[idx] == target:
            return idx
        return -1


"""
Funny enough there was a point were I was like, man it would be nice if I knew where the lowest was
what if we just binary search once to find that min, then we know were it is and can search with it
in mind? but figured it kinda defeated the purpose of the exersise, lo and behold, one of the 
solutions was doing just that. Since your running binary search, even if its a couple of times its
still O(log(n)) since its really only O(2log(n)) which is effectively the same thing. 
"""
