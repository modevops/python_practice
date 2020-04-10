import re

runRegex = re.compile(r"run(ning|ner|s)")

run_match = runRegex.search("The marathon running is quick")

print(run_match.group())
print(run_match.group(1))