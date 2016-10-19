#!/usr/bin/env python

import sys
import string
import json
tweets = []

for line in sys.stdin:
  try: 
    tweets.append(json.loads(line))
  except:
    pass
texts = [tweet['text'] for tweet in tweets]
screen_names = [tweet['user']['screen_name'] for tweet in tweets]
for i in range(len(screen_names)):
  print '%s\t%s' %(screen_names[i],len(texts[i]))
