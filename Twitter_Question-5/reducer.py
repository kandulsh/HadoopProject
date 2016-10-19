#!/usr/bin/env python
import sys
import string
import operator
from collections import defaultdict


d = defaultdict(list)
num_of_tweets={}

for line in sys.stdin:
  (key,val) = line.strip().split('\t')
  d[key].append(int(val))
#for finding what twitter user tweeted the most
for key in d.keys():
  num_of_tweets[key]=len(d[key])
print 'The twitter user who tweeted the most'
for w in sorted(num_of_tweets, key=num_of_tweets.get, reverse=True):
  print '%s\t%s' %(w,num_of_tweets[w])
  break
#for finding the average length of each twitter user  
new_d={}
for key in d.keys():
  avg = sum(d[key])/float(len(d[key]))
  new_d[key]=float(avg)
k=[]
v=[]
for w in sorted(new_d, key=new_d.get, reverse=True):
  k.append(w)
  v.append(new_d[w])
l=len(k)
print 'Top 5 longest tweeters over each average tweet length'
for i in range(5):
  print '%s\t%s' %(k[i],v[i]) 
print 'Bottom 5 tweeters over each average tweet length' 
for i in range(-5,0):
  print '%s\t%s' %(k[i],v[i])
