tweettxt=open('tweets.txt','r')
tweet=tweettxt.read()  
ft1=open('ft1.txt','w')
from collections import Counter
wordcount = Counter(tweet.split())

for key,value in sorted(wordcount.items()):
    ft1.write(u'{} {}\n'.format(key, value))
