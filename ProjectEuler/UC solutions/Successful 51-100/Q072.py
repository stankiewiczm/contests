from Numeric import *

ALL = list();            MAX = 1000001;         MAXP = 80000;
Prime = zeros(MAXP);     Prime[0] = 2;          Prime[1] = 3;   
IsP = ones(MAX);         IsP[1] = 0;            NP = 0;  

for i in arange(MAX+1):
    ALL.append(list());



def Gen():
    for i in arange(2,MAX/2):
        IsP[2*i] = 0;
    n = 3;
    NIsP = 1;
    while (n < MAX):
        if (IsP[n] == 1):
            Prime[NIsP] = n;
            NIsP += 1;
            for i in arange(2,(MAX-1)/n+1):
                IsP[n*i] = 0;
        n = n+2;
    return NIsP;
        


def Phi(N):
    PHI = N;
    for i in ALL[N]:
        PHI = (PHI*(i-1))/i;
    if PHI == N:
        PHI = PHI-1;
    return PHI;
        
NP = Gen();
print "Generated"

for i in arange(NP):
    for j in arange(1,int(ceil((MAX+1.)/Prime[i]))):
        ALL[Prime[i]*j].append(Prime[i]);

print "Populated"

NFs = long(0);
for i in arange(1,MAX):
    NFs = NFs + Phi(i);
#    print i, Phi(i);


print NFs;
print "All done"        # Answer:       303963152392
