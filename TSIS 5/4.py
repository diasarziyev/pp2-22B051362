import re
txt = input()
x = re.findall("^[A-Z]([a-z]*)$",txt)
if x:
    print("YES")
else:
    print("NO")