#lookup.py main lookup.py

import re
import argparse

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument('word', help='specify word to search for')
	parser.add_argument('fname', help='specify file to search for')
	args = parser.parse_args()

	searchFile = open(args.fname)
	lineNum = 0

	for line in searchFile.readlines():
		line = line.strip('\n\r')
		lineNum += 1
		searchResult = re.search(args.word, line, re.M|re.I)
		if searchResult:
			print(str(lineNum) + ': ' + line)

if __name__ == '__main__':
    Main()			
	