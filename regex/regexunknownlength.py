import re

nameRegex = re.compile(r"My name is (.*)")

print(nameRegex.search("My name is John Marston.").group())