"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
"""

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        self.max = maxWidth
        res = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            line_length = 0
            while j < n and line_length + len(words[j]) + (j - i) <= maxWidth:
                line_length += len(words[j])
                j += 1

            is_last_line = j == n
            num_words = j - i
            num_spaces = maxWidth - line_length

            if is_last_line or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                spaces_between_words = num_words - 1
                space, extra = divmod(num_spaces, spaces_between_words)

                line = words[i]
                for k in range(i + 1, j):
                    line += " " * (space + (1 if extra > 0 else 0))
                    extra -= 1
                    line += words[k]

            res.append(line)
            i = j

        return res
