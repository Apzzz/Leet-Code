"""
LeetCode link to the problem: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

"""


class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        n = len(s)

        for i in range(n - 1):
            #   count the no of 1s and 0s in each splitting and store the maximum count
            score = max(score, s[: i + 1].count("0") + s[i + 1 :].count("1"))

        return score