#! python3
# inventory.py - Creates cards for the Fantasy Game Inventory 
# ("Automate the Boring Stuff with Python" by Albert Sweigart).
# The data structure to model the player’s inventory is a dictionary
# where the keys are string values describing the item
# in the inventory and the value is an integer value detailing 
# how many of that item the player has. 

my_cards = {'rope':1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 


def displayCards(cards):
	''' takes any possible “inventory”
 and displays it like the following:

        Inventory:
        12 arrow
        42 gold coin
        1 rope
        6 torch
        1 dagger
        Total number of items: 63 '''

	print('Inventory: ')
	item_total = 0
	for k, v in cards.items():
		print(str(v) + ' ' + k)
		item_total += v
	print('Total number of items: ' + str(item_total))


displayCards(my_cards)			

# List to Dictionary Function for Fantasy Game Inventory

from collections import Counter

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] 


def addToInventory(inventory, addedItems) :
	''' returns a dictionary that represents 
	the updated inventory. 

	Keyword arguments:
	inventory -- is a dictionary representing the player’s inventory 
	addedItems -- is a list like dragonLoot,
	can contain multiples of the same item.  


	'''
	count = {}
	for i in addedItems:
		count.setdefault(i, 0)
		count[i] = count[i] + 1
		new_count = count

	c1 = Counter(new_count)
	c2 = Counter(inv)
	result = dict(c1 + c2)
	return result
	print(result)


inv = addToInventory(inv, dragonLoot)
displayCards(inv)

