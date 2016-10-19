#!/usr/bin/env python
import sys
import string
from collections import defaultdict
#import matplotlib.pyplot as plt


d = defaultdict(list)
a=[]
for line in sys.stdin:
  (key,val) = line.strip().split('\t')
  d[key].append(int(val))
new_d={}
for key in d.keys():
  avg = sum(d[key])/float(len(d[key]))
  new_d[key]=float(avg)
  if (key == "PrezOno"):
    continue
  else:
    a.append(float(avg))    
other_avg = sum(a)/float((len(d)-1))
prez_avg = new_d['PrezOno']
print 'PrezOno average tweet length: %s' %(prez_avg)
print 'Others average tweet length: %s' %(other_avg)
  
