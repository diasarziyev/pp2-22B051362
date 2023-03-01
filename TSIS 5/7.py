import re
snake = input()
words = snake.split("_")
up_words = [words[0]] + [w.capitalize() for w in words[1:]]
camel = "".join(up_words)
print(camel)