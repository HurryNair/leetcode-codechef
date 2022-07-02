"""
Task is to place eight queens on a chessboard in such a way that no two queens attach each other
As an additional challenge, each square is either occupied or free
Queens can only be placed on free squares
Occupied squares do not prevent the queen from attacking each other

How many possible ways to place the queens ?


Input will have eight lines, each with eight characters
'.' representing an empty square & '*' representing a reserved square
"""

from itertools import permutations

# utility function to calculate all permutations of a string
def allPermutations(p):

    return list(permutations(p))

def place_queens(s):

    p = [x for x in range(8)] # pointers for each square in the rows
    ans = 0

    for p in allPermutations(p):

        # we iterate through all permutations of [0...7]

        # Assume this perm will be a solution
        # Set it to True
        # We then evaluate cases where it could be False
        ok = 1

        for i in range(8):
            # ensuring here that every position 
            # chosen on the board in this iteration is empty

            # If yes ok remains 1
            # Else it would be 0

            ok &= s[i][p[i]] == '.'
        
        # s[i] - picks a different row each iteration
        # p[i] - picks a different columm in the new row
        # this way no two queens are placed in same row or same column
        # now we just need to handle the permutations where queens would be placed diagonally
        
        # perms where diags are all empty can be added to answer

        # consider points [0,7] & [1,6] on the chessboard
        # These are diagonally aligned
        # 0 + 7 == 1 + 6

        # Consider points 
        b = [0] * 15 # 8 + 8 diag cells - 1 common cell

        for i in range(8): # all diagonal positions like 1,4 & 2,3 || 0,7 & 1,6 will have the same sum
            if b[i+p[i]]: # If a diag position has been used to place a queen
                ok = 0
            b[i+p[i]] = 1 # Mark space on b that a queen is placed here
        
        b = [0] * 15 # 8 + 8 diag cells - 1 common cell # second direction

        for i in range(8): # testing diagonals in the other direction
            if b[i+7-p[i]]:
                ok = 0
            b[i+7-p[i]] = 1

        ans += ok
    
    return ans

if __name__ == "__main__":

    # list to hold eight input strings
    s = ["........", "........", "..*.....", "........", "........", ".....**.", "...*....", "........"]
    
    print(place_queens(s))