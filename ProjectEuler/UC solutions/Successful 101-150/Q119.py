from Numeric import *

def SDig(N):
    SD = 0;     N0 = N;
    while (N0 > 0):
        SD += N0%10;
        N0 = N0/10;
    return SD;

LIST = list();      LIST.append(0);
for i in arange(2,100):
    for j in arange(1,50):
        IJ = i**j
        if (IJ < 1e15) and (IJ > 9):
            if SDig(i**j) == i:
                LIST.append(IJ)

SLIST = sort(LIST);

print len(SLIST), SLIST[2], SLIST[10],SLIST[30]
print "All done"
    
