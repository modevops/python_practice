import re 

ssnRegex = re.compile(r"\d\d\d-\d\d-\d\d\d\d")

ssnMatch = ssnRegex.search("The two ssn's you'r looking for are 557-12-8176 and 321-54-9876")

print(ssnMatch.group())