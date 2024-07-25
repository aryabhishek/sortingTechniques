"""

"""
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.sort(0, len(nums) - 1, nums)
        return nums

    def merge(self, start, mid, end, nums):
        temp = []
        l = start
        m = mid + 1
        
        while l <= mid and m <= end:
            if nums[l] <= nums[m]:
                temp.append(nums[l])
                l += 1
            else:
                temp.append(nums[m])
                m += 1

        while l <= mid:
            temp.append(nums[l])
            l += 1

        while m <= end:
            temp.append(nums[m])
            m += 1

        for i in range(len(temp)):
            nums[start + i] = temp[i]

    def sort(self, start, end, nums):
        if start < end:
            mid = start + (end - start) // 2
            self.sort(start, mid, nums)
            self.sort(mid + 1, end, nums)
            self.merge(start, mid, end, nums)


if __name__ == "__main__":
    nums = [5,2,3,1]
    print(Solution().sortArray(nums))