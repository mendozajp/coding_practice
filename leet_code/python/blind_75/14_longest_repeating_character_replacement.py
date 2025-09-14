"""
https://neetcode.io/problems/longest-repeating-substring-with-replacement?list=blind75
Sliding window question. One of those algos I still have a bit of trouble putting into practice
I get it conceptually but struggle with it sometimes. This one I was thinking, slowly expand your
window when you see matching letters, once you see a break, deduct k by 1 and continue anyways
once you run out, then you know your at the max you can get.
It feels kind of like a sliding window but that the window is consistently resized, which is
normal. That idea let to the below code.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        largest = 0
        for idx, letter in enumerate(s):
            k_remaining = k
            temp_id = idx + 1
            curr = 1
            while temp_id < len(s):
                if s[temp_id] == letter:
                    curr += 1
                    temp_id += 1
                else:
                    if k_remaining > 0:
                        k_remaining -= 1
                        curr += 1
                        temp_id += 1
                    else:
                        break  # no more replacements, substring broken
            if k_remaining < idx:  # check for k_remaining replacements backwards
                curr += k_remaining
            else:
                curr += idx
            largest = max(curr, largest)
        return largest


"""
This passes the blind, but I wanted to see its preformance on LC, there it times out.
I swapped it to a while loop and jumped around a bit more for any unbroken sections and that
passed a couple more test but there was an even bigger test case that still timed out. Don't think
we could be much more preformant with this strategy. At least that I can see in the short term. 

The optimal solution is a sliding window, we already knew that. But they did it a lot differently
then I did. some of the same ideas, but they more fine tuned their window resizing, where you just
kinda make it bigger till you reach the end of cant anymore and then restart. 

"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(
                s[r], 0
            )  # normal use case is frequency counting
            maxf = max(
                maxf, count[s[r]]
            )  # getting the match substring if unbroken. Checks being after is interesting, but they're not returning this.

            while (
                r - l + 1
            ) - maxf > k:  # (r - l + 1) - maxf counts up the eqivalent of k_remaining in our apporach. How many chars can be replaced.
                # if you enter the loop, typically means you ran out of replacements.
                count[
                    s[l]
                ] -= 1  # Not sure whats going on here, reducing the frequency something was seen. Oh, so this count, only ends up being what is in the window.
                l += 1  # counting up the left pointer, reducing the window size and technecally giving you an extra k_repalcement.
            res = max(
                res, r - l + 1
            )  # then all that matters is the length of the unbroken substring.

        return res


"""
So your approach is a lot closer to the brute force. You look at every value, and then iterate 
after that value until you run out of k replacements. If you hit the end, you use your k 
replacements backwards. After you finish looking at each value though, you completly restart
at 1 value, and then extend as much as you can. Hence the similarity to brute force. 
The optimal solution, maintains a window, they start at some value, they go as much as
they can with a combination of unbroken values and k replacements, but then instead of restarting
they shorten the window by just 1, so they can keep going forward by 1. Its a loop cause it can be
any amount not just one, but just as an example. So just remember the whole point of sliding window
is to maintain that window of data for scrutiy. If you find yourself starting with very little data
between iterations, ask yourself. Is this really a sliding window approach? 
"""
