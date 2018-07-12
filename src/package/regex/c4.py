import re

language = 'PythonC#JavaPHPC#'


def convert(value):
    metched = value.group()
    return '!!' + metched + '!!'


# r = language.replace('C#', 'GO')
r = re.sub('C#', convert, language, 0)
print(r)
