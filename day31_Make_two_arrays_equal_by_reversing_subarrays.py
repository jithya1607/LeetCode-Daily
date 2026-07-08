#31 Make two arrays equal by reversing subarrays
def canMakeEqual(target, arr):
    return sorted(target) == sorted(arr)