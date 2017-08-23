# sets.py

# Introduction to Sets

n = input()
heights_of_the_plants = [int(pl) for pl in input().split()]

set_of_heights = set(heights_of_the_plants)
sum_of_heights = sum(set_of_heights)
len_of_heights = len(set_of_heights)

avr = sum_of_heights/len_of_heights
print(avr)


# Symmetric Difference
a = input()
m = set([int(i) for i in input().split()])
b = input()
n = set([int(i) for i in input().split()])

m_differ = m.difference(n)
n_differ = n.difference(m)

sim_differ = sorted(list(m.difference(n)) + list(n.difference(m)))

for x in sim_differ:
    print(x)


# Set .add() 
a_set = {input() for el in range(int(input()))}
print(len(a_set))


# Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int,input().split()))
num_of_commands = int(input())

for i in range(num_of_commands):
    choice = input().split()
    if choice[0]=="pop" :
        s.pop()
    elif choice[0]=="remove" :
        s.remove(int(choice[1]))
    elif choice[0]=="discard" :
        s.discard(int(choice[1])) 

print(sum(s))  


# Set .union() Operation
n = input()
eng = {int(i) for i in input().split()}

n1 = input()
french = {int(i) for i in input().split()}

print(len(eng.union(french)))


# Set .intersection() Operation
n = input()
eng = {int(i) for i in input().split()}

n1 = input()
french = {int(i) for i in input().split()}

print(len(eng.intersection(french)))


# Set .difference() Operation
n = input()
eng = {int(i) for i in input().split()}

n1 = input()
french = {int(i) for i in input().split()}

print(len(eng.difference(french)))


# Set .symmetric_difference() Operation
n = input()
eng = {int(i) for i in input().split()}

n1 = input()
french = {int(i) for i in input().split()}

print(len(eng.symmetric_difference(french)))


# Set Mutations
n = int(input())
origin = set(map(int,input().split()))
num_of_commands = int(input())

for i in range(num_of_commands):
    choice = input().split()
    other = set(map(int,input().split()))
    
    if choice[0]=="intersection_update" :
        origin.intersection_update(other)
    elif choice[0]=="update" :
        origin.update(other)
    elif choice[0]=="symmetric_difference_update" :
        origin.symmetric_difference_update(other)
    elif choice[0]=="difference_update" :
        origin.difference_update(other) 
             
            
print(sum(origin))  


# Check Subset
for i in range(int(input())):
    a = int(input()); A = set(input().split()) 
    b = int(input()); B = set(input().split())
    print(A.issubset(B))


#Check Strict Superset 
a_set = {int(i) for i in input().split()}
n = input()
b_set = {int(i) for i in input().split()}
c_set = {int(i) for i in input().split()}

print(a_set.issuperset(b_set) and a_set.issuperset(c_set))


# No Idea!
n, m = input().split()
arr = set(input().split())
A = set(input().split())
B = set(input().split())

# I don't understand why this way doesn't work in for current tests
# print(len(A.intersection(arr)) - len(B.intersection(arr)]))
# At the same time, this solution works. Why?
print(sum([(i in A) - (i in B) for i in arr]))


# The Captain's Room
n = input()
line = input().split()
count = {}

for num in line:
    count.setdefault(num, 0)
    count[num] = count[num] + 1

for k, v in count.items():
    if v == 1:
        print(k)  


# k,arr = int(input()),list(map(int, input().split()))
# myset = set(arr)
# print(((sum(myset)*k)-(sum(arr)))//(k-1))        