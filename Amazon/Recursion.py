'''
The idea of recursion is to make the input smaller
Role of recursion in decision space
How to design a recursive tree

"""

"""
Factorial using recursion
'''

def factorial(n):

    return 1 if (n == 1 or n ==0) else n*factorial(n-1)

if __name__ == "__main__":
    print(factorial(4))
