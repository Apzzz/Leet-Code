"""
LeetCode link to the problem: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

"""

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        string = "0"
        if k > 1:
            for _ in range(n):
                inv = string.translate(str.maketrans("01", "10")) # invert 0s and 1s in the string
                string += "1"+inv[::-1] #   append the reverse of inverted string with 1 to the initial string
                if k < len(string):
                    return string[k-1]
        return string
