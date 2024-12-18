"""
LeetCode link to the problem: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

"""


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = prices.copy()
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    answer[i] = prices[i] - prices[j]
                    break

        return answer
