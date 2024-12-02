from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def traversal(root):
    if root is None:
        return
    traversal(root.left)

    print("Node: ", root.value)
    traversal(root.right)


def insertNode(root, value):
    if root.value is None:
        root.value = value
        return root
    q = deque()
    q.append(root)
    while q:
        curr = q.popleft()
        if curr.left is not None:
            q.append(curr.left)
        else:
            curr.left = Node(value)
            return root
        if curr.right is not None:
            q.append(curr.right)
        else:
            curr.right = Node(value)
            return root

if __name__ == '__main__':
    bst_file = open('example.txt', 'r')
    root = Node(10)
    root.left = Node(11)
    root.right = Node(9)
    root.left.left = Node(7)
    root.right.left = Node(15)
    root.right.right = Node(8)
    key = 12
    root = insertNode(root, key)
    traversal(root)
