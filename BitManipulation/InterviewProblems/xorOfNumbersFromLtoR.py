"""
You are given two integers L and R, your task is to find the XOR of elements of the range [L, R].

Example:

Input: 
L = 4, R = 8 
Output:
8 
Explanation:
4 ^ 5 ^ 6 ^ 7 ^ 8 = 8
Your Task:

Your task is to complete the function findXOR() which takes two integers l and r and returns the XOR of numbers from l to r.

Expected Time Complexity: O(1).

Expected Auxiliary Space: O(1).

Constraints:

1<=l<=r<=109
"""


class Solution:
    def findXOR(self, l, r):
        # Code here
        def get_xor(num):
            if num % 4 == 1:
                return 1
            elif num % 4 == 2:
                return num + 1
            elif num % 4 == 3:
                return 0
            else:
                return num

        return get_xor(l - 1) ^ get_xor(r)
