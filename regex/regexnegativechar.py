import re

letterRegex = re.compile(r"[^bBa ]")
print(letterRegex.findall("Betty Botter bought a bit of a better butter"))
