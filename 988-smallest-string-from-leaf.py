"""
Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': 
a value of 0 represents 'a', a value of 1 represents 'b', and so on.
Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
(As a reminder, any shorter prefix of a string is lexicographically smaller: 
for example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)
Note:

    1. The number of nodes in the given tree will be between 1 and 1000.
    2. Each node in the tree will have a value between 0 and 25.

Example:

Input: [0,1,2,3,4,3,4]
Output: "dba"
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        left = self.smallestFromLeaf(root.left)
        right = self.smallestFromLeaf(root.right)
        # from leaf to root
        if right == '' or (left != '' and left < right):
            return left + chr(97 + root.val)
        return right + chr(97 + root.val)


if __name__ == "__main__":
    vals = [3, 9, 20, None, None, 15, 7]
    root = TreeNode(vals[0])
    node = root
    node.left = TreeNode(vals[1])
    node.right = TreeNode(vals[2])
    node = node.right
    node.left = TreeNode(vals[5])
    node.right = TreeNode(vals[6])
    print(Solution().smallestFromLeaf(root))
