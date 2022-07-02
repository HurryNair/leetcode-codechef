# Given coordinates of four points in a plane, find if the four points form a square or not. 
# To check for square, we need to check for following. 
# a) All fours sides formed by points are the same. 
# b) The angle between any two sides is 90 degree. (This condition is required as Quadrilateral also has same sides. 
# c) Check both the diagonals have the same distance

# All fours sides formed by points are the same.
# Find which pairs of coordinates form sides
# Find difference between the x2,x1 & y2,y1 of these pairs
# These differences must match amongst all four pairs representing all four sides

# Seasoned approach

# Pick a point p
# Distance of this point from 2 of the 3 other points must be equal. Call this distance d & the points a & b 
# Distance of p from the 3rd point must be 1.432 times d. Call this third point q
# Distance from a & b to p must be equal to d 

# So by ensuring that the diag is edge*root(2) we are ensuring that the angle between the edges is 90 degrees


# structure of a point in 2D space

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

# utility function to calculate distance
# between two points

def distance(p, q):

    # distance formula - (x1 - x2)^2 + (y1 - y2)^2
    d = ((p.x - q.x) * (p.x - q.x)) + ((p.y - q.y) * (p.y - q.y))

    return d

def isSquare(p1, p2, p3, p4):

    # calculate distance from p1 to p2, p3 & p4

    d2 = distance(p1, p2)
    d3 = distance(p1, p3)
    d4 = distance(p1, p4)

    # No two points in a sq can have the same 2D coordinates

    if d2 == 0 or d3 == 0 or d4 == 0:
        return False
    
    if d2 == d3 and d4 == 2*d2 and 2*(distance(p2,p4)) == distance(p2,p3):
        return True
    
    if d3 == d4 and d2 == 2*d3 and 2*(distance(p3,p2)) == distance(p3,p4):
        return True

    if d2 == d4 and d3 == 2*d2 and 2*(distance(p2,p3)) == distance(p2,p4):
        return True

    return False

# Driver Code
if __name__=="__main__":
    p1 = Point(20, 10)
    p2 = Point(10, 20)
    p3 = Point(20, 20)
    p4 = Point(10, 10)
     
    if isSquare(p1, p2, p3, p4):
        print('Yes')
    else:
        print('No')
    





