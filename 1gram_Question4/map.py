#!/usr/bin/env python

import sys
import string
import re

for line in sys.stdin:
  try:
    words = line.strip().lower().translate(None,string.punctuation).split() 
  except:
    pass
   #Calculating number of syllables in each word
  word1=words[0]
  count = 0
  vowels = 'aeiouy'
  word= " ".join(re.findall("[a-zA-Z]+",word1 ))
  
      
  if len(word)>0:
    if word[0] in vowels:
      count +=1
    for index in range(1,len(word)):
      if word[index] in vowels and word[index-1] not in vowels:
        count +=1
    if word.endswith('e'):
      count -= 1
    if word.endswith('le'):
      count+=1
    if count == 0:
      count +=1
	  #Printing year and number of syllables in that year
  print '%s\t%s' % (words[1],count)
 
    
    