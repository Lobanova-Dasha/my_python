#! python3
# data_structures.py
from collections import deque

#Linked List
class Node:
    """Linked list is either None or a value and a link to the next list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


head = Node(1, Node(2, Node(3, Node(4))))


def print_list(head, end='\n'):
    while head:
        print(head.data, end=' -> ' if head.next else '')
        head = head.next
    print(end=end)


print_list(head)


def reverse_list(head, tail=None):
    while head:
        head.next, tail, head = tail, head, head.next
    return tail


print_list(reverse_list(head))


# Queue
my_queue = []
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)
my_queue.append(4)

print(my_queue)
print(my_queue.pop(0))
my_queue.append(5)
print(my_queue)

# Deque
q = deque()
 
q.append('eat')
q.append('sleep')
q.append('code')
 
print(q)
# deque(['eat', 'sleep', 'code'])

print(q.popleft()) # 'eat'
print(q.popleft()) # 'sleep'
print(q.popleft()) # 'code'
 
print(q.popleft())

