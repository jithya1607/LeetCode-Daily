#45 Find the highest altitude
#Given a list gain, of integers representing altitude changes, return the highest altitude reached.
def largestAltitude(gain):
    c=0
    altitude=[0]
    for i in gain:
        altitude.append(altitude[-1]+i)
    return max(altitude)