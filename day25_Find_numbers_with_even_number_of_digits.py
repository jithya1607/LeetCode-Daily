#25 Find numbers with even number of digits
# Given an array of integers, return the count of numbers that have an even number of digits.
def findNumbers(nums):
    count = 0
    for n in nums:
        if len(str(n)) % 2 == 0:
            count += 1
    return count