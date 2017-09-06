regexp.py

import re
for i in range(int(raw_input())):
    print bool(re.search(r"^[+-]?\d*\.\d+$",raw_input().strip()))