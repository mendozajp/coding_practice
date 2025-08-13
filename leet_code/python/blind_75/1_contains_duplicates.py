"""
https://neetcode.io/problems/duplicate-integer?list=blind75
easy
Solution took me 2 seconds, just checking if there are dups. Nothing new here
sets have no dups, check for different in len
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) > len(set(nums)):
            return True
        else:
            return False