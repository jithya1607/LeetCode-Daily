#28 How many numbers are smaller than the current number
# Given an array of integers, return an array where each element at index i represents the count of numbers smaller than the element at index i.
from ast import List


def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        b=[]
        for i in nums:
            a=0
            for j in nums:
                if i>j:
                    a+=1
            b.append(a)
        return b