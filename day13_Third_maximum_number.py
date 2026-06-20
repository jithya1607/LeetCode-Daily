#13 Third Maximum Number
# Given an integer array nums, return the third distinct maximum number in this array.
# If the third maximum does not exist, return the maximum number.
from ast import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num=list(set(nums))
        if len(num)<3:
            return max(num)
        elif len(num)==3:
            return min(num)
        else:
            i=0
            while i<2:
                num.remove(max(num))
                i+=1
            return max(num)