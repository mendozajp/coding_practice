"""
https://neetcode.io/problems/max-water-container?list=blind75
So I've seen this one before back before I started the blind. Was my first exposure to two pointers
actually so thats cool. I ended up remembering pretty well it seems. 
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = 0
        while l < r:
            edge = min(heights[l],heights[r])
            max_water = max(max_water, ((r-l)*edge))
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        return max_water

"""
Just to test preformance since blind doesnt really tell you, I put it up on LC and ended with 
beats 68% so thats cool. 
Good pattern to remember. Should be able to pull something like this out at the drop of a hat. 
"""