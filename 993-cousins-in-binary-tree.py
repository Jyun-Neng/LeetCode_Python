"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.

Note:
    1. The number of nodes in the tree will be between 2 and 100.
    2. Each node has a unique integer value from 1 to 100.

Example:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false
"""
import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False
        queue = collections.deque([])
        queue.append([None, root, 0])
        cousins = 0
        # BFS
        while queue:
            par, node, depth = queue.popleft()
            if node.val == x:
                cousins += 1
                node_x = [par, depth]
            elif node.val == y:
                cousins += 1
                node_y = [par, depth]
            if cousins == 2:
                if node_x[0] != node_y[0] and node_x[1] == node_y[1]:
                    return True
                else:
                    return False
            if node.left:
                queue.append([node, node.left, depth + 1])
            if node.right:
                queue.append([node, node.right, depth + 1])
        return False


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    node = root.left
    node.left = TreeNode(4)
    print(Solution().isCousins(root, 3, 4))
