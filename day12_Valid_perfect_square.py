#12 Valid perfect square
# Given a positive integer n, determine if it is a perfect square.
def isPerfectSquare(self, num: int) -> bool:
    if num<0:
        return False
    i=0
    while i**2<num:
        i+=1
    return i**2==num