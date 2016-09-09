# Q: For two integer arrays, sorted from lowest to highest

# Write a function that takes them as input, returns merged sorted array

# For example:

# array1= [1,4,7,33]
# array2= [2,3,4]
# output= [1,2,3,4,4,7,33]
import pytest


def merge_sorted_arrays(input1, input2):
    output_array = []
    i1 = 0
    i2 = 0
    while i1 < len(input1):
        while i2 < len(input2) and input2[i2] <= input1[i1]:
            output_array.append(input2[i2])
            i2 = i2 + 1
        output_array.append(input1[i1])
        i1 = i1 + 1
    if i2 < len(input2):
        while i2 < len(input2):
            output_array.append(input2[i2])
            i2 += 1
    return output_array


def test_merge_sorted_array():
    array1 = [1, 4, 7, 33]
    array2 = [2, 3, 4]
    result = merge_sorted_arrays(array1, array2)
    print(result)
