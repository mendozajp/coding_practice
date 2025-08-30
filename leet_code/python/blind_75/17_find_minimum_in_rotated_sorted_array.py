"""
https://neetcode.io/problems/find-minimum-in-rotated-sorted-array?list=blind75
First question in the binary search category. I did a tiny primer on it before starting.
When I switched over, I realized I understood conceptually what to do but had no idea
how I would actually go about conducting that iteration. This completly stonewalled
me as I could not figure it out. After exceeding my time limit by more then I will
admit, heres what I ended with.
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = 1001
        l = 0
        r = len(nums) - 1
        idx = (r - l) // 2
        while idx not in (l, r):
            print(idx)
            min_val = min(min_val, nums[idx])
            if min_val > nums[r]:
                l = idx
                idx += ((r - l) // 2) if ((r - l) // 2) != 0 else 1
            else:
                r = idx
                idx -= ((r - l) // 2) if ((r - l) // 2) != 0 else 1
        return min_val


"""
the while condition I for the life of me could not figure out. 
Looking at the solution, I was very very close, but I just couldn't see it
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1  # init l and r, so they used a similar framing device
        while (
            l < r
        ):  # simple enough, I tried this and with the way I was setting l and r led to me thinking this wasn't it
            m = (
                l + (r - l) // 2
            )  # I didnt add l, I just had (r-l) // 2, but I kept adding it to a saved index
            if (
                nums[m] < nums[r]
            ):  # Saw something different, I saw, if right most is smaller then current, min should be between current and right
                r = m  # similar enough, this is if current is smaller then right, everything to the right is increasing, ignore
            else:
                l = (
                    m + 1
                )  # m + 1 to keep things moving maybe? I started with r and l = idx, but kept hitting endless loops
                # not convinced that its not just cause of a bad loop condition.
        return nums[l]


"""
No checking for min value, they just end at it after the search. Guess that is the point of the 
search in the first place, you should always end there if you're doing it right. Surprised I
didn't see that. 

So things to take home:
 - concept of a search algo is to look for something specific, you will end at your goal, no need 
    to dedicate memory to saving values for the same purpose
 - don't just set new values unless your sure you are incrementing, leads to endless loops, you 
    eventually want both walls to intersect, shows theres nothing left to do. 
"""


"""
5 days later, came back to revist this, I remembered it pretty well. Actually remembered it 
perfectly now that Im looking at that previous answer
Remembered end condition is l and r intersec, didnt need to save max as your last value will
be what you want, and from then it fell into place. 
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            idx = l + ((r - l) // 2)
            print(f"At index {idx}")
            if nums[idx] > nums[r]:  # we know smallest value beteween idx and r
                l = idx + 1  # increment to make progress, no need to include it
            else:
                r = idx
        return nums[(l + ((r - l) // 2))]


"""
They did return l though instead of say m. One less calculation on their part, at that 
point they would be equal, which makes my equation just give l so that makes sense. 
"""
