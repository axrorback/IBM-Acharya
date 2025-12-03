class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2

current = n1

while current is not None:
    print(current.data, end='->')
    current = current.next
print("None")


#Reverse the linked list
current = n3
while current is not None:
    print(current.data, end='->')
    current = current.prev
print("None")