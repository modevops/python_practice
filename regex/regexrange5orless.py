import re 

blahRegex = re.compile(r"(blah){,5}")

blah_match = blahRegex.search("blahblah")

print(blah_match.group())
blah_match = blahRegex.search("blahblahblahblahblahblah")

print(blah_match.group())

blah_match = blahRegex.search("blahblahblahblahblah")

print(blah_match.group())

print(blah_match.group())
blah_match = blahRegex.search("blahblahblahblahblahblah")

print(blah_match.group())