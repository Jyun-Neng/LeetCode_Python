"""
Given a linked list, remove the n-th node from the end of list and return its head.
Note:
Given n will always be valid.

Example:

Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = second = head
        for i in range(n):
            first = first.next
        # if only one node in list
        if not first:
            return head.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head


if __name__ == "__main__":
    head = ListNode(1)
    node = ListNode(2)
    head.next = node
    node.next = ListNode(3)
    node = node.next
    node.next = ListNode(4)
    node = node.next
    node.next = ListNode(5)
    head = Solution().removeNthFromEnd(head, 2)
    while head:
        print(head.val, end=' ')
        head = head.next
    print('')
