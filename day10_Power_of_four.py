#10 Power of four
# Given an integer n, return true if it is a power of four. Otherwise, return false.
def isPowerOfFour(self, n: int) -> bool:
    if n<=0:
        return False
    while n%4==0:
        n//=4
    return n==1