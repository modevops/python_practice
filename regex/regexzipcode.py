import re 

ssnRegex = re.compile(r"\d{5}-\d{4}")

ssnMatch = ssnRegex.search("The zip code is 98210-1138" )

print(ssnMatch.group())