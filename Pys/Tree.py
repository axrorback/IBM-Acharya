#Binary trees
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
F = Node(6)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

print('************* Pre Order ***************')


def pre_order(node):
    if not node:
        return

    print(node.val)
    pre_order(node.left)
    pre_order(node.right)

pre_order(A)

print('************* In Order ***************')

def in_order(node):
    if not node:
        return

    pre_order(node.left)
    print(node.val)
    pre_order(node.right)

in_order(A)

print('************* Post Order ***************')

def post_order(node):
    if not node:
        return

    pre_order(node.left)
    pre_order(node.right)
    print(node.val)


in_order(A)