"""
Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1
        con, tail = prev, cur
        # reverse
        while n:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            n -= 1
        # the condition of m = 1
        # con point to None
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
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
    head = Solution().reverseBetween(head, 1, 3)
    while head:
        print(head.val, end=' ')
        head = head.next
    print('')
