# data-structures

April 20th - April 24th - Data Structures

Day 1 - Linked Lists

In an array, a list of items would be:

    [12, 15, 43, 20]

In a _linked list_, it would be:

    [12] -> [15] -> [43] -> [20]

The nodes are isolated, and one item holds the "path" to the next node.

First node in the linked list is the _head_

Last node in the linked list is the _tail_ and it points to None

Linked lists don't have direct access to random items, you would need to start from the head and move on. You also will not be able to go back a place in the linked list, only to the NEXT node.

When you add a new node to the linked list, you first want to have your node point to None, just like the tail node does, then update the tail's pointer value to then be the node you are adding. This ensures there's always a node pointing to None (the tail node)

### Singly/Doubly Linked Lists

Singly Linked Lists are your standard linked list, that point to the next node in the list until the tail, which points to None

Doubly Linked Lists, however, follow the same as Singly Linked Lists, but also can point backwards to their previous node.

### Some Good Questions to Ask Yourself

How would you insert an element into an empty linked list? What about a linked list with only one element?

How would you iterate along a linked list to reach an element that isn't the head nor the tail of the list?

How would you delete an element from a linked list?

### Pros/Cons of linked lists

Pro: Easier to insert into and delete from the middle of a linked list compared to an array

Pro: We can keep adding elements to a linked list as much as we want, unlike arrays that contain a static amount of allocated memory

Con: Linked lists are not as cache-friendly since caches are typically optimized for contiguous memory accesses.

## Queue

FIFO - First In, First Out! As you know.

Queues are simple and intuitive to use and implement

They can be used to serialize data coming in from multiple sources

## LRU Cache

Least-Recently-Used Cache.

Caches keep copies of data from slow sources in a fast, local source. (Webpages you may visit frequently)

Terms:

Cache Hit: When the data you want is in the cache
Cache Miss: When you have to go to the primary storage to get the data (was not in the cache)

Caches are limited in size compared to primary storage

LRU Caches discard the Least-RecentlyUsed item in the cache when it is full. Clears out space for more important things!

Day 2 - Queues and Stacks

Day 3 - Binary Search Trees

Day 4 - Tree Traversal
