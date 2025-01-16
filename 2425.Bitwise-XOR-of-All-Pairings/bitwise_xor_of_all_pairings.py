"""
LeetCode link to the problem: https://leetcode.com/problems/bitwise-xor-of-all-pairings/

"""


class Solution:
    #   If the length of nums1 is m and the length of nums2 is n, then each number in nums1 is repeated n times and each number in nums2 is repeated m times.4
    #   XOR with itself results in 0: a ^ a = 0, XOR with 0 results in the same number: a ^ 0 = a
    #   Hence only if the length of the array is an odd number, the result has to be calculated
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)
        result = 0

        if len2 % 2:
            for no in nums1:
                result ^= no
        if len1 % 2:
            for no in nums2:
                result ^= no

        return result
