import re

DrSeuss = "The Grinch hated Christmas\nThe whole Christmas season!\nNow, please don't ask why."

print(DrSeuss)

DotallRegex = re.compile(r".*", re.DOTALL)
print(DotallRegex.search(DrSeuss).group())