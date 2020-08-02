# 参考：https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/tu-jie-er-cha-shu-de-si-chong-bian-li-by-z1m/

# -------- leeftcode114 前序遍历 --------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 时间空间复杂度均为O(n)
        """
        # 递归
        rs =[]
        def dfs(root):
            # 为了让上一级定义的rs能在这个函数中使用
            nonlocal rs
            if not root:
                return
            rs.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return rs
        """
        # 迭代
        if root is None:
            return []
        # [root,]的逗号是方便多行定义的时候复制的,否则容易在添加元素的过程中缺少逗号出现语法错误.
        stack,rs=[root,],[]
        while stack:
            root = stack.pop()
            if root is not None:
                rs.append(root.val)
                # 由于栈先进后出，因此前序遍历中先把右叶子结点压入栈中
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        return rs

# ----------- leetcode94 中序遍历 ----------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        # 递归
        rs=[]
        def dfs(root):
            if root is None:return
            dfs(root.left)
            dfs(root.right)
            rs.append(root.val)
        dfs(root)
        return rs
        """
        # 迭代
        if root is None:return []
        cur,stack,rs=root,[],[]
        while cur or stack:
            while cur:
                rs.append(cur.val)
                stack.append(cur)
                cur = cur.right
            tmp = stack.pop()
            cur = tmp.left
        return rs[::-1]
        # 访问标记法
        if root is None:return []
        Y,N=1,0
        stack,rs=[(N,root)],[]
        while stack:
            flag,root=stack.pop()
            if root is None:continue
            if flag == N:
                stack.append((Y,root))
                stack.append((N,root.right))
                stack.append((N,root.left))
        return rs

# ----------- leetcode 145 后序遍历 ---------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        # 递归
        rs=[]
        def dfs(root):
            if root is None:return
            dfs(root.left)
            dfs(root.right)
            rs.append(root.val)
        dfs(root)
        return rs
        """
        # 迭代
        if root is None:return []
        cur,stack,rs=root,[],[]
        while cur or stack:
            while cur:
                rs.append(cur.val)
                stack.append(cur)
                cur = cur.right
            tmp = stack.pop()
            cur = tmp.left
        return rs[::-1]
        # 访问标记法
        if root is None:return []
        Y,N=1,0
        stack,rs=[(N,root)],[]
        while stack:
            flag,root=stack.pop()
            if root is None:continue
            if flag == N:
                stack.append((Y,root))
                stack.append((N,root.right))
                stack.append((N,root.left))
        return rs
# --------- leetcode 102 层次遍历 -----------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        # 调用collections.deque()
        # 空节点
        if not root:return []

        # 思路：将一层的节点储存起来，然后遍历
        myroot=collections.deque()
        # 压入初始节点
        myroot.append(root)
        # 结果
        rs=[]
        while myroot:
            cur_layer=[] # 临时变量，记录当前层的节点
            for _ in range(len(myroot)):  # 遍历某一层的节点
                node = myroot.popleft()
                cur_layer.append(node.val)
                # 如果当前节点有左右节点，则压入队列，根据题意注意压入顺序，先左后右
                if node.left:
                    myroot.append(node.left)
                if node.right:
                    myroot.append(node.right)
            rs.append(cur_layer)
        return rs
        """
        if not root:return []
        queue=[root]
        rs=[]
        while queue:
            n =len(queue)
            level = []
            for i in range(n):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            rs.append(level)
        return rs
