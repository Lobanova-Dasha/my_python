import pprint

message = '''It was a rainy cold day in July, 
          and the clocks were striking seventeen.'''

count = {}

for character in message:
	count.setdefault(character, 0)
	count[character] += 1


pprint.pprint(count)	
print(pprint.pformat(count)) #the same one