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



# Word Order
# You are given n words. Some words may repeat. 
#For each word, output its number of occurrences. 
# The output order should correspond with the input order 
# of appearance of the word. 
# See the sample input/output for clarification.
from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

order_counter  = OrderedCounter(input() for _ in range(int(input())))

print(len(order_counter))
print(*order_counter.values())

# This way failed :(
from collections import Counter

my_counter = Counter([input() for _ in range(int(input()))])

res = [v for k, v in my_counter.items()]
print(len(res))
print(*(sorted(res, reverse=True)))


# Most Common
# You are given a string S. 
# The string contains only lowercase English alphabet characters.
# Your task is to find the top 
# three most common characters in the string S.

# This is my solution, but sometimes it fails several tests
from collections import Counter, OrderedDict

my_counter = Counter(sorted(input()))

order_counter = OrderedDict([i for i in my_counter.most_common(3)])

for k, v in order_counter.items():
    print(k, v)    


# This isn't my solution, but it always works
from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]