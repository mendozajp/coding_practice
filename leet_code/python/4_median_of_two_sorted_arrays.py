"""
Not much to say about this one. It was ranked hard but its really only hard if you have no idea how to find
the median of a list. If you do then its kind of trivial. Just combine the lists, sort them again 
and get the middle values, do the little math we learned in middle school and return that. 

It did take me a second to get there I guess, but it is a very easy problem. 
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        temp = sorted(nums1 + nums2)
        length = len(temp)
        if length == 1:
            return temp[0]
        if length % 2 == 0: # is even
            return  (temp[((length // 2))] + temp[(length // 2)-1]) / 2.0
        else:
            return temp[length//2]

"""
Looking at other solutions, interestingly enough, this is the brute force solution. Which is crazy
cause its apparently the fastest there is. Probably in the sub ms level which is meaningless for 
this. 

So sorted is O(nlogn)
most of these binary search solutions seem to claim O(log(n+m)) which would be ideal, but theres a lot 
of deliberations over which is better when I feel like its to close to matter. IDK maybe we should
be thinking of millions and millions of values. Maybe a sorted is not gonna cut it like that. 
I cant imagine looping over the whole thing is gonna be much better though. 

It might be that cpp just doesnt have good built in sorting. I don't really remember. 
But I guess the real challenge is getting O(log(n+m))
Actually, just thinking about how O(log(n)) works, I guess they are directly saying you should
just add the lists and then divide and conquer. Regardless I think your good. 
"""