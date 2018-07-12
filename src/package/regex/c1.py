import re

a = 'C0C++7Java9C#5PythonJavaScript'

# print(a.index('Python') > -1)
# print('Python' in a)

if len(re.findall('Python', a)) > 0:
    print('字符串中包含 Python')

if len(re.findall('PHP', a)) > 0:
    print('字符串中包含 PHP')
else:
    print('字符串中不包含 PHP')
