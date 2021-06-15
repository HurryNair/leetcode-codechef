"""
A number spiral is an infinite grid with its upper-left cell with value 1

Solution is to find the value stored in the row x and column y of this grid
"""

def findValue(y, x):

    z = max(y, x)

    z2 = (z-1)*(z-1)
    ans = 0

    if z%2 == 0:
        if y == z:
            ans = z2 + x
        else:
            ans = z2 + 2*z - y
    else:
        if x == z:
            ans = z2 + y
        else:
            ans = z2 + 2*z - x
    
    return ans

if __name__ == "__main__":
    t = int(input("Input t: "))
    print(t)
    while t:
        x = int(input("Input column: ")) # column
        y = int(input("Input row: ")) # row

        print(findValue(y, x))

        t -= 1



        



    

