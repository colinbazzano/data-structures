

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)
        self.value = value

    def reverse(self):
        prev = None  # Starts as None
        current = self.value  # the head
        while (current is not None):  # While the head is not None
            next = current.next  # one to the right
            current.next = prev  # next is None
            prev = current
            current = next
        self.value = prev


def reverseNode(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def find_half(head):
    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


node4 = Node(3)
node3 = Node(2)
node2 = Node(1)
node1 = Node(0)

# print(find_half(node1).value)

print(Node.reverse(node1))
