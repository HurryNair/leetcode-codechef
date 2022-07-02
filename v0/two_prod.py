"""
Given an array of distinct elements and a number x, find if there is a pair with a product equal to x. 
"""

def findtwoprod(array, target):
    
    for i in range(len(array)):
        if target/array[i] in array:
            return [x for x in [i, array.index(target/array[i])]]

if __name__ == "__main__":
    array = [10, 20, 9, 40]
    target = 400

    print(findtwoprod(array, target))