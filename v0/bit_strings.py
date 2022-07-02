"""
Task is to calculate the number of bitstrings of length n

For example if n = 3, the correct answer is 8 because the possible bitstrings are 001, 001, 010, 011, 100, 101, 110 & 111
"""

def bitstrings(n):
    return 2**n

if __name__ == "__main__":
    print(bitstrings(3))