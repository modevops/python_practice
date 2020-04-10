import re

zipRegex = re.compile(r"((\d\d\d\d\d)-\d\d\d\d)")

zipCodes = """

33410-5260
33410-5266
33410-5261
33410-5262

"""

print(zipRegex.findall(zipCodes))
