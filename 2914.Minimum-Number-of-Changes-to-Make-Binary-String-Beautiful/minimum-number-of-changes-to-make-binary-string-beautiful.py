"""
LeetCode link to the problem: https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

"""


class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        #Maximum number of substrings can be made by considering each pair as a substring.
        #Taking the sum of pairs which are not equal gives the number of changes to be made.
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                count += 1

        return count