# 2018 newcoder链接：https://www.nowcoder.com/questionTerminal/f652bf7904bf4905804fa3bc347fdd2a
# -----------求出点集合P中所有“最大的”点的集合-----------
# 70% 超时 朋友们有可以优化的欢迎提供思路和代码 感谢（撒花～）
# 思路：坐标点先按照x升序排列，那么只需要从后往前比较y值即可
[n] = list(map(int,input().strip().split()))
arr = []
rs = []
for i in range(n):
    arr.append(list(map(int,input().strip().split())))
# print(arr)
# python sort和sorted函数复杂度分析 https://www.cnblogs.com/clement-jiao/p/9243066.html
arr = sorted(arr)
# print(arr)
y_max = 0
for i in range(n-1,-1,-1):
    if not rs:
        rs.append(arr[i])
        y_max = arr[i][1]
    else:
        if arr[i][1] >= y_max:
            rs.append(arr[i])
            y_max = max(y_max,arr[i][1])
rs = sorted(rs)
for i in range(len(rs)):
    print(rs[i][0],end=' ')
    print(rs[i][1])
# ---------- 区间中的最小数 * 区间所有数的和最后程序输出经过计算后的最大值 -------
# 题目链接：https://www.nowcoder.com/questionTerminal/e6e57ef2771541dfa2f1720e50bebc9a
# 用栈，用哨兵，找出最小值，和包含此最小值的最长区间，最小值乘求和更新就可以了
def maxnum(nums):
    stack = []
    maxpro = 0
    for i, num in enumerate(nums):
        while stack and num < nums[stack[-1]]:
            cur = stack.pop()
            maxpro = max(maxpro, nums[cur] * sum(nums[stack[-1] + 1 : i]))
        stack.append(i)
    return maxpro
n = int(input())
nums = [0] + list(map(int, input().split())) + [0]
print(maxnum(nums))

# --------- leetcode 84 柱状图中最大矩阵 ---------
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1] # 初始化给定一个左索引
        rs = 0
        for i,num in enumerate(heights):
            while len(stack) > 1 and heights[i] < heights[stack[-1]]:
                tmp = stack.pop()
                rs = max(rs,heights[tmp]*(i-stack[-1]-1))
            stack.append(i)
        for i in range(len(stack)-1):
            rs = max(rs,heights[stack.pop()]*(len(heights)-stack[-1]-1))
        return rs
