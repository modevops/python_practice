import re

phoneRegex = re.compile(r"\W\d{3}\W\s\d{3}-\d{4}")

#print(phoneRegex.search("My new phone number is (425) 644-5121."))
print (phoneRegex.sub("(360) 991-8012", "My new phone number is (425) 644-5121."))