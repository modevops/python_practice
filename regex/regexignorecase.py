import re

ignoreCaseRegex = re.compile(r"[b]", re.IGNORECASE)

print(ignoreCaseRegex.findall("Betty Botter bought a bit of better butter to make the Botters' butter better."))