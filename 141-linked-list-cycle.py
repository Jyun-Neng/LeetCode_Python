"""
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, 
we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.

Example:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
"""

# Definition for singly-linked list.
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        first = head.next
        second = head
        while first != second:
            if not first or not first.next:
                return False
            first = first.next.next
            second = second.next
        return True


if __name__ == "__main__":
    head = ListNode(1)
    node = ListNode(2)
    head.next = node
    node.next = ListNode(3)
    node = node.next
    node.next = ListNode(4)
    node = node.next
    node.next = head
    print(Solution().hasCycle(head))
