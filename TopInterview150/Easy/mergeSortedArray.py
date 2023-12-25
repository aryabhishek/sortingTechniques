"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
 representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Link: https://leetcode.com/problems/merge-sorted-array/
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m - 1
        r = n - 1
        cur = m + n - 1

        # strat merging from the right side
        while l >= 0 and r >= 0:
            if nums1[l] < nums2[r]:
                nums1[cur] = nums2[r]
                r -= 1
            else:
                nums1[cur] = nums1[l]
                l -= 1
            cur -= 1

        # fill the leftover elements of nums2
        while r >= 0:
            nums1[cur] = nums2[r]
            r -= 1
            cur -= 1
