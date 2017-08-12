#regex.py

import re

def Main():
	message = "I think I understand regukal expressions"
	mathResult = re.match("think", message, re.M|re.I)
	if mathResult:
		print("Match Found: " + mathResult.group())
	else:
	    print("No Match was Found")	

	searchResult = re.search("think", message, re.M|re.I)
	if searchResult:
	    print("Search Found: " + searchResult.group())
	else:
	    print("Noting found in search")

if __name__ == "__main__":
	Main()