"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

https://leetcode.com/problems/reverse-vowels-of-a-string
"""

from collections import deque


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        dq = deque([char for char in s if char in vowels])
        output = []
        for char in s:
            if char in vowels:
                output.append(dq.pop())
            else:
                output.append(char)

        return "".join(output)
