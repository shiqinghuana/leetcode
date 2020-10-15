# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        l = []

        def su(root: TreeNode):
            if root:
                if root.left and not root.left.left and not root.left.right:
                    l.append(root.left.val)

                su(root.left)
                su(root.right)

        su(root)
        return sum(l)