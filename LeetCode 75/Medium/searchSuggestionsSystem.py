"""
You are given an array of strings products and a string searchWord.
Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
Return a list of lists of the suggested products after each character of searchWord is typed.

https://leetcode.com/problems/search-suggestions-system/
"""

from typing import List


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        res = []
        products.sort()
        n = len(products)
        l, r = 0, n - 1

        for i in range(len(searchWord)):
            char = searchWord[i]

            while l <= r and (len(products[l]) <= i or products[l][i] != char):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != char):
                r -= 1

            temp = []
            for j in range(l, min(l + 3, r + 1)):
                temp.append(products[j])
            res.append(temp)

        return res


if __name__ == "__main__":
    sol = Solution()
    products = [
        "havana",
    ]
    searchWord = "havana"
    print(sol.suggestedProducts(products, searchWord))
