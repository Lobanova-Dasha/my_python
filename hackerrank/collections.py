#collections.py

from collections import Counter

numShoes = int(input())
shoes = Counter(map(int, input().split()))
numCust = int(input())

income = 0

for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1

print(income)


# Collections.OrderedDict()
# Task. You are the manager of a supermarket. 
# You have a list of  N items together with their prices 
# that consumers bought on a particular day. 
# Your task is to print each item_name and net_price 
# in order of its first occurrence.
from collections import OrderedDict

bill_order = OrderedDict()

for _ in range(int(input())):
    item_name, space, net_price = input().rpartition(' ')
    
    bill_order[item_name] = bill_order.get(item_name, 0) + int(net_price)

    '''the same

    if name not in bill_order:
        bill_order[name] = int(price)
    else:
        bill_order[name] += int(price)'''

for item_name, net_price in bill_order.items():
    print(item_name, net_price)


# Collections.deque() 
# Task. Perform append, pop, popleft and appendleft methods 
# on an empty deque d.
from collections import deque

dq = deque()
num_of_commands = int(input())

for i in range(num_of_commands):
    choice = input().split()
    if choice[0] == "pop":
        dq.pop()
    elif choice[0] == "append":
        dq.append(int(choice[1]))
    elif choice[0]=="popleft" :
        dq.popleft() 
    elif choice[0] == "appendleft":
        dq.appendleft(int(choice[1]))

print(*list(dq)) 
