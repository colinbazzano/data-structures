# Building an LRU Cache
"""LRU Cache

We will need a hash table to quickly look up cache entries by key O(1) searching!

Also, a doubly-linked list for the cache entries. O(1) operations for insert/delete

A Hash Table for doubly linked list

We will use the doubly-linked list to order from MRU to LRU

Some questions to consider:

What are some applications of LRU Cache?


"""
import time


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    cache_limit = 3  # set to 3 just for easy demo
    DEBUG = False

    def __init__(self, func):
        self.func = func
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail  # the bottom equals the tail
        self.tail.prev = self.head  # doubly linked list

    def __call__(self, *args, **kwargs):
        # If in cache, pull results
        if args in self.cache:
            self.llist(args)
            if self.DEBUG == True:
                return f'Cached...{args}\n{self.cache[args]}\nCache: {self.cache}'
            return self.cache[args]

        # If cache-limit reached - Remove LRU from node link list and dict - cache.
        if self.cache_limit is not None:
            if len(self.cache) > self.cache_limit:
                n = self.head.next
                self._remove(n)
                del self.cache[n.key]

        # Compute and cache and node - if not in cache
        result = self.func(*args, **kwargs)
        self.cache[args] = result
        node = Node(args, result)
        self._add(node)
        if self.DEBUG == True:
            return f'{result}\nCache: {self.cache}'
        return result

    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = node
        node.prev = prev

    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail

    def llist(self, args):
        current = self.head
        while True:
            if current.key == args:
                node = current
                self._remove(node)
                self._add(node)
                break
            else:
                current = current.next
