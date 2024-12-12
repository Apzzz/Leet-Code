"""
LeetCode link to the problem: https://leetcode.com/problems/take-gifts-from-the-richest-pile/

"""

import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        for i in range(k):
            #   Always take the largest element in the array
            idx = gifts.index(max(gifts))
            gifts[idx] = math.floor(gifts[idx] ** 0.5)

        return sum(gifts)


#   Solution using heap
import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapq.heapify(heap)

        while k:
            largest = -heapq.heappop(heap)
            largest = math.floor(largest**0.5)
            heapq.heappush(heap, -largest)
            k -= 1

        return -1 * sum(heap)
