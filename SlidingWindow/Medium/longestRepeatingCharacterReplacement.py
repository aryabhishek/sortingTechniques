"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        i = j = 0
        alpha = [0] * 26
        max_diff = ans = 0

        while j < n:
            idx = ord(s[j]) - 65
            alpha[idx] += 1
            max_diff = max(max_diff, alpha[idx])

            if j - i + 1 - max_diff > k:
                alpha[ord(s[i]) - 65] -= 1
                max_diff = 0
                i += 1

            if j - i + 1 - max_diff <= k:
                ans = max(ans, j - i + 1)

            j += 1

        return ans


if __name__ == "__main__":
    solution = Solution()
    s = "ABAB"
    k = 2
    print(solution.characterReplacement(s, k))
