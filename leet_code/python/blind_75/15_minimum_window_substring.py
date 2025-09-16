"""
https://neetcode.io/problems/minimum-window-with-characters?list=blind75
Haven't done any hards in the blind yet, at least seriously, since this was the first one I wanted
to spend more time on it. As long as I wasn't completley stuck. The general movement of the window
we got down with only a couple of minor tweaks needed, mainly with the seperation of the movements
of both left and right in their own loops, which is a pretty standard part of the whole sliding
window thing. Regardless, this took us a bit but its all us. Ran into some of the same pain points
that I typically run into and I want to note some of them.
 - loop conditions, the loop for moving l was l<r for a while, took us a bit to figure out we
    needed to occationally match r, and seperatly we needed to make sure we don't go out of
    bounds.
 - when to increment when using while loops, for our r movements, we got that pretty quickly
    but l needed some additional chances and it was hard to see all of them right away.
those were really my biggest complaints, mainly because they were the reason we ended up taking
so long. Our design took a bit but debugging and iterating took longer.

I put this on LC and it passes everything, but its pretty slow. 8% I think.
But hey thats our solution right there.
"""


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        mappings = {}
        res = ""
        for i in t:
            mappings[i] = mappings.get(i, 0) + 1
        l, r = 0, 0

        while l < len(s):
            # move r until success
            while r <= len(s) - 1:
                if s[r] in mappings.keys():
                    mappings[s[r]] -= 1
                    if all(value <= 0 for value in mappings.values()):
                        if not res:
                            res = s[l : r + 1]
                        else:
                            if len(res) > len(s[l : r + 1]):
                                res = s[l : r + 1]
                        break  # start moving l, see if something smaller then this is possible
                r += 1

            # now that we have a successful substring, we need to try to make it smaller
            while l <= r and l < len(s):
                if s[l] not in mappings.keys():
                    l += 1
                    continue
                if all(value <= 0 for value in mappings.values()):
                    if len(res) > len(s[l : r + 1]):
                        res = s[l : r + 1]
                    mappings[s[l]] += 1
                    if mappings[s[l]] <= 0:
                        l += 1
                        continue
                    l += 1
                    break
                mappings[s[l]] += 1
                l += 1
            if r < len(s):
                r += 1  # we left r at a key value, increment it so we dont hit a key twice

        return str(res)


"""
Now lets look at some solutions. 
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = (
            {},
            {},
        )  # 2 dicts is interesting. But they do track t in a dict which is good to see
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(
            countT
        )  # concept of a need feels like a waste of time but okay.
        res, resLen = [-1, -1], float(
            "infinity"
        )  # infinity for an easy first time check and final confirmation
        # actually now that I think about it, with this, we don't really need to be constantly
        # checking a sublist for confirmation, we can just say its good.
        # now that I think about it, we didnt actually need to be slicing and reseting res,
        # we really only needed the 2 ends and we could slice at the end.
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""


"""
Their concept is the same as my sliding window, they just went about it more efficently. Thats good
Having the second dictionary for the window itself lets them not need to check against values like 
we did with all, which probably helps alot in terms of speed. Having res just be l and r, saves a 
lot of memory and avoids a bunch of slicing until the end which is cool. And since you don't have 
the whole list, saving the len makes sense. 

Only having 2 loops in this solution makes it way better for readability. Since your plan was to
move r until you had a hit and then move l until you didnt, using a for loop is something you 
should have considered for r. Lets us avoid using breaks and continues to. which are fine, but
keeps things sequentail.

We should for sure come back to this question later. I want to be able to use that sort of saving
pointers till the end strat, and piggybacking off of the 2 seperate dictionaries for speed. 
"""
