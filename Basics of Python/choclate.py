
import re

value = input()

result = re.match("[-+]?\d+$", value)

if result is not None:
    print("INT")
else:
    print("STR")