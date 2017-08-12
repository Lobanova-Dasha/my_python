#! python3
# mad_libs.py _ reads in text files and lets the user add their own text
# anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. 


message = ''' The ADJECTIVE panda walked to the NOUN and then VERB. A
 nearby NOUN was unaffected by these events'''
print(message)

import re

adj = input('Type your adjective: ')
noun = input('Type your noun: ')
verb = input('Type your verb: ')
noun2 = input('Type your noun2: ')

result = re.sub(r'VERB', verb, message)
result2 = re.sub(r'ADJECTIVE', adj, result)
result3 = re.sub(r'NOUN', noun, result2)
result4 = re.sub(r'NOUN', noun2, result3)

print(result4)