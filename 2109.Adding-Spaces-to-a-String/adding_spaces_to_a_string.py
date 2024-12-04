"""
LeetCode link to the problem: https://leetcode.com/problems/adding-spaces-to-a-string/

"""


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        modifiedString = ""
        j = 0
        for idx, ch in enumerate(s):
            if j < len(spaces) and idx == spaces[j]:
                modifiedString += " "
                j += 1
            modifiedString += ch
        return modifiedString



# Optimized time complexityclass Solution:
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        modifiedString = ""
        j = 0
        for idx, ch in enumerate(s):
            if j < len(spaces) and idx == spaces[j]:
                modifiedString += " "
                j += 1
            modifiedString += ch
        return modifiedString