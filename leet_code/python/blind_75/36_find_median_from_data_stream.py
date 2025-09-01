"""
https://neetcode.io/problems/find-median-in-a-data-stream?list=blind75
First read this, was super confused why it was a hard, finished it in like 10 minutes
passed all cases. Put it into LC instead, cause NC doesnt give you the preformance graph
Literally the last percential, only beats 5.05% of submissions.
Makes sense. No way it was gonna be this simple.
"""


class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        if len(self.arr) % 2 == 0:
            # even, need to provide new number
            return (
                self.arr[(len(self.arr) // 2)] + self.arr[((len(self.arr) // 2) - 1)]
            ) / 2
        else:
            return self.arr[len(self.arr) // 2]


"""
Based on the TC requested, You're gonna have to read up on Heaps to figure this one out for sure. 
I'll upload this for now but you should come back and solve this later after a primer with heaps.
"""
