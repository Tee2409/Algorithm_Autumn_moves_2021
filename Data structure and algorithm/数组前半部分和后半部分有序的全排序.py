# coding: utf-8
"""Ordered total ordering of the first and second half of an array (Spatial complexity O(1))
time : 2021/07/21
author : Jessy
"""
def mergesort(nums,p):
    """nums[:p-1] and nums[p:] are sorted
    """
    n = len(nums)
    left,right = 0,p
    while left < right and right < n:
        while nums[left] < nums[right]:
            left += 1
        tmp = nums[right]
        for i in range(right,left,-1):
            nums[i] = nums[i-1]
        nums[left] = tmp
        left += 1
        right += 1
    return nums
# sample
v=[1,3,5,7,9,3,6,8,10]
mergesort(v,5)
