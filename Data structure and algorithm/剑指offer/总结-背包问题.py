# 背包问题是一个经典且面试笔试经常考查的知识点，加上不同的限制和条件可以衍生出多种类型题目，本文给出背包问题的几种情况和对应的题目示例，参考资料放于最后。
# 题目均为python3实现
# 包含以下9个分类：
"""
-- （1）01背包问题
-- （2）完全背包问题
-- （3）多重背包问题
-- （4）混合背包问题
-- （5）二维费用背包问题
-- （6）分组背包问题
-- （7）背包问题求方案数
-- （8）求背包问题的方案
-- （9）有依赖的背包问题
"""

# ----------01背包问题-----------
# 问题描述：有N件物品和一个容量为V的背包。第i件物品的体积是v[i]，价值是w[i]。求解不超过背包容量的前提下，将哪些物品装入背包可使价值总和最大。
# 约束条件：每种物品数量为 1，可以选择放或不放。
# 状态定义：dp[i][j]表示只看前i个物品，当前容量是j的情况下，总价值最大是多少。
# 状态转移：
# --第i个物品不选择，dp[i][j]和i-1个物品放入容量j的总价值最大情况相同，即dp[i][j]=dp[i-1][j]；
# --第i个物品选择，那么i-1个物品需存放在j-v[i]容量约束下，dp[i][j]=dp[i-1][j-v[i]]+w[i]。
# 状态转移公式：dp[i][j] = max(dp[i-1][j],dp[i-1][j-v[i]]+w[i])
# code
"""# input
N,V = map(int, input().strip().split())
goods = []
for i in range(N):
    # goods[i]=[v[i],w[i]]
    goods.append([int(j) for j in input().strip().split()])
"""
# function
def bag_01(N,V,goods):
    # 二维dp 时间空间复杂度O(nv)
    # 初始化为0 注意边界
    dp = [[0 for _ in range(V+1)] for _ in range(N+1)]
    # 
    for i in range(1,N+1):
        for j in range(1,V+1):
            if j < goods[i-1][0]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-goods[i-1][0]]+goods[i-1][1])
    return dp[-1][-1]

if __name__ == '__main__':
    result = bag_01(4,50,[[0,0],[10,60],[20,100],[30,120]])
    print(result)
    result = bag_01(1,5,[[10,60]])
    print(result)
# 优化 可以看出上述状态转移公式只与前一个状态有关
# 只使用一维数组来实现，这样可使空间复杂度降到 O(V)
def bag_01(N,V,goods):
    # 维数组来实现，这样可使空间复杂度降到 O(V) 时间空间复杂度仍为O(nv)
    dp = [0 for i in range(V+1)]
    for i in range(N):
        for j in range(V,-1,-1): # 从后往前遍历 为了状态转移的时候
            if j >= goods[i][0]:
                # max函数里面的dp[j]其实代表的就是i-1时的状态值，dp[j-goods[i][0]]也是i-1的状态值
                dp[j] = max(dp[j], dp[j-goods[i][0]] + goods[i][1])
    return dp[-1]
if __name__ == '__main__':
    result = bag_01(4,50,[[0,0],[10,60],[20,100],[30,120]])
    print(result)
    result = bag_01(1,5,[[10,60]])
    print(result)
# 思考：如果要求的不是尽可能最大的价值，而是刚好等于背包容量的最大价值，那么该如何去做呢？

# ----------完全背包问题-----------
# 问题描述：有N件物品和一个容量为V的背包。第i件物品的体积是v[i]，价值是w[i]。求解不超过背包容量的前提下，将哪些物品装入背包可使价值总和最大。
# 约束条件：每种物品的数量为无限个，你可以选择任意数量的物品。（每件物品可以被选多次）

# [例题：](https://leetcode-cn.com/problems/coin-lcci/solution/ying-bi-by-leetcode-solution/)
# ----------01背包问题-----------



# ----------01背包问题-----------





# 1、力扣面试题 08.11. 硬币 题解
# https://leetcode-cn.com/problems/coin-lcci/solution/bei-bao-jiu-jiang-ge-ren-yi-jian-da-jia-fen-xiang-/
# 2、github 背包问题九讲
# https://github.com/tianyicui/pack/blob/master/V1/P01.muse
# 3、动态规划——背包问题python实现（01背包、完全背包、多重背包）
# https://www.cnblogs.com/anzhengyu/p/11408466.html
