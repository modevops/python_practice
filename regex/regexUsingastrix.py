import re

snakeRegex = re.compile(r"snake(s)*")

snake_match = snakeRegex.search("I saw green snakes.")

print(snake_match.group())

snake_match = snakeRegex.search("I saw green snakesssss.")

print(snake_match.group())