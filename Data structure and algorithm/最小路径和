# dp 时间复杂度o(mn) 空间复杂度o(mn)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:return False
        # m,n 行 列
        m,n=len(grid),len(grid[0])
        dp=[[0]*n for _ in range(m)]
        if m == 1 and n == 1:
            return grid[0][0]
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
# dp 优化 时间复杂度o(mn) 空间复杂度o(n)
# 参考：https://leetcode-cn.com/problems/minimum-path-sum/solution/zui-xiao-lu-jing-he-by-leetcode-solution/
class Solution:
    def minPathSum(self, grid):
        dp = [float('inf')] * (len(grid[0])+1)
        dp[1] = 0
        for row in grid:
            for idx, num in enumerate(row):
                dp[idx + 1] = min(dp[idx], dp[idx + 1]) + num
        return dp[-1]
# dp 优化 原地修改 时间复杂度o(mn) 空间复杂度o(1)
# 参考：https://leetcode-cn.com/problems/minimum-path-sum/solution/zui-xiao-lu-jing-he-dong-tai-gui-hua-gui-fan-liu-c/
class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        if not grid:return False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]
