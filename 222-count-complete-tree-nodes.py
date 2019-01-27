"""
Given a complete binary tree, count the number of nodes.
Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6
Output: 6
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getHeight(self, node):
        if not node:
            return 0
        return 1 + self.getHeight(node.left)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        time complexity: O(log(N)^2)
        """
        cnt = 0
        while root:
            # root is height 0
            l, r = self.getHeight(root.left), self.getHeight(root.right)
            if l == r:
                root = root.right
                # add the number of left subtree nodes
                cnt += pow(2, l)
            else:
                root = root.left
                # add the number of left subtree nodes without last level
                cnt += pow(2, r)
        return cnt


if __name__ == "__main__":
    vals = [1, 2, 3]
    root = TreeNode(vals[0])
    node = root
    node.left = TreeNode(vals[1])
    node.right = TreeNode(vals[2])
    print(Solution().countNodes(root))
