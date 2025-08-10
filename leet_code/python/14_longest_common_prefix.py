"""
https://leetcode.com/problems/longest-common-prefix/description/
didnt see a fast way to do it in under o(n^2) so I went with that approach but I couldnt finish
it in time. I thought to save the smallest string first and then iterate over that string, 
looking each individual character along each string throughout the list. The second it didnt 
match, save the index and result smallest_string[:id]
but I think my loop didnt process what happens when the entire shortest string is in every 
other element, which led to 72/126

"""
# 72/126 test cases
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]

        shortest_string = strs[0]
        for i in strs:
            if len(i) < len(shortest_string):
                shortest_string = i
        
        result = 0
        for i in range(len(shortest_string)):
            match = True
            for word in strs:
                if shortest_string[i] != word[i]:
                    match = False
                    break
            if match == False:
                result = i
                break
            else:
                result = i
        
        if result == 0:
            return ""
        return shortest_string[:result]
"""
alright you know what I spent another 10 minutes on it. 
It was a couple of things. slicing for the result means you cant have :0 casue that gives you ""
1 will give you the first element, so you kinda have to start from 1 and then be incrementing up. 
also moved the return "" condition to the middle cause it was a better place for it. 
After submitting it beats 100% so we're good actually. Lemme put my slightly adjusted one below
"""
# beats 100%
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]

        shortest_string = strs[0]
        for i in strs:
            if len(i) < len(shortest_string):
                shortest_string = i
        
        result = 1
        for i in range(len(shortest_string)):
            match = True
            for word in strs:
                if shortest_string[i] != word[i]:
                    if i == 0: return ""
                    match = False
                    break
            if match == False:
                result -=1
                break
            else:
                result +=1
        
        return shortest_string[:result]
    

"""
Quick check to see if anyone did anything worth mentioning
its mostly nested loops like us, but they just grabbed the first one, and tried to match it with everything else, 
When it didnt they just made it smaller and tried again. Def don't need to find the smallest first, maybe it makes it
faster, but I doubt by any measureable amount. 

someone else sorted the list, then grabbed the last one, which I think gives you the shortest one
in searching it up apparently you can do min(the_list, key=len) to get the shortest one so thats pretty cool. 

there is one that only looks at the first and last elements which is interesting. Not sure how that can pass
since if you have something like ["length", "tonighttonight", "lengthwidthheight"] it should fail.

oooh shit i think sorted sorts based on characters
so sorting that list brings tonighttonight to the end and you can make the comparisons. 
Alright I like that one. Ill put it below. It only has one loop. thought I think sorted is slow O(n log n)
apparently so not bad. 
"""

class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 