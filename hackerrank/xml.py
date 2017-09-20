#xml.py

import sys 
import xml.etree.ElementTree as etree

xml = ''.join([input() for line in range(int(input()))])
tree = etree.ElementTree(etree.fromstring(xml))

# XML 1 - Find the Score
# You are given a valid XML document, and you have to print its score. 
# The score is calculated by the sum of the score of each element. 
# For any element, the score is equal to the number of attributes it has.
def get_attr_number(node):
    return len(node.attrib) + sum(get_attr_number(child) for child in node)

print(get_attr_number(tree.getroot()))


# if __name__ == '__main__':
#     sys.stdin.readline()
#     xml = sys.stdin.read()
#     tree = etree.ElementTree(etree.fromstring(xml))
#     root = tree.getroot()
#     print(get_attr_number(root))



# XML2 - Find the Maximum Depth
# You are given a valid XML document, and you have to print the maximum level of nesting in it.
maxdepth = -1

def depth(elem, level):
    global maxdepth
    
    if (level == maxdepth):
        maxdepth += 1
        
    for child in elem:
        depth(child, level + 1)

depth(tree.getroot(), -1)
print(maxdepth)        