"""
https://neetcode.io/problems/longest-substring-without-duplicates?list=blind75
Havent done a sliding window in a while. Took me a bit cause I was trying to do some dictionary
optimizations which ended up not working out but after just diong the obvious loop in, I got it
sorted and checked it on LC as well and its not the worse thing we've seen in terms of preformance.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = []
        highest = 0
        for i in s:
            if i in current:
                highest = max(highest, len(current))
                slide_to = 0
                for idx, x in enumerate(current):
                    if x == i:
                        slide_to = idx
                        break
                current = current[idx+1:]
                current.append(i)
            else:
                current.append(i)
        highest = max(highest, len(current))
        return highest
    

"""
Their sliding window approach is a bit better then mine but conceptually the same. They used a set
which I didnt think would work since we kind of need to maintain order. But actually you don't, as
long as you know the order in which you added values, since you have the og string, you do have 
that. So you're still iterating through an additional time looking for whatever value you want to 
slice to, but since they have it in a set, that whole process is a lot faster. Remember slicing 
itself is a O(len of slice) so just dropping from the set is way better in comparison.  
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
    
"""
Know that their optimal sliding window solution involved dictionaries maintaining keys like 
you were thinking. So I'll put it here so you can reference. Gotta learn map. We don't use it 
enough. 
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res