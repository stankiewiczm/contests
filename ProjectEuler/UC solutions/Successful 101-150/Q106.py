from Numeric import *

N = 12;     L = [];     FRQ = zeros(N+1);     BITL = [];   T = 0;    

for a in arange(N+1):
    BITL.append([]);

for a in arange(1,2**N):
    s = [];
    for b in arange(N):
        s.append(a%2);
        a = a/2;
    L.append(s);
    FRQ[sum(s)] += 1;
    BITL[sum(s)].append(s);

########################################################

def Compare(s1,s2):
    for q in arange(N):           # Ensure that the sets are disjoint
        if s1[q]+s2[q] == 2:
            return 0;

    S = 0;
    for q in arange(N):
        S += s1[q] - s2[q];         # The sequences are not in direct order
        if (S > 0):
            return 1;               # Sequence not clear, to be checked
        
    return 0;


for n in arange(1,N/2+1):
    for a in arange(len(BITL[n])):
        for b in arange(a):
            T += Compare(BITL[n][a],BITL[n][b]);

print "Total of ",T,"disjoint subset pairs found, of same sizes";
