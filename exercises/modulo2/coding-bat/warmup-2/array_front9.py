"""
http://codingbat.com/prob/p110166

Given an array of ints, return True if one of the first 4 elements in the array is a 9.
The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
"""

def array_front9(nums):
    return 9 in nums[:4]


if __name__ == '__main__':
    assert array_front9([1, 2, 9, 3, 4])
    assert array_front9([9, 3, 5, 7, 5])
    assert array_front9([1, 9, 5])
    assert not array_front9([1, 2, 3, 4, 9])
    assert not array_front9([1, 2, 3, 4, 5])
    assert not array_front9([])
    print('fim')