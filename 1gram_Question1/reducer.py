#!/usr/bin/env python

import sys
import string


word_count = 0
old_word = 0


for line in sys.stdin:
  (key,val) = line.strip().split('\t')
  if old_word != key:
    if old_word:
      print '%s\t%d' % ( old_word,word_count)
      word_count = 0
  old_word = key
  try:
    word_count = word_count + int(val)
  except:
    continue
print '%s\t%d' % (old_word,word_count)



