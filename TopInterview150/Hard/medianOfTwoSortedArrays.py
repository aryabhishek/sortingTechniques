"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        low = 0  # take 0 elements from nums1
        high = m  # take all the elements
        minn = float("-inf")
        maxx = float("inf")

        while low <= high:
            px = low + (high - low) // 2
            py = (m + n + 1) // 2 - px

            x1 = minn if px == 0 else nums1[px - 1]
            x2 = minn if py == 0 else nums2[py - 1]
            x3 = maxx if px == m else nums1[px]
            x4 = maxx if py == n else nums2[py]

            if x1 <= x4 and x2 <= x3:
                if (m + n) % 2 == 1:
                    return max(x1, x2)  # greatest of the left partiton
                return (max(x1, x2) + min(x3, x4)) / 2
            elif x1 > x4:
                high = px - 1
            else:
                low = px + 1

        return -1


if __name__ == "__main__":
    s = Solution()
    nums1 = [1,2]
    nums2 = [3,4]
    print(s.findMedianSortedArrays([0, 0], [0, 0]))