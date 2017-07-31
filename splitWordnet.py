#!/usr/bin/python
import sys
import csv

filename = sys.argv[1]
f = open(filename,'r')
lines = csv.reader(f)

splitFilename = "splitFiles/block"
c=0
b=0

splitFile = open(splitFilename+str(c),'w')

for line in f:
   if line[0] == ";":
      splitFile.close()
      c=c+1
      splitFile = open(splitFilename+str(c),'w')
   else:
      splitFile.write(line)
      b=b+1


f.close()
splitFile.close()

print "# of blocks: " + str(c) + " ---- # of lines: " + str(b)
sys.stdout.flush()

