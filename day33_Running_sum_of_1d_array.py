#33 Running sum of 1d array
# Given an array of integers, return an array where each element is the running sum of the elements up to that index.
from typing import List


def runningSum(self, nums: List[int]) -> List[int]:
        a=[]
        b=0
        for i in nums:
            b+=i
            a.append(b)
        return a