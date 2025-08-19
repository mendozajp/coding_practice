"""
https://neetcode.io/problems/products-of-array-discluding-self?list=blind75
overall the concept for this one was pretty simple. I did need up until the second hint before
I was confident enough to actually do anything on it though. Second hint was just can we avoid 
repeated work. Dividing by the single number you want to exclude from the total product will do it.
So this is the obvious solution from that approach, with the double 0 in nums edge case addressed first.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # multiple 0s case
        zero_present = False
        if 0 in nums:
            zero_present = True
            temp = deepcopy(nums)
            temp.remove(0)
            if 0 in temp:
                return [0]*len(nums)

        total_product = 1
        res = []
        for num in nums:
            if num == 0:
                continue
            total_product *= num
        for num in nums:
            if zero_present and num != 0:
                res.append(0)
            elif zero_present and num == 0:
                res.append(total_product)
            else:
                if num == 0: # was getting a run time error so I thought this was happening but apparently not. 
                    print("this should be impossible")
                    res.append(total_product)
                else:
                    res.append(total_product//num)
        return res
    
"""
I am actually happy with my solution. Its seemingly a bit messy but its very understandable. 
The ideal solution apparently didnt have any divisions.
Hold up the next hint might have given it to me. 
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_list = []
        suffix_list = []
        product_total = 1
        i = 0
        # prefix
        ignored_value = 1
        while i < len(nums):
            if i == 0:
                ignored_value = nums[i]
                prefix_list.append(1)
                i += 1 
                continue
            product_total *= ignored_value
            prefix_list.append(product_total)
            ignored_value = nums[i]
            i += 1

        # suffixs
        i = len(nums) - 1
        product_total = 1

        while i >= 0:
            if i == len(nums) - 1:
                ignored_value = nums[i]
                suffix_list.append(1)
                i -= 1 
                continue
            product_total *= ignored_value
            suffix_list.append(product_total)
            ignored_value = nums[i]
            i -= 1
        print(f"{prefix_list=}")
        print(f"{suffix_list=}")

        res = []
        i = 0
        while i < len(nums):
            res.append(prefix_list[i] * suffix_list[len(nums)-i])
            i += 1
        return res

"""
Yep that ended up working right away. This does feel a bit faster. Its also kinda simplier step by step.
Not really any ifs, just checking if we're on the first iteration, where as we have to check if there are 0s
and then check if there are 2 0s, and then if there are 0s present we have to do something but if there arent
we have to do other things. 

Yeah this one is pretty nice. 
I've seen the setup a couple of different lists a couple of times now. After the tip I got it going pretty quick
So I think implementing it we're good at, but we need to work on identifing when its best to use. 
"""