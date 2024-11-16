"""
LeetCode link to the problem: https://leetcode.com/problems/longest-increasing-subsequence/

"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []

        for n in nums:
            idx = bisect_left(lis, n)
            if idx == len(lis):  
                lis.append(n)
            else:
                lis[idx] = n
        return len(lis)
