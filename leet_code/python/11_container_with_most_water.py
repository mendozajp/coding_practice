"""
#https://leetcode.com/problems/container-with-most-water/description/
My first passthrough on this question took too long and I couldnt figure out the proper way to go about it.
Yeah I could have done the brute force attempt but I know I can do that so I didn't want to. Was trying to find the most efficeint method and that after thinking aboout it for way to long I couldnt find it.
I started looking for patterns and ended up at a pretty nonsense coincidence that I latched onto after some surface level testing seemingly yielded good results. That pattern was, when 2 lines have a matching best case, they often end up being the 2 lines that correspond to the correst answer. The base test cases reenforce this though. So I spent way to much time working on that angle when I originally thought it probably was not gonna work. The first big of code below is that implementation. 

After this failed, I talked to J.G about the solution, he gave me something in c++ which I implemented into python

"""
# original implementation 

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        match_keys = {} # ex: 32: [] and we would append to that
        midpoint = len(height) // 2
        for id, line in enumerate(height):

            if id < midpoint:
                best_possible_result = line * ((len(height) - 1) - id)
            else: 
                best_possible_result = line * id

            if match_keys.get(best_possible_result):
                match_keys[best_possible_result].append(id)
            else:
                match_keys[best_possible_result] = [id]

        # now checking canidates
        top_canidate = 0
        for key, value in match_keys.items():
            if len(value) > 1:
                shorter_line = min(height[min(value)], height[max(value)])
                distance_between_lines = max(value) - min(value)
                if top_canidate < (shorter_line * distance_between_lines):
                    top_canidate = shorter_line * distance_between_lines
        if top_canidate == 0:
            highest_best_case = max(match_keys.keys())
            if match_keys[highest_best_case][0] < midpoint:
                distance_between_lines = len(height) - (match_keys[highest_best_case][0] + 1)
            else:
                distance_between_lines = match_keys[highest_best_case][0]

            shorter_line = min(height[match_keys[highest_best_case][0]], height[0], height[-1])
            top_canidate = shorter_line * distance_between_lines


        return top_canidate
    
"""
Yeah its so much more complicated then just doing brute force. That should have been the first clue. In our initial though process
we constantly thought that we should be looking at both sides, but we didn't go with that because we thought that would mean O(N^2)
I remember us thinking, we basically need, maximum distance with the 2nd biggest line since you go on the lower of the 2. 
This following tracks both ends of the list, starting at the highest length, we basically check the volume and if its higher then 
the highest, we save. Then we move the lower of the 2 lines, since the higher line could end up being higher if theres a bigger line 
in the middle somewhere. We calculate the distance between the 2 with the difference so thats all set from either being incremented. 
Thats all you need. 
Basically interating though the list only once, its just that you are closing in from both sides at the same time. 
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_id = 0
        right_id = len(height) - 1
        highest_volume = 0

        while right_id > left_id:
            current_volume = 0
            if height[right_id] >= height[left_id]:
                current_volume = height[left_id] * (right_id - left_id)
                left_id += 1
            else:
                current_volume = height[right_id] * (right_id - left_id)
                right_id -= 1
            highest_volume = max(highest_volume, current_volume)
        return highest_volume


"""
Better in every way. 
I feel like when we first started we had a better mindset, if we kept thinking about it we might have gotten it. But after finding a 
pattern I think you locked onto it way to hard. Starting off we were thinking it would be great if we could iterate from both sides
but I think I dismissed the idea too quickly. Give ideas maybe more of a shot from now on I suppose. 
"""