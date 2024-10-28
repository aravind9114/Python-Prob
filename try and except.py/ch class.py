import re
pattern="[A-Z][0-9][a-z]"
if re.search(pattern,"PA8yy"):
    print("matched")
else:
    print("not matched")