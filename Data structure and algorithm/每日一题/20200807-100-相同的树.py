# 20200807-100-相同的树 
# 题目链接：https://leetcode-cn.com/problems/same-tree/
# 时间、空间复杂度：O(min(m,n)) 其中 m和 n 分别是两个二叉树的节点数。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # BFS
        if not p and not q:return True
        if not p or not q:return False
        stackp=collections.deque([p])
        stackq=collections.deque([q])
        while stackp and stackq:
            tmpp=stackp.popleft()
            tmpq=stackq.popleft()
            if tmpp.val != tmpq.val:
                return False
            if tmpp.left and tmpq.left:
                stackp.append(tmpp.left)
                stackq.append(tmpq.left)
            if (tmpp.left and not tmpq.left) or (not tmpp.left and tmpq.left):
                return False
            if tmpp.left and tmpq.left:
                stackp.append(tmpp.left)
                stackq.append(tmpq.left)
            if (tmpp.left and not tmpq.left) or (not tmpp.left and tmpq.left):
                return False
            if tmpp.right and tmpq.right:
                stackp.append(tmpp.right)
                stackq.append(tmpq.right)
            if (tmpp.right and not tmpq.right) or (not tmpp.right and tmpq.right):
                return False
        return True
                


