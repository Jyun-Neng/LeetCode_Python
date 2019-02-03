"""
Given a binary tree, return the vertical order traversal of its nodes values.
For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).
Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, 
we report the values of the nodes in order from top to bottom (decreasing Y coordinates).
If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.
Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.
Note:

    1. The tree will have between 1 and 1000 nodes.
    2. Each node's value will be between 0 and 1000.

Example:

Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
"""
import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def dfs(self, node, x, y):
        if not node:
            return
        self.map[x][y].append(node.val)
        self.dfs(node.left, x - 1, y + 1)
        self.dfs(node.right, x + 1, y + 1)

    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.map = collections.defaultdict(
            lambda: collections.defaultdict(list))
        # record the position of each node
        self.dfs(root, 0, 1)
        ans = []
        for x in sorted(self.map):
            res = []
            for y in sorted(self.map[x]):
                res.extend(sorted(self.map[x][y]))
            ans.append(res)
        return ans


if __name__ == "__main__":
    vals = [3, 9, 20, None, None, 15, 7]
    root = TreeNode(vals[0])
    node = root
    node.left = TreeNode(vals[1])
    node.right = TreeNode(vals[2])
    node = node.right
    node.left = TreeNode(vals[5])
    node.right = TreeNode(vals[6])
    print(Solution().verticalTraversal(root))
