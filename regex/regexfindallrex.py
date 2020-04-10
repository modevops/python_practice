import re

zipRegex = re.compile(r"\d\d\d\d\d")

addressess = """
1151 Custer Pl
Aurora, CO 80012


113 E Custer Pl
Aurora, CO 800123


115 E Custer Pl
Aurora, CO 80013

"""

print(zipRegex.findall(addressess))

