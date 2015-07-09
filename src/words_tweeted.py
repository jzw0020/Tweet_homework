import sys
a=sys.path[0]
d=a.rfind('src')
b=a[:d]
tweettxt=open(b+'tweet_input\\tweets.txt', 'r')
tweet=tweettxt.read()  
ft1=open(b+'tweet_output\\ft1.txt','w')
from collections import Counter
wordcount = Counter(tweet.split())

for key,value in sorted(wordcount.items()):
    ft1.write(u'{} {}\n'.format(key, value))
