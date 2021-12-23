import re
regex=re.compile(r'(app)?le')
matchobj=regex.search(input())
print(matchobj.group())