#9 Power of three
# Given an integer n, return true if it is a power of three. Otherwise, return false.
def isPowerOfThree(self, n: int) -> bool:
    if n>0:
        a=1
        while a<n:
            a*=3
        if a==n:
            return True
        else:
            return False
    else:
        return False