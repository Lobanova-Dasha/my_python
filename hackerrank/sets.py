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