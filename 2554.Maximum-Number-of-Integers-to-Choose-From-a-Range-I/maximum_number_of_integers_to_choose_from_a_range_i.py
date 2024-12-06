"""
LeetCode link to the problem: https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

"""


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count = 0
        bannedNumbersinRange = set(banned)

        for i in range(1, n + 1):
            if maxSum == 0 or maxSum - i < 0:
                break
            if i not in bannedNumbersinRange:
                count += 1
                maxSum -= i
        return count
