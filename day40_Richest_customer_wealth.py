#40 Richest customer wealth
#Return the wealth of the richest customer in the given list of customers' wealth.
def maximumWealth(accounts):
    a=[]
    for i in accounts:
        a.append(sum(i))
    return max(a)