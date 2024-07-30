"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

https://leetcode.com/problems/reverse-words-in-a-string/
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        sentence = list(s)[::-1]
        i = l = r = 0
        n = len(sentence)

        while i < n:
            while i < n and sentence[i] != " ":
                sentence[r] = sentence[i]
                i += 1
                r += 1

            if l < r:
                self.reverse(l, r - 1, sentence)
                if r < n:
                    sentence[r] = " "
                r += 1
                l = r
            i += 1

        return "".join(sentence[: r - 1])

    def reverse(self, l, r, lst):
        while l < r:
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1


class OneLiner:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("The Sky is blue"))
