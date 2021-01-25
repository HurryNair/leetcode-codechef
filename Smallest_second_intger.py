#Filename : Smallest_second_intger.py
#! /usr/bin/python3

# Program to find the second smallest integer
# in a given array of integers

import sys

def print_second_smallest(arr):

    arr_size = len(arr)

    #Array must have two numbers minimum
    if arr_size < 2:
        print("invalid input")

    else:
        first = second = sys.maxint
        #first > smallest
        #second > second smallest
        
        #so when we find a number
        #smaller than first, what was
        #in first will automatically
        #go to second and first is updated

        #numbers larger than first
        #but smaller than second
        #need to be looked out for

        
        for i in range(0, arr_size):
            if arr[i] < first:
                second = first
                first = arr[i]
            elif arr[i] < second and arr[i] != first:
                second = arr[i]

        #we also need to look out for
        #inputs with identical inputs
        
        if second == sys.maxint:
            return("No second smallest element")

        else:
            return(second)
                
                
                
                
            
