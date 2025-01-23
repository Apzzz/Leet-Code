"""
LeetCode link to the problem: https://leetcode.com/problems/count-servers-that-communicate/

"""


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row_c = [0] * m
        col_c = [0] * n
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row_c[i] += 1
                    col_c[j] += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if row_c[i] > 1 or col_c[j] > 1:
                        count += 1

        return count



class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        count = 0

        for i in range(m):
            s = sum(grid[i])
            if s > 1:
                count += s
            elif s == 1:
                idx = grid[i].index(1)
                if sum(grid[j][idx] for j in range(m)) > 1:
                    count += 1
        return count
