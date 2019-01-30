"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:

Given 1->2->3->4, reorder it to 1->4->2->3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # empty list
        if not head:
            return
        first = second = head
        # find the middle node of list
        while first and first.next:
            first = first.next.next
            second = second.next
        mid = second.next
        second.next = None
        # reverse the last half of list
        reverse = None
        while mid:
            temp = mid.next
            mid.next = reverse
            reverse = mid
            mid = temp
        # merge the first half list and the last half list
        node = head
        while reverse:  # the length of last half of list is always less than and equal to the first half of list
            temp1 = node.next
            temp2 = reverse.next
            node.next = reverse
            reverse.next = temp1
            node = temp1
            reverse = temp2


if __name__ == "__main__":
    head = ListNode(1)
    node = ListNode(2)
    head.next = node
    node.next = ListNode(3)
    node = node.next
    node.next = ListNode(4)
    node = node.next
    node.next = ListNode(5)
    Solution().reorderList(head)
    while head:
        print(head.val, end=' ')
        head = head.next
    print('')
