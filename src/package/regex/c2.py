import re

a = 'C0C++7Java9C#5PythonJavaScript'

r = re.findall('\D', a)
print(r)
