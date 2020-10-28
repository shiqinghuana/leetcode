# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        l = [root]

        n = 0
        while n<len(l):
            pre = l[n]
            z= n
            if isinstance(pre,TreeNode):
                l[n] = pre.val
                if pre.left:
                    n+=1
                    l.insert(n,pre.left)
                if pre.right:
                    n+=1
                    l.insert(n,pre.right)

            n = z+1
        return l


    def preorderTraversal1(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        return [root.val]+self.preorderTraversal(root.left) + self.preorderTraversal(root.right)