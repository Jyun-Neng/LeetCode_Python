"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reverse = None
        while head:
            tmp, head.next = head.next, reverse
            reverse, head = head, tmp
        return reverse


if __name__ == "__main__":
    head = ListNode(1)
    node = ListNode(2)
    head.next = node
    node.next = ListNode(3)
    node = node.next
    node.next = ListNode(4)
    head = Solution().reverseList(head)
    while head:
        print(head.val, end=' ')
        head = head.next
    print('')
