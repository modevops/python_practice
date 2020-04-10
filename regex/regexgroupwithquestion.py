import re

businessRegex = re.compile(r"business(wo)?man") 

businessMatch = businessRegex.search("She is a businesswoman.")

print(businessMatch.group())


businessMatch = businessRegex.search("Warren Buffet is quite famous as a businessman.")

print(businessMatch.group())