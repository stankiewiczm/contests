from numpy import *

FILE = open("B-large.in","r");

N = int(FILE.readline());
for k in range(N):          # Each of the N cases:
    words = FILE.readline().split();
    print "Case #%d: " % (k+1),
    for l in range(len(words)-1, -1, -1):
        print words[l],
    print "";


