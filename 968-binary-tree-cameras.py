"""
Given a binary tree, we install cameras on the nodes of the tree.
Each camera at a node can monitor its parent, itself, and its immediate children.
Calculate the minimum number of cameras needed to monitor all nodes of the tree.

Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.camera = 0
        self.covered = {None}

    def dfs(self, node, parent):
        if node is None:
            return
        self.dfs(node.left, node)
        self.dfs(node.right, node)
        # leaf node
        if node.left is None and node.right is None:
            return
        # append children, parent, and itself into covered dict
        # search element in dict is O(1)
        if node.left not in self.covered or node.right not in self.covered:
            self.camera += 1
            self.covered.update({parent, node, node.left, node.right})
            return

    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root, None)
        if root not in self.covered:
            self.camera += 1
        return self.camera


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(0)
    node = root.left
    node.left = TreeNode(0)
    node.right = TreeNode(0)
    print(Solution().minCameraCover(root))
