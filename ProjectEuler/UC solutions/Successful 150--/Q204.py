from Numeric import *

P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97];

LIST = [1];
LIM = 1000000001;

for p in P:
    NL = [];    
    for l in LIST:
        n = p*l;
        while n < LIM:
            NL.append(n);
            n = n*p;
    for nl in NL:
        LIST.append(nl);
    print p, len(LIST)

print len(LIST);
    
