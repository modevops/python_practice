import re 

blahRegex = re.compile(r"(blah){2,4}")

blah_match = blahRegex.search("blahblah")

print(blah_match.group())
blah_match = blahRegex.search("blahblahblahblahblahblah")

print(blah_match.group())