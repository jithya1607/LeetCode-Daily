#7 Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
from ast import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if sorted(nums)==sorted(list(set(nums))):
            return False
        else:
            return True