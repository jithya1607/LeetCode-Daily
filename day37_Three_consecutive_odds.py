#37 Three consecutive odds
# Return True if the array contains three consecutive odd numbers. Otherwise, return False.
from ast import List


def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        try:
            for i in range(len(arr)):
                if arr[i]%2==1 and arr[i+1]%2==1 and arr[i+2]%2==1:
                    return True
        except:
            pass
        return False