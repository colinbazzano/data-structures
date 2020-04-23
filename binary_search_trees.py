"""Binary Search Trees

Some quality terminology:

Root: The topmost node in the tree. (like the head?)

Child: A node directly connected to another node when moving TOWARDS the root node.

Siblings: Nodes that share the same parent

Leaf: A node that does NOT have any children of its own.

Each break in the binary search tree, the LEFT will be less than the parent, and the RIGHT will be more. This starts at the top and keeps going in that method.

"""


# class BinarySearchTree:
#     self.value = value
#     self.left = left_subtree
#     self.right = right_subtree

from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')

# self = NODE (binary search node)


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # check if self.left is a valid node
            if self.left:  # is Not None / is there a node here
                self.left.insert(value)
            # base case - the left side is empty
            else:
                # we've found our valid parking spot
                self.left = BinarySearchTree(value)
        # otherwise, value >= self.value
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        # # base case: we found a parking spot
        # # we're in an empty spot in the tree
        # if self is None:
        #     self = BinarySearchTree(value)
        # else:
        #     # self is a node with a value
        #     # compare the value to the value at this node
        #     if value < self.value:

        # # if we aren't at the base case, move towards it

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
