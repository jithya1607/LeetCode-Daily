#24 Subtract the Product and Sum of Digits of an Integer
# Given an integer n, compute the difference between the product of its digits and the sum of its digits.
def subtractProductAndSum(n):
    p=1
    s=0
    while n > 0:
        p*=n%10
        s+=n%10
        n//=10
    return p-s