"""
Given two rectangles, find if the given two rectangles overlap or not.
Note that a rectangle can be represented by two coordinates, top left and bottom right. So mainly we are given following four coordinates. 
l1: Top Left coordinate of first rectangle. 
r1: Bottom Right coordinate of first rectangle. 
l2: Top Left coordinate of second rectangle. 
r2: Bottom Right coordinate of second rectangle.
"""

# How many ways in which two rectangles can overlap ?

# Rather, when do we say two rectangles do not overlap?
# - one rectangle is above the other
# - one rectangle is to the right of the other

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

def isOverlapping(l1, r1, l2, r2):
    
    # Ensure neither rectanges are lines

    if (l1.x == r1.x or l1.y ==r1.y or l2.x == r2.x or l2.y == r2.y):
        return False

    if (l1.x >= r2.x or l2.x >= r1.x):
        return False
    
    if (r1.y >= l2.y or r2.y >= l1.y):
        return False
    
    return True

if __name__ == "__main__":
    l1 = Point(0, 10)
    r1 = Point(10, 0)
    l2 = Point(5, 5)
    r2 = Point(15, 0)

    if isOverlapping(l1, r1, l2, r2):
        print("Yes")

    else:
        print("No")

# https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/
# How to check if a given point lies inside or outside a polygon?