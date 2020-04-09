#!python

"""
ANNOTATE FUNCTIONS WITH TIME AND SPACE COMPLEXITY!!!!!

"""




def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""

    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    """Time complexity: O(n) because you iterate through n amount of items in array
        Space Complexity: O(n) because there are n amount of items"""
    # loop over all array values until item is found
    for index, value in enumerate(array): #O(n)
        if item == value:               #O(1)
            return index  # found       O(1)
    return None  # not found            O(1)


def linear_search_recursive(array, item, index=0):
    """Time complexity: O(n) because you are returning the function continuously until index equals to nth-item
    """

    if len(array) <= index:
        return index

    if array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""

    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    """Time Complexity: O(log*n) because you are constantly dividing the length of array by 2 until array length is 1
        Space Complexity: O(1) """
    left, right = 0, len(array) - 1

    if len(array) == 0:
        return None

    while left <=  right:
        middle = left + (right - left) // 2

        if item == array[middle]:
            return middle

        elif item > array[middle]:
            left = middle + 1
        else:
            right = middle - 1
            
    return None


def binary_search_recursive(array, item, left=None, right=None):
    """Time Complexity: O(log*n)
        Space Complexity: 0(log*n) recursion call stack space"""
    # TODO: implement binary search recursively here
    if left is None and right is None:
        left, right = 0, len(array) - 1

    middle = left + (right - left) // 2

    if left > right:
        return None

    if array[middle] == item:
        return middle
    elif item > array[middle]:
        return binary_search_recursive(array, item, middle + 1, right)
    else:
        return binary_search_recursive(array, item, left, middle - 1)


