import sys
a=sys.path[0]
d=a.rfind('src')
b=a[:d]
import numpy
def median(lst):
    return round(numpy.median(numpy.array(lst)),2)
num_lines=0
num_words=0
num_chars=0
array = []
ft2=open(b+'tweet_output\\ft2.txt','w')
with open(b+'tweet_input\\tweets.txt', 'r') as f:
    for line in f:
        words = set(line.split())
        num_lines += 1
        num_words = len(words)
        num_chars += len(line)
        array.append(num_words)
        ft2.write(u'{}\n'.format(str(median(array))))
