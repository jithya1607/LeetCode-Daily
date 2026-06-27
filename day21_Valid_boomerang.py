#21 Valid Boomerang
# Given three points in the plane, determine if they form a valid boomerang (i.e., they are not collinear and not identical).
def isBoomerang(points):
    a=points[0][0]*(points[1][1]-points[2][1])
    b=points[0][1]*(points[1][0]-points[2][0])
    c=(points[1][0]*points[2][1])-(points[2][0]*points[1][1])
    return (a-b+c)!=0