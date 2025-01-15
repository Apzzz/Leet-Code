"""
LeetCode link to the problem: https://leetcode.com/problems/minimize-xor/

"""


class Solution:
    def isSet(self, num: int, i: int) -> bool:
        #   Formula to check if a bit is set or not
        return ((1 << i) & num) != 0

    def setBit(self, num: int, i: int) -> int:
        #   Formula to set a bit
        return (1 << i) | num

    def unsetBit(self, num: int, i: int) -> int:
        #   Formula to unset a bit
        return ~(1 << i) & num

    def minimizeXor(self, num1: int, num2: int) -> int:

        result = num1
        targetSetBits = bin(num2).count("1")
        setBits = bin(result).count("1")

        curBit = 0

        #   if the number of bits in num2 is greater set the bits of num1 starting from the least significant bit so that the xor doesn't affect much
        while targetSetBits > setBits:
            if not self.isSet(result, curBit):
                result = self.setBit(result, curBit)
                setBits += 1
            curBit += 1

        #   if the number of bits in num1 is greater unset the bits from num1 starting from the least significant bit
        while targetSetBits < setBits:
            if self.isSet(result, curBit):
                result = self.unsetBit(result, curBit)
                setBits -= 1
            curBit += 1

        return result