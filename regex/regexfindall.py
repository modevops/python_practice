import re

dateRegex = re.compile(r"\d{2}\/\d{2}\/\d{4}")

print(dateRegex.findall("The dates are 11/12/2015, 09/02/2000, 02/11/1991"))