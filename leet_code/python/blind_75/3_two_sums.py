"""
https://neetcode.io/problems/two-integer-sum?list=blind75
Its a pattern I've used before but one I didn't really think to use for this problem until I looked
at some hints. Keep forgetting that getting things from dicts are just way faster and if you can 
deligate searching to it you should. 
My first thought was using a bunch of ins and if you find it go get the id and your done, but in is
iterating through the list in the first place so I knew I didnt want to do that, I thought of using
a dict and my thought process regarding the matter started and stopped right there. Could have, 
should have, just didn't 
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for idx, number in enumerate(nums):
            if number in indexes:
                return [indexes[number], idx]
            else:
                indexes[target-number] = idx 
        return [0,1]
    
"""
You ended up getting it so its cool, but we have a bad habit at following one though to ruin
incorperate differnt strategies, if you think something is too slow, remember there are 
other types that are just faster.

At the very least, the solution you gave was their best solution so actually just good stuff. 
"""