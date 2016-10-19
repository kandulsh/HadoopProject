#!/usr/bin/env python

import sys
import string


for line in sys.stdin:
  words = line.strip().lower().split()
  print '%s\t%s' % (words[1],1)
