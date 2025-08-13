"""
https://neetcode.io/problems/is-anagram?list=blind75
easy
the turning to a list, sorting and then comparing might be suboptimal but it was the second thing
to pop into my head. The first was turn into a set and do a union, but the first test case had a 
string with more then one of the same char, so we could easily have like rrr and rrrr and that
would fail with a union.
So I just went with this. 
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        if s==t:
            return True
        else:
            return False
        

"""
They have a couple of solutions, this was your solution but better
this was the slowest of the 3 solutions they have
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

"""
The following 2 solutions match in speed and are after then the one above
using hash maps is the first one.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    
"""
the above makes the most sense to me. basically a dict where you track each char
and increment them as they come up, then just check if the dictionaries are the same

the last solution is doing the same thing but instead of using a dict, they use a list
26 elements long to indicate each char, and they increment if in one and decrement if in
the other, so if they are the same it should match. Very nice. 
"""