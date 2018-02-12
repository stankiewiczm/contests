from Numeric import *

LENGTH = 9;    TOT = 0;        SEQS = [];

for lgh in arange(3,6):
    for a in arange(2**lgh):
        A = a;      sq = [];
        for b in arange(lgh):
            if (A%2 == 1):
                sq.append(3);
            else:
                sq.append(2);
            A = A/2;
        if (sum(sq)== LENGTH):
            SEQS.append(sq);
            TOT += 1;
print TOT;
            

def CrkFree(Sq1, Sq2):
    Used = zeros(LENGTH+1);
    Tot1 = 0;   Tot2 = 0;
    for a in arange(len(Sq1)):
        Tot1 += Sq1[a];
        Used[Tot1] += 1;
    for b in arange(len(Sq2)):
        Tot2 += Sq2[b];
        Used[Tot2] += 1;
    Used[LENGTH] = 1;
    return (max(Used) == 1);
    

FRIEND = [];
for a in arange(TOT):
    FRIEND.append([]);
for a in arange(TOT):
    if (a%100 == 99):
        print a;
    for b in arange(a+1,TOT):
        if CrkFree(SEQS[a], SEQS[b]):
            FRIEND[a].append(b);
            FRIEND[b].append(a);


Counts = [ones(TOT)];
for a in arange(1,10):
    Counts.append([]);
    for b in arange(TOT):
        Counts[a].append(0L);
print 1, sum(Counts[0]);
for layer in arange(1,10):
    for a in arange(TOT):
        for b in FRIEND[a]:
            Counts[layer][a] += Counts[layer-1][b];
    print layer+1, sum(Counts[layer]);            
