"""
https://neetcode.io/problems/maximum-subarray?list=blind75
Just before going into this one I listened to a podcast talking about the greedy algo, which is 
what this question is about. Conceptually pretty simple, went into this problem and I couldnt 
really put it into practice. Couldnt really hammer down what exactly needed to happen for me to
opt to take the another choice besides the next one because of the number range. If it was just
as long as its over 0 or greater then current_sum, then that would have been simple, but since 
you can have a starting value that is negative, and can 100% take a loss in the short term and 
end up with a gain at the end, I didn't really understand how (at least the greedy algo that I 
heard) the greedy algo could be implemented here. 
So I stopped and started reading the solution.
This is where I left off. Not passing any test cases. 
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # beginning with logic that if a subarrays sum is negative, its not worth continuing
        # that is not actually true since the contraints are -1000 <= 10000
        highest_sum, current_sum = 0, 0    
        idx = 0
        while idx < (len(nums)-1):
            if idx == 0:
                current_sum = 0
            elif current_sum + nums[idx] > current_sum:
                current_sum += nums[idx]
                highest_sum = max(highest_sum, current_sum)
            else:
                temp_sum = current_sum + nums[idx]
                if idx + 1 > len(nums):
                    for i in range(idx+1, len(nums)-1):
                        temp_sum += nums[idx]
                        if temp_sum > current_sum:
                            highest_sum = max(highest_sum, temp_sum)
                current_sum = 0
            idx+= 1
        return highest_sum
    
"""
Kadane's Algorithm is listed as the best solution at O(n)
but there are a total of 7 different solutions. 
I know we always go for the best, and not getting any of them maybe is not how you should think
about it but we should be aware of the various different approaches you can do for a problem. 
1. Brute force
2. Recursion - Very difficult to read by condensing all logic into recursion, single return 
    in each call, check for len and flag, which seems to represent if we are negative? Not sure
3. Dynamic programming (top-down) - populating a lists of lists with values and then returning the 
    first value, list is populated recursivley
4. Dynamic programming (bottom-up) - same concept but the other way. This one is a lot shorter
    but also alot uglier
5. Dynamic programming (space optimized) - Conceptually the same, populating a list of len(nums) 
    and then reassigning each element to the max of it and its neighbor, and then returning the max
    This ones interesting, I'm gonna put this one below. 
"""

class Solution:
    def maxSubArray(self, nums):
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        return max(dp)
    
"""
I actually like that solution alot. You compare a value and its previous one, take the max, the 
greedy strat at its core, then you reassign it. its almost the same as just maintaining a 
current_sum like above but you save it along the way in the list. Each element is reassigned to 
the sum from its previous values if its better, or to itself since adding it to the sum before 
it would not have resulted in something higher then it.

I had something like this very earily on but then changed it for what I had above. 
Gonna try the same concept to what I had going on before. 

Check this out, ended up working out great
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum, highest_number = 0, -1e4                       # didnt have that starting -1000 before. Critical since we have such high negatives and 0 is a number too not just a starting place
        for i in nums:
            if current_sum + i >= i:                                # this is really the only thing I missed, since this is basically what I had but without this condition, I was checking against current_sum
                                                                    # when I should have been checking against i itself. That was the bit of logic I was missing. This is were Greedy came into play perfectly
                current_sum += i
                highest_number = max(current_sum, highest_number)
            else:
                current_sum = i
                highest_number = max(current_sum, highest_number)
        return highest_number
    
"""
That above solution that we made is almost exactly Kadane's Algorithm, which is this questions 
best solution, so very nice work. Ill put said algorithm below for reference.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub