# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# dfs
# 时间复杂度：O(n)，其中 N 为树的节点个数。
# 空间复杂度：O(h)，其中 h 为树的高度， 最坏的情况下树退化到链表，这个时候高度为 N，其中 N 为树的节点个数。
# 参考：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/jian-dan-di-gui-zhe-ti-de-ben-zhi-jiu-shi-hou-xu-b/
class Solution:
    ans = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(node):
            if not node: return 0
            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            l = max(helper(node.left),0)
            r = max(helper(node.right),0)
            self.ans = max(self.ans, l + r + node.val)
            return max(l, r, 0) + node.val
        helper(root)
        return self.ans
