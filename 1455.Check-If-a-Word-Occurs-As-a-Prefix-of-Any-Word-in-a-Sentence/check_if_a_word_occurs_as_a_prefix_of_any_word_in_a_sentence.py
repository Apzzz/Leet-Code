"""
LeetCode link to the problem: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        if searchWord in sentence:
            for i, word in enumerate(sentence.split()):
                if word.startswith(searchWord):
                    return i + 1
        return -1
