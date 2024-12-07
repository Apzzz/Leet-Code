"""
LeetCode link to the problem: https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

"""


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        #   Determine the number of operations to distribute the balls such that no bag contains more than maxBallsinBag balls
        def maxOperation(maxBallsinBag: int) -> int:
            return sum([(no - 1) // maxBallsinBag for no in nums])

        left, right = 1, max(nums)

        #   Perform binary search
        while left < right:
            mid = (left + right) // 2

            #   at most maxOperations operations is allowed
            if maxOperation(mid) <= maxOperations:
                right = mid
            else:
                left = mid + 1

        return left
