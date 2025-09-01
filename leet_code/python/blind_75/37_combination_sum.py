"""
https://neetcode.io/problems/combination-target-sum?list=blind75
So I've tried this one before but I keep ending up confusing the hell out of myself with the 
recursive logic, when things are supposse to be doing what their doing. Going into the runback
the only thing I really remembered was the concept, which sort of got going kind of quickly but
ended up running to a whole slew of problems pretty quickly. 
"""

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            print("They lied to us")
            return []
        res = []
        nums.sort()
        current_sum = 0
        current_values = []

        # recusive function
        def deep_search(starting_point: int, current_sum: int, current_values: list) -> None:
            for idx, val in enumerate(nums[starting_point:]):   # bro, this idx will always start at 0, and you pass it later to deep_search, this is why you have duplicates in res
                if val > target: return None
                current_sum += val
                current_values.append(val)
                if current_sum > target:
                    current_sum -= val
                    current_values.pop()
                    return None
                if current_sum == target:
                    res.append(deepcopy(current_values))
                    current_sum -= val
                    current_values.pop()
                    return None
                deep_search(idx, current_sum, current_values)
                if current_values:
                    current_sum -= val
                    current_values.pop()

        
        for idx, val in enumerate(nums):
            current_sum =  val
            current_values = [val]
            if current_sum == target:
                res.append(current_values)
                continue
            if current_sum > target:
                continue
            
            deep_search(idx, current_sum, current_values)
        return res

"""
I shy away from kinda housing all that logic in the recur. fn but thats what the solution did and 
it made it seem pretty simple. Actually having it all be in the recurv. makes it a bit easier to
 focus on so we should have just done that if we could have. 
"""

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()                             # same thought on sorting, just makes it faster to parse through in the longrun

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            for j in range(i, len(nums)):       # basically had the same thought for our loops but this is kind of easier to understand. 
                if total + nums[j] > target:    # doesnt change total, just checks if its over, if it is, backout, pop is next.
                    return
                cur.append(nums[j])             # curr gets past along in a similar way but less happens to it along the way, less error prone. 
                dfs(j, cur, total + nums[j])    # just pass through the added total, no real need to save it. 
                cur.pop()

        dfs(0, [], 0)                           # single call does it, since the call itself checks for target hits and adds them into res right at the start
        return res
    
"""
Alright I was looking at my code and solution trying to get some way for them to meet in the middle
I put a comment up there, I realized what we were doing, for i, x in enumerate will always start
from 0, the solution uses range and an incrementing i. I also got rid of the inital loop we had up
there since I realized the recuv. basically needs no changes to do that too. 
Check it out, this works. 
"""

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            print("They lied to us")
            return []
        res = []
        nums.sort()
        current_sum = 0
        current_values = []

        # recusive function
        def deep_search(starting_point: int, current_sum: int, current_values: list) -> None:
            for idx in range(starting_point, len(nums)):
                val = nums[idx]
                if val > target: return None
                current_sum += val
                current_values.append(val)
                if current_sum > target:
                    current_sum -= val
                    current_values.pop()
                    return None
                if current_sum == target:
                    res.append(deepcopy(current_values))
                    current_sum -= val
                    current_values.pop()
                    return None
                deep_search(idx, current_sum, current_values)
                if current_values:
                    current_sum -= val
                    current_values.pop()

        deep_search(0, current_sum, current_values)
        return res
    
"""
You were right there, but you were bogged down by a bit of a logical blunder. So it goes."""