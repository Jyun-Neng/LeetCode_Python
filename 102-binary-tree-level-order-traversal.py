"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = collections.deque([])
        queue.append([root, 1])
        level = 1
        nodes, res = [], []
        # BFS
        while queue:
            node, depth = queue.popleft()
            # record same level nodes
            if depth == level:
                nodes.append(node.val)
            else:   # traverse the different level should create a new nodes list
                res.append(nodes)
                nodes = []
                nodes.append(node.val)
                level += 1
            # BFS push nodes into queue
            if node.left:
                queue.append([node.left, depth + 1])
            if node.right:
                queue.append([node.right, depth + 1])
        # add last level nodes
        res.append(nodes)
        return res


if __name__ == "__main__":
    vals = [3, 9, 20, None, None, 15, 7]
    root = TreeNode(vals[0])
    node = root
    node.left = TreeNode(vals[1])
    node.right = TreeNode(vals[2])
    node = node.right
    node.left = TreeNode(vals[5])
    node.right = TreeNode(vals[6])
    print(Solution().levelOrder(root))
