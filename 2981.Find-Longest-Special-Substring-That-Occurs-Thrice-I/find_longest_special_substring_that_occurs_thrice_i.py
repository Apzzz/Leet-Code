"""
LeetCode link to the problem: https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

"""


class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        if len(set(s)) == n:
            return -1

        substr = {} #   To store all substrings and their count
        for i in range(n):
            string = ""
            for j in range(i, n):
                #   Add each char to the substring only if it's the same
                if not string or s[j] == string[-1]:
                    string += s[j]
                    if string in substr:
                        substr[string] += 1
                    else:
                        substr[string] = 1
                else:
                    break
        ans = -1
        for string, count in substr.items():
            if count >= 3 and len(string) > ans:
                #   Find the length of the longest substring with count >= 3
                ans = len(string)
                print(string, count)

        return ans
