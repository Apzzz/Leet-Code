"""
LeetCode link to the problem: https://leetcode.com/problems/most-beautiful-item-for-each-query/

"""


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        items.sort()
        maxBeauty = []
        currMax = 0
        for price, beauty in items:
            currMax = max(currMax,beauty)
            maxBeauty.append((price,currMax)) # Find the max beauty for each price value

        answer = []
        for query in queries:
            # Find the position to insert the next max beauty for a particular price
            idx = bisect_right(maxBeauty,(query, float('inf')))-1
            if idx>=0:
                answer.append(maxBeauty[idx][1]) # If index is found, use the beauty at that index
            else:
                answer.append(0)
        
        return answer
    

    # Optimised time complexity
    class Solution:
        def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
            # Sort the items based on the beauty in descending order
            items.sort(key=lambda x: x[1], reverse=True)
            answer = []
            for query in queries:
                beauty = 0
                for item in items:
                    if item[0] <= query: # The first item with price <= query has the max beauty
                        beauty = item[1]
                        break
                answer.append(beauty)

            return answer