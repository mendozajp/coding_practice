"""
First thought, iterate through and populate a dictionary with the numbers and their highest count
probably the best way to go about doing that 
The part that gave me pause was actually getting the top k values.
I opted to iterate through the dict k times, adding the highest to the final list and deleting 
the highest one. 
not ideal but gets the job done. 
since we should have been aiming for O(n) this is def not the best way. 
i think we do O(n + klogN) or something along those lines. we aren't splitting up n so log is 
not quite right. Actually del is bascially O(n) so this is pretty bad overall.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_counter = {}
        for number in nums:
            number_counter[number] = number_counter.get(number,0) + 1
        top_k_values = []
        for i in range(k):
            current_max = 0
            key_to_delete = 0
            for key, value in number_counter.items():
                if value > current_max:
                    current_max = value
                    key_to_delete = key
            top_k_values.append(key_to_delete)
            del number_counter[key_to_delete]

        return top_k_values


"""
So their worst solution is better then this one. I havent seen it yet but I was looking at the 
hints

    A naive solution would be to count the frequency of each number and then sort the array 
    based on each element’s frequency. After that, we would select the top k frequent elements.
    This would be an O(nlogn) solution. Though this solution is acceptable, can you think 
    of a better way?

Thats basically what I did, but probably not as well as they got it going on. 
I looked at the next hint and it said to use bucket sort, creating n buckets and 
grouping based on their frequencies from 1-n then get the top k numbers from the buckets.
Basically we want to be grouping numbers based on their frequency so we can just grab the top
k largest. 

Im not sure how seperating it in different buckets is the solution here. But I did it again in 
the way I actually envisioned it, which is just to say, organize them all in a dict, then sort 
and return the range indicated by k. 
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_counter = {}
        for number in nums:
            number_counter[number] = number_counter.get(number,0) + 1
        number_counter = {k: v for k, v in sorted(number_counter.items(), key=lambda item: item[1], reverse=True)}
        return list(number_counter.keys())[0:k]
    
"""
Now lets look at that bucket sort solution.
Their worse solution is conceptually what we were thinking.
It's basically the same. ours is maybe a tad bit more complicated. The poping is probably the worse
part in comparison to ours. 
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
    
"""
Now lets look at the bucket sort solution.
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
"""
Basically just sorting via populating another list via the dicts values as keys.
"""