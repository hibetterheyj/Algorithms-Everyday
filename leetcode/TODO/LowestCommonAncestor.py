# -*- coding: utf-8 -*-
"""
236. Lowest Common Ancestor of a Binary Tree
解法同样使用235，对于Binary Search Tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root is None or root == p or root==q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 表示左右均能找到，那么对应的root就是LCA
        if (left is not None and right is not None):
            return root
        if (left is None):
            return right
        if (right is None):
            return left
        return None

if __name__ == '__main__':

    a = Tree = TreeNode(2)
    b = Tree.left = TreeNode(1)
    c = Tree.right = TreeNode(3)
    d = c.left=TreeNode(4)
    s = Solution()
    # 对应树的结构
    print(s.lowestCommonAncestor(a,b,d).val)