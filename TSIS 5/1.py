import re
txt = input()
x = re.findall('^a(b*)$',txt)
if x:
    print("Yes")
else:
    print("No")