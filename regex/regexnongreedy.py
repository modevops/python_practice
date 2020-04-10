import re

wordRegex = re.compile(r"(\w){1,3}?")

word_match = wordRegex.search("Eyes")

print(word_match.group())