'''
Given an array of integers, find the nearest smaller number for every element such that the smaller element is on left side.
'''

def prevSmaller(array, size):

    prevSmallernum = ['_']

    for i in range(1, size):
        for j in reversed(range(i)):
            if array[j] < array[i]:
                prevSmallernum.append(array[j])
                break
        else:
            prevSmallernum.append("_")
    
    return prevSmallernum

if __name__ == "__main__":

    array = [1, 3, 0, 2, 5]

    print(prevSmaller(array, len(array)))