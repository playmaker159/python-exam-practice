#repititions
import re
regex=re.compile(r'(lol){3,5}?')
searchobj=regex.search(input())
print(searchobj.group())