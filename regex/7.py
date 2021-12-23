import os
file=open('file.txt','a')
file.write('Hello world\n')
file.close()
file=open('file.txt','r')
print(file.read())
file.close