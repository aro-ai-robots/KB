#!/usr/bin/python
import sys
import csv
import re

splitFilename = sys.argv[2]+".txt"
delimiters = [',', '?', '!', ':', '.']

filename = sys.argv[1]
f = open(filename,'r')
words = f.readlines()

new_words= []
for word in words:
   new_words += word.split()
words = new_words

new_words = []
for delimiter in delimiters:
   for word in words:
      if word.endswith(delimiter):
         new_words.append(word[:-1])
      else:
         new_words.append(word)

f.close()
f = open(splitFilename,'w')

for new_word in new_words:
   f.write(new_word + "\n")

f.close()
