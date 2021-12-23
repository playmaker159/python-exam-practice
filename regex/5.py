#substuite
import re
regex=re.compile(r'Agent \w+',re.I)
print(regex.sub('SECRET','agent ashwin is a good buoy'))