"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, 
it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.table = dict()
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.table:
            # remove the existed node in queue
            node = self.table[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            # add to queue
            tmp = self.head.next
            self.head.next, node.prev = node, self.head
            node.next, tmp.prev = tmp, node
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.table:
            # remove the existed node in queue
            node = self.table[key]
            node.prev.next = node.next
            node.next.prev = node.prev

        node = Node(key, value)
        # add to queue
        tmp = self.head.next
        self.head.next, node.prev = node, self.head
        node.next, tmp.prev = tmp, node
        # update table
        self.table[key] = node
        if self.capacity < len(self.table):
            # remove the last node in queue
            node = self.tail.prev
            self.tail.prev, node.prev.next = node.prev, self.tail
            # remove the key of the last node in the table
            self.table.pop(node.key)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
