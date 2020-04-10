import re

DrWhoRegex = re.compile(r"^rude")
print(DrWhoRegex.search("rude and not ginger"))

print(DrWhoRegex.search("That was rude"))

print(DrWhoRegex.search("rude and not ginger").group())