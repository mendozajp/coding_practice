"""
https://leetcode.com/problems/trapping-rain-water/description/
First hard problem this time around. 
Should have been thinking of that before I decided to spend liek 5 hours on it over the course of 2 days. 
I'm finding that these algos are very much you either know it or you don't and if you don't, you should really
be spending your time learning them instead of bashing your head into figuring out an optimal solution.
The amount of times I thought of something and said 'no that wont work its not optimal' was insane. 
After several hours I went with an approach that I thought might work. My attempt at a brute force 
Was able to solve 321/324 test cases, but then from those test cases I realized my design was flawed. 
I think I could have changed it up a bit but I sunk to much time so I accepted the loss. 
Maybe thinking about it as a loss is the problem...

Regardless, I went through a couple of different designs
First was iterating through, saving the last seen height and the current height
the objective was to watch for height increases, while saving height decreases in a dictionary
so if the height increases, we check the dict, if theres anything there (any height decreases before, implying a divit)
then we run through the dict calculating any water collected. Then I would remove those from the dict. 
The idea was to basically collect by the smallest divit seen first and then handle the top

The logic for the top was flawed though, as if you had a lot of alt changes within 2 larger walls, I didn't have a good
way to calculate that. That was the big reason I stopped thinking that way. Thought I could have found and saved the 
largest seen inbetween segments but I think that didnt end up working for one reason or another. 

I didnt end up submitting the code for this design so I lost it, but later I moved to a different line of thinking.
What if we just calculate best case senario all the water possible, and then when we find the second largest (or next)
we just calculate overflow based on the difference? 
This potentially involves iterating through the whole list several times if there is nothing to stop the left most side
was one of the main problems. Actually that was THE problem. Because it ended up working, except for 4 test cases that only
decrease with massive canals within them. So on that one I kinda thought the design was just flawed. 

Too much talking, heres the last bit of code that got 321/324

"""

class Solution(object):

    def trap(self,height):
        """
        :type height: List[int]
        :rtype: int
        """
        _id, LH, LHid, total_water = 0, 0, 0, 0
        while _id < len(height):
            if height[_id] < LH:
                temp_id, temp_water, lower_max, lower_max_id, lower_max_temp_water = deepcopy(_id), 0, 0, 0, 0
                while temp_id < len(height):
                    # iterate until you reach EOF, LH or higher
                    if height[temp_id] < LH:
                        temp_water += (LH - height[temp_id])
                        if height[temp_id] > lower_max:
                            lower_max, lower_max_id, lower_max_temp_water = height[temp_id], deepcopy(temp_id), deepcopy(temp_water)
                        temp_id += 1 
                        continue
                    else: # if height[temp_id] >= LH:
                        lower_side = min(height[temp_id], LH)
                        over_flow = ((temp_id - LHid) - 1) * (LH - lower_side)
                        temp_water -= over_flow
                        _id = deepcopy(temp_id)
                        total_water += temp_water
                        break
                if temp_id == len(height):
                    # attempt to fill to the next highest value
                    print(lower_max_id, _id)
                    if lower_max_id >= _id:
                        lower_side = lower_max
                        over_flow = ((lower_max_id - LHid)) * (LH - lower_side)
                        print(over_flow)
                        if over_flow == 0:
                            # no more water anywhere case, 
                            _id = len(height)
                            break
                        total_water += (lower_max_temp_water - over_flow)

                        # move pointer along
                        _id = deepcopy(lower_max_id)
                    if _id != len(height): LH, LHid = height[_id], _id
            else:
                LH, LHid = height[_id], _id
                _id += 1
        return total_water
    

"""
might not have needed those deepcopies but I wanted to be safe. 
lot of saved variables for a variety of different things. 

Now looking for solutions. 
Looks like double pointer might have been the move from both sides. 
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        left = [0] * n
        right = [0] * n
        
        # Fill left array
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
        
        # Fill right array
        right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        
        # Calculate trapped water
        trappedWater = 0
        for i in range(n):
            trappedWater += min(left[i], right[i]) - height[i]
        
        return trappedWater     
    

"""
Okay i really like that above solution, it makes it super simple, counting from both sides so that 
for any given point, you have the max a given spot can be, then you just subtract the value itself
its floor to find how much water is in it. 
You definetly don't have to store as much data as this guy is going. I doubt you really need 2 
lists for the height list, all you really need is the left highest and the right highest. 
I feel like we were close but the counting up from both sides once again eluded me. 
I remember thinking about it but I dismissed the though too quickly. 
Feel like it was the same thing for the other one that had 2 iterators from both sides. 

Theres one other solution here that doesnt store everything like this one that I want to save
just to show that our thought of holding maxs was good but we didnt take it to the other side
"""

class Solution:
    def sumBackets(self, height: list[int], left, right):

        minHeightLeft = height[left]
        total = 0
        leftBacket = 0
        locationMinLeft = left

        while left < right:
            
            if height[left] < minHeightLeft:
                leftBacket += minHeightLeft - height[left]                
            else:
                minHeightLeft = height[left]
                total +=  leftBacket
                leftBacket = 0
                locationMinLeft = left            
            left += 1
            
        if minHeightLeft <= height[right]:
             return total + leftBacket, right
        else :      
            return total, locationMinLeft

    def sumBacketsReverce(self, height: list[int], left, right):

        minHeightRight = height[right]
        total = 0
        rightBacket = 0
        locationMinRight = right

        while left < right:
            
            if height[right] < minHeightRight:
                rightBacket += minHeightRight - height[right]                
            else :
                minHeightRight = height[right]
                total +=  rightBacket
                rightBacket = 0
                locationMinRight = right            
            right -= 1


        if minHeightRight <= height[left]:
            return total + rightBacket, left
        else :
            return total, locationMinRight
    
    def trap(self, height: List[int]) -> int:                      
        right = len(height)-1
        left =0
        totalSum =0


        while left < right-1:            
            if( height[left]< height[right]):
                total, left = self.sumBackets(height, left, right)    
            else:
                total, right = self.sumBacketsReverce(height, left, right)        
                
            totalSum += total       
             
        return totalSum