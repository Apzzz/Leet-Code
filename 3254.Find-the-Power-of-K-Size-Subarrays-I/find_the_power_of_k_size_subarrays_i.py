"""
LeetCode link to the problem: https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

"""

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1] * (n - k + 1)

        for i in range(n - k + 1):
            j = i
            while j < i + k - 1:    #   check if all the elements of len k are consecutive
                if nums[j] + 1 == nums[j + 1]:
                    j += 1
                else:
                    break
            if j == i + k - 1:
                result[i] = max(nums[i : i + k])    #   if they are, add the max value to the result

        return result
