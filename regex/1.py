import re
'''regex=re.compile(r'bat(man|mobile|woman|pokemon)')
searchobj=regex.search(input())
if searchobj.group():
    print(searchobj.group())
else:
    print("pattern not found")'''

regex=re.compile(r'\w+')
searchobj=regex.search('ashwin prabhu')
print(searchobj.group())