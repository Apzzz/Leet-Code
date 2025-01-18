"""
LeetCode link to the problem: https://leetcode.com/problems/neighboring-bitwise-xor/

"""


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        #   The sum of the elements gives the total count of 1s in the array. 
        #   If the sum is even, it means that the mismatches can be paired and resolved, allowing us to construct a valid original array
        return sum(derived) % 2 == 0




class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        #   Each element in original appears exactly twice in the equations: once as original[i] and once as original[i+1]
        #   If the derived array is valid, then the XOR of all elements in derived must be 0. This is because all elements of original cancel out when XORed
        xorSum = 0

        for bin in derived:
            xorSum ^= bin
        
        return xorSum == 0