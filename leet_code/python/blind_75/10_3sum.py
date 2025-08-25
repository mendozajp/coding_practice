"""
https://leetcode.com/problems/3sum/
2 pointers question. I had attempted it before and forgot to put my first pass here
conceptually we were right there, my only issues is that I was reducing the search
area for the 3rd character which ended up mising a lot cases and I was a bit unclear about 
which side to increment when we find a valid sum. Looking at the solution showed that it was 
actually both, which didnt make sense right away but it was because I was shortening the search
area. once we iterate though the list in tandem with our 2 pointers (yes its gonna be O(n^2)) then
we start seeing success. I haven't implemented that so I'll do that as this entry. 

Times up, couldnt get a solution fast enough. Passing the original test cases very quickly but
kept getting bogged down on edge cases. Actually not even edge cases, some situations I would
expect our implementation to be fine so we just did something wrong. Heres the code. 
"""
class Solution(object):
    def sum_three(self, i: int, j: int, k: int) -> int:
        return i + j + k


    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result_list = []
        nums.sort()

        left_id = 0
        right_id = len(nums) - 1

        while left_id < right_id:
            idx = 0
            sub_sum = 0
            while idx < len(nums):
                if idx == left_id or idx == right_id:
                    idx += 1
                    continue
                current_sum = self.sum_three(nums[left_id],nums[right_id],nums[idx])
                if current_sum == 0:
                    sol = [nums[left_id],nums[right_id],nums[idx]]
                    sol.sort()
                    if sol not in result_list:
                        result_list.append(sol)
                    left_id += 1
                    right_id -= 1
                    break
                else:
                    sub_sum += self.sum_three(nums[left_id],nums[right_id],nums[idx])
                    idx += 1
            if idx == len(nums):
                if sub_sum > 0:
                    right_id -= 1
                elif sub_sum < 0:
                    left_id += 1
                else:
                    left_id += 1
                    right_id -= 1
        return result_list
                
"""
Honestly our first attempt was better then this. 
In our other solution we used in alot, thinking that we need to be shortening the list. The 
solution I read now actually ends up doing that as well.
Gonna restart it, try one more time.
"""

class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        left = 0
        increment_left, increment_right = False, False
        right = len(nums) - 1
        nums.sort()
        print(nums)
        while left < right:
            print(nums[left], nums[right])
            if -(nums[left]+nums[right]) in nums[left+1:right]:
                res.append([nums[left],nums[right],(-(nums[left]+nums[right]))])
                increment_left, increment_right = True, True
            elif (nums[left]+nums[right]) > 0: # value large, attempt to make smaller
                increment_right = True
            elif (nums[left]+nums[right]) < 0:
                increment_left = True
            else:
                increment_right, increment_left = True, True
            if increment_left:
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    print("left incremented")
                    left += 1
            if increment_right:
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    print('right decremented')
                    right -= 1
        return res
    
"""
lol okay so this is kinda what I had before and its actually 100% worse then up above. 
I seem to be missing something critical. Gonna anotate through the solution below.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []                                                # init res arr
        nums.sort()                                             # starting sort for 2 pointer usage

        for i, a in enumerate(nums):                            # bit weird but okay, we're gonna hit everything at least once. 
            if a > 0:                                           # looking a bit ahead, left is started with i + 1, so anything above 0 will never work, makes sense
                break

            if i > 0 and a == nums[i - 1]:                      # skip over duplicates, again makes sense. seeing it as the for loop is a bit weird though
                continue

            l, r = i + 1, len(nums) - 1                         # starting the 2 pointers from i is different from what we were doing, i will never be incremented so instead of our approach, they are
                                                                # looping over with the 2 pointers every time
            while l < r:                                        # same stopping method as us
                threeSum = a + nums[l] + nums[r]                # immeditatly save the sum of 3 for each iteration
                if threeSum > 0:                                # with going through 2 pointer iterations for every i, you pass my issue with not having a solid way to move l and r as with this youll
                                                                # see everything
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1                                      # incrementing both is fine since odds are we'll see the same l and r but in a different combination in a later run when i is increm.
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:     # this is interesting. Only skipping over left side duplicates. I suppose as long as one side is different we'll see something new, 
                                                                # and we'll run into that right side combination again with an i iteration
                        l += 1

        return res
    
"""
Purhaps the lesson learned here is that the algo in question doesn't have to be the focal point
in whatever your doing. Which is to say, it doesn't have to be the leading iterator or structuring
the entire problem. I was too stuck on the idea that since this is a two pointer question, two
pointers will structure the entire problem, I have to be iterating where its all over once l meets
r. And while to some extent that is right, it was a level deeper, where you actually use 2 pointers 
several times through iterations. 
So it goes. We'll try again in a few days.
"""