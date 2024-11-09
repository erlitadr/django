import re

pattern = r'\W+'

text = ' This isString'

x=re.findall(pattern, text)

print(x)