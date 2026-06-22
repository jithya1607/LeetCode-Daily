# Max Consecutive Ones
# Given a binary array, find the maximum number of consecutive 1s in this array.
from ast import List


def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    a=0
    b=[]
    for i in range(len(nums)):
        if nums[i]==1:
            a+=1
        else:
            b.append(a)
            a=0
    b.append(a)
    return max(b)