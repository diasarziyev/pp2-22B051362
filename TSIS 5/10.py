import re
camel = input()
spl = re.sub('([A-Z][a-z]+)',r' \1',camel).split()
snk = '_'.join([s.lower() for s in spl])
print(snk)