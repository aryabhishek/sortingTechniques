"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""

from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        word_count = len(words)
        total_length = word_length * word_count

        word_map = {}
        for word in words:
            if word in word_map:
                word_map[word] += 1
            else:
                word_map[word] = 1

        res = []

        for i in range(word_length):
            left = i
            right = i
            current_count = 0
            cur_map = {}

            while right + word_length <= len(s):
                word = s[right : right + word_length]
                right += word_length

                if word in word_map:
                    if word in cur_map:
                        cur_map[word] += 1
                    else:
                        cur_map[word] = 1

                    current_count += 1

                    while cur_map[word] > word_map[word]:
                        left_word = s[left : left + word_length]
                        cur_map[left_word] -= 1
                        current_count -= 1
                        left += word_length

                    if current_count == word_count:
                        res.append(left)
                else:
                    cur_map.clear()
                    current_count = 0
                    left = right

        return res
