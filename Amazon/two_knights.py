"""
For k in range(n), task is to count the number of ways to place 2 knights on a kxk chessboard so that they dont attack each other
"""

# Essentially a selection problem with 
# some restrictions

# I can compute total number of seats to be k*k
# From this n seats, I can select 2 seats with n*(n-1)/2

def computeKnightPlacements(n):

    for k in range(1, n+1):
        total_seats = k*k
        two_seats_from_n = total_seats*(total_seats-1)/2

        # for k = 1 & k = 2, knights cannot move
        if k > 2: # while k is 3 or greater we would have 9 seats total
            two_seats_from_n = two_seats_from_n - (4*(k-1)*(k-2))
        
        print(int(two_seats_from_n))


if __name__ == "__main__":
    n = int(input())
    print(computeKnightPlacements(n))
