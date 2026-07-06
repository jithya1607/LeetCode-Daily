#29 Create target array in the given order
#Given two arrays of integers nums and index. Your task is to create target array such that target[i] is the value nums[i] inserted at index index[i] in target array. You should return the target array.

def createTargetArray(nums, index):
    target = []
    for i in range(len(nums)):
        target.insert(index[i], nums[i])
    return target