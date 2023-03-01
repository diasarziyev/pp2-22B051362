import re
txt = input()
x = re.sub("\s" , ":", txt)
y = re.sub("\.",":",x)
z = re.sub("\,",":",y)
print(z)