#fileSize
import os
fileSize=0
for filename in os.listdir('F:\CodeBlocks'):
    fileSize+=os.path.getsize(os.path.join('F:\CodeBlocks',filename))
print(fileSize)