"""
https://neetcode.io/problems/buy-and-sell-crypto?list=blind75
I had to step out so in the car had a lot of time to think about this one. I'm happy to say the
idea I came up with ended up working. 
Mainly the thinking was, the order is critical, at any given point, if you knew the highest value
to the right of that value, then you would only need to calculate everything once and you'd be
done, so could we have that info prior to a full iteration? Well if you iterate backwards and
find the right highest for each index then you sure can, worked right away. 
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right_most_profitable = []
        j = len(prices) - 1
        previous_max = -1
        while j >= 0:
            if len(right_most_profitable) == 0:
                right_most_profitable.append(-1)
                previous_max = prices[j]
                j -= 1
                continue
            if prices[j] > previous_max:
                right_most_profitable.append(prices[j])
                previous_max = prices[j]
            else:
                right_most_profitable.append(previous_max)
            j -= 1
        right_most_profitable.reverse()
        highest_observed_profit = 0
        for i, value in enumerate(prices):
            highest_observed_profit = max(highest_observed_profit, (right_most_profitable[i] - value))
        return highest_observed_profit
    
"""
Plenty of minor inaccuracies here, reversing the string at the end, probably would have been faster
to initialize a fully populated list of 0s [0]*len(prices) and edit those since those are mutable.
beyond that I think this is pretty good. about O(2N) I would guess.

Looked at the solution, ho boy, O(n) without issue. Check this out
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0                                        # max profit, right away, we do it after setting up the key
        minBuy = prices[0]                              # just a min waiting to update when it sees something smaller. Makes sense.

        for sell in prices:                             # right into the only loop from that
            maxP = max(maxP, sell - minBuy)             # so we check if the current "best" buy price's profit, if its better we save
            minBuy = min(minBuy, sell)                  # now we check if there is a better buy price, so if there was a better deal before now, even if it cost more, we would have seen it already.
        return maxP
    
"""
Alright thats pretty clean. This was labled as Dynamic programming. And I suppose this makes more
sense as a sliding window then whatever I had going on up there. 
"""