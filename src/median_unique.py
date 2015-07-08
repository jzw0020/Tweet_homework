import numpy
def median(lst):
    return numpy.median(numpy.array(lst))
num_lines=0
num_words=0
num_chars=0
i = 0
array = []
ft2=open('ft2.txt','w')
with open(r'c:\users\jing\onedrive\cpython-ms\tweet\tweets.txt', 'r') as f:
    for line in f:
        words = set(line.split())
        i +=1
        num_lines += 1
        num_words = len(words)
        num_chars += len(line)
        array.append(num_words)
        ft2.write(u'{}\n'.format(str(median(array))))
