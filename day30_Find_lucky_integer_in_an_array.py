#30 Find lucky integer in an array
# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
from ast import List


def findLucky(self, arr: List[int]) -> int:
        l=[]
        for i in arr:
            f=0
            for j in arr:
                if i==j:
                    f+=1
            if f==i:
                l.append(i)
        return max(l,default=-1)