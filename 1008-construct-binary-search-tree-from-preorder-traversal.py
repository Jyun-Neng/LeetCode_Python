# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        val, N = preorder[0], len(preorder)
        node = TreeNode(val)
        i = 1
        while i < N and preorder[i] < val:
            i += 1
        # each value of left subtree is less than val    
        node.left = self.bstFromPreorder(preorder[1:i])
        # each value of right subtree is large than val
        node.right = self.bstFromPreorder(preorder[i:N])
        return node
