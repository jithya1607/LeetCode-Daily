#11 Intersection of Two Arrays
# Given two arrays, write a function to compute their intersection.
from ast import List

def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    a=[]
    for i in range(min(len(nums1),len(nums2))):
        if len(nums1)<len(nums2):
            if nums1[i] in nums2:
                a.append(nums1[i])
        else:
            if nums2[i] in nums1:
                a.append(nums2[i])
    return list(set(a))