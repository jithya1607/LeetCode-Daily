#22 Height checker
#Return the number of indices where heights[i] != expected[i]
def heightChecker(heights):
    expected = sorted(heights)
    a = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            a += 1
    return a