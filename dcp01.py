#! /usr/bin/python

""" 
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given[10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""

import sys

def hasSum (arr, sum):
    i = 0
    j = len(arr) - 1
    success = False

    arr.sort()

    while i < j:
        check = arr[i] + arr[j]
        if check == sum:
            success = True
            break
        elif check < sum:
            i = i + 1
        elif check > sum:
            j = j - 1
    
    return success


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('pass in the sum you want to compute')
        exit()
        
    arr = [10, 15, 3, 7]
    k = int(sys.argv[1])
    print(hasSum(arr, k))
