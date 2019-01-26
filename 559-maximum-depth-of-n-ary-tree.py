"""
Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
import collections
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        queue = collections.deque([])
        queue.append([root, 1])
        # BFS
        while queue:
            node, depth = queue.popleft()
            for child in node.children:
                queue.append([child, depth + 1])
        return depth


if __name__ == "__main__":
    node5 = Node(5, [])
    node6 = Node(6, [])
    node4 = Node(4, [])
    node3 = Node(3, [])
    node2 = Node(2, {node5, node6})
    node1 = Node(1, {node2, node3, node4})
    print(Solution().maxDepth(node1))
