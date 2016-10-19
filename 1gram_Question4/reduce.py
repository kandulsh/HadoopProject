#!/usr/bin/env python

import sys
import string

word_count = 0
old_word = 0
syl_avg=0
syl_count=0
keys=[]
values=[]

for line in sys.stdin:
  (key,val) = line.strip().split('\t')
  
  if old_word != key:
    if old_word:
	#Printing year, number of syllables and number of words in that year
      print '%s\t%s\t%s' % ( old_word,syl_count,word_count)
      syl_count=0
      word_count = 0
  old_word = key
  #Calculating number of syllables and number of words in each year
  try:
    syl_count=syl_count+int(val)
    word_count = word_count + 1
    
  except:
    continue
#Printing last year, number of syllables and number of words in that year
print '%s\t%s\t%s' % (old_word,syl_count,word_count)



