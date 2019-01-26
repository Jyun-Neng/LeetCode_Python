"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = collections.deque([])
        queue.append(root)
        reverse = False
        res = []
        # BFS
        while queue:
            size = len(queue)
            nodes = [0 for i in range(size)]
            for i in range(size):
                node = queue.popleft()
                idx = i if not reverse else size - 1 - i
                nodes[idx] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            reverse = not reverse
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
    print(Solution().zigzagLevelOrder(root))
