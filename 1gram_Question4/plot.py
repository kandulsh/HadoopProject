#!/usr/bin/env python

import sys
import string
import re
import matplotlib.pyplot as plt

years1=[]
syl_a=[]

for line in sys.stdin:
  (year,syl,wc) = line.strip().split('\t',2)
  years1.append(int(year))
  syl_avg= float(float(syl)/float(wc)) 
  syl_a.append(syl_avg)
 
plt.plot(years1,syl_a)
plt.show()