"""
https://neetcode.io/problems/decode-ways?list=blind75
Dynamic programming is something that we have not investigated very much. So not getting this
question is no surprise. got 17/25 but no where closer then that, got pretty hard stuck at
that point. When looking at certain situations, for longer strings, I could not come up with
how you would get all the combinations in a single iteration.
Here is where I left off.
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        count = 0
        idx = 0
        zero_found = False
        while idx < len(s) - 1:
            if s[idx] == "0":
                if not zero_found:
                    zero_found = True
                if s[idx + 1] == "0":
                    return 0
            elif int(s[idx] + s[idx + 1]) <= 26:
                count += 1
                if (idx + 2) < len(s):
                    if s[idx + 2] == "0":
                        count -= 1
                if s[idx + 1] == "0":
                    zero_found = True
                    idx += 1
            else:
                if s[idx + 1] == "0":
                    return 0
            idx += 1
        if zero_found:
            return count
        return (
            count + 1
        )  # adding one for the full single case. Though if there is even 1 zero i think you don't want to do this


"""
Feel like we stopped writing clean code at some point. feel like a lot of what we dish
out looks like this. Maybe it doesn't matter here, but you should be writing clean code
everywhere, not just where it matters. In reality it matters everywhere.

First approach which is simple enough is recursion. Wont go into much detail since its
somewhat self explainitory.
"""


class Solution:
    def numDecodings(self, s: str) -> int:

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i < len(s) - 1:
                if s[i] == "1" or (s[i] == "2" and s[i + 1] < "7"):
                    res += dfs(i + 2)

            return res

        return dfs(0)


"""
It handles the third of any given 2 digit num being a 0 well with its entry 
The idea is for every number, we iterate to the end, we count up for that combination
then we slowing count back every combination since then, adding that to the current iterations
results, and once you get back to the start, you have a baseline all single digits, and then 
every combination of a pairing infront with its baseline all single digits infront of it. 

Hopfully that makes sense. That took me a bit to get to. 


The dp solution here I wont get into to much detail yet. Come back after reading more about
dynamic programming. 
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)
