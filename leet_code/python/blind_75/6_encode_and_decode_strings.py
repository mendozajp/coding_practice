"""
Actually had a lot of difficulty with this one and couldn't figure it out. 
Spent too much time on it after going through several different iterations. 
All of which definetly way too complicated for what we needed to do. 
Here's were I stopped
"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        if strs == []:
            return ""
        for word in strs:
            if not word:
                res += "0_"
                continue
            res += str(len(word)) + "_"
        res = str(len(res + str(len(res)))) + "_" + res
        res += "".join(strs)
        print(res)
        return res
            
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        if s[0] == 1:
            return []
        starting_counter = 1
        for i in s:
            if i != "_":
                starting_counter += 1
            else:
                break 
        print(s[starting_counter:int(s[0])].split('_'))
        codex = [int(i) for i in s[starting_counter:int(s[0])].split('_')]
        index = int(s[0])
        res = []
        for length in codex:
            res.append(s[index+1:index + length + 1])
            index += length
        return res
    
"""
First solution is again this but simpler. And actually working this time

"""

class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s)) # counting up the lens first
        for sz in sizes:
            res += str(sz) # adding all the lens for words at the start of list like us
            res += ','
        res += '#'
        for s in strs:
            res += s # then adding all the words just like we did
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur)) # organizing numbers into the list like us, but without split which is a better move, such a headace cause of it
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz]) # was trying to do the same thing, when it worked it worked but kept failing for one reason or another for me. 
            i += sz
        return res
    

"""Tried to go back and fix mine since they were so similar but couldnt do it.
Its def closer but I got to a test that was failing for a reason i didnt know and decided to call it.
We'll revisit this one later. 
"""