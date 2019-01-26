"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
import collections
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = collections.deque([])
        queue.append([root, 1])
        # BFS
        while queue:
            node, depth = queue.popleft()
            if node.left:
                queue.append([node.left, depth + 1])
            if node.right:
                queue.append([node.right, depth + 1])
        return depth


if __name__ == "__main__":
    vals = [3, 9, 20, None, None, 15, 7]
    root = TreeNode(vals[0])
    node = root
    node.left = TreeNode(vals[1])
    node.right = TreeNode(vals[2])
    node = node.right
    node.left = TreeNode(vals[5])
    node.right = TreeNode(vals[6])
    print(Solution().maxDepth(root))
