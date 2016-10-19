#!/usr/bin/env python

import sys
import string
import matplotlib.pyplot as plt

keys=[]
values=[]
for line in sys.stdin:
  words = line.strip().lower().split()
  keys.append(words[0])
  values.append(words[1])


plt.plot(keys,values)
plt.xlabel('Years')
plt.ylabel('Total No of unique words')
plt.title('1gram plot for Years vs Words')
plt.grid(True)
plt.show()
