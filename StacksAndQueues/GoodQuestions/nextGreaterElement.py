from collections import deque


class Solution:
    def nextLargerElement(self, arr, n):
        # code here
        stk = deque()
        ans = []

        for i in range(n - 1, -1, -1):
            ele = arr[i]

            if not stk:
                ans.append(-1)

            elif stk and stk[-1] > ele:
                ans.append(stk[-1])

            elif stk and stk[-1] <= ele:
                while stk and stk[-1] <= ele:
                    stk.pop()
                if stk:
                    ans.append(stk[-1])
                else:
                    ans.append(-1)
            stk.append(ele)

        ans.reverse()

        return ans
