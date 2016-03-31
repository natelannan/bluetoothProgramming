import sys
import re

fileIn=open('sample.txt')
fileOut=open('stream.txt','w')
stream=re.compile(r'Rcvd \"(.*)\"')
for line in fileIn:
    foo=stream.search(line)
    if foo:
        fileOut.write(stream.search(line).group(1))
fileIn.close()
fileOut.close()
