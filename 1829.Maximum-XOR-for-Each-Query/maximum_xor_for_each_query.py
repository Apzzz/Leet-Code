"""
LeetCode link to the problem: https://leetcode.com/problems/maximum-xor-for-each-query/

"""


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        maxBit = (2**maximumBit) - 1 # The maximum possible XOR result is always 2^(maximumBit) - 1
        answer = [0] * n
        xorValue = nums[0]
        answer[0] = xorValue ^ maxBit

        # Instead of deleting an element from the list everytime run the loop in forward and calculate the xor till that value
        for i in range(1, n):
            xorValue ^= nums[i]
            answer[i] = xorValue ^ maxBit # The answer for a prefix is the XOR of that prefix XORed with 2^(maximumBit)-1

        return answer[::-1]
