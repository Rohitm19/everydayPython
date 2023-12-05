#neetCode
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]


#vsCode
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        oldToCopy = {None: None}

        # Function to copy a node
        def copy_node(node):
            if node in oldToCopy:
                return oldToCopy[node]
            copy = Node(node.val)
            oldToCopy[node] = copy
            copy.next = copy_node(node.next)
            copy.random = copy_node(node.random)
            return copy

        return copy_node(head)

# Manual input and usage
solution = Solution()

# Create some nodes and connections
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node1.random = node3
node2.next = node3
node2.random = node1
node3.random = node2

# Copy the linked list
copied_head = solution.copyRandomList(node1)

# Print the values and random pointers of the copied linked list
cur = copied_head
while cur:
    print("Value:", cur.val)
    if cur.random:
        print("Random points to value:", cur.random.val)
    else:
        print("Random points to None")
    cur = cur.next
