"""
https://neetcode.io/problems/longest-consecutive-sequence?list=blind75
Didnt really need to have a list saving them all but it helped with debugging
Also was able to nicely get rid of the falsy test cases with a oneliner cause of it so thats cool
idea was basically iterate through counting up, after sorting, if its one up, add to list, if not
then reset the list, save if its the largest and continue. 
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = sorted(set(nums))
        i = 0

        largest_seq = [1] if len(s) > 0 else []
        current_seq = []
        while i < len(s):
            if len(current_seq) == 0:
                current_seq = [s[i]]
                i += 1
                continue
            if s[i] == current_seq[-1] + 1:
                current_seq.append(s[i])
            else:
                if len(current_seq) > len(largest_seq):
                    largest_seq = current_seq
                current_seq = [s[i]]
                i +=1
                continue
            if len(current_seq) > len(largest_seq):
                largest_seq = current_seq
            
            i += 1
        return len(largest_seq)

"""
The Ideal solution has us making a set, like we did here, but keeping it as a set, searching for 
num -1 since if there is one, we do not have a starting point yet. 
I don't think its much better then this one though. With this strategy, I would assume we have to keep searching
in the set for num -1.
Lets look at the solution. 
Okay theres a hash map and a hash set solution, both the same time and the hash set is def the better solution
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

"""
Very clean, just using in, which is crazy cause that was our first thought but I figured it be a lot slower. 
in for sets is still worse case O(n) just like a list. Oh no, in is O(1) average. its only O(n) for hash collisions
very good to know. We'll be using that one in the future for sure. 
"""