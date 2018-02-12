from Numeric import *
from time import *

p = 1009;       q = 3643;
N = p*q;        Phi = (p-1)*(q-1)       # Phi = 32 * 27 * 7 * 607

e1 = 7;     e2 = 5;     eLIST = [];
while (e2 < Phi):
    if (e2%7 != 0) and (e2%607 != 0):
        eLIST.append(e2);
    e2 += 6;    

while (e1 < Phi):
    if (e1%7 != 0) and (e1%607 != 0):
        eLIST.append(e1);
    e1 += 6;    

print "Starting"


def FindPeriod(m0,MOD):
    L = [m0, (m0**607)%MOD];           EXP = [1, 607];      MN = []

    for k in range(2):
        L.append( (L[k]**7)%MOD );          # Add powers of 7
        EXP.append( EXP[k]*7 );

    for k in range(4):
        for b in range(1,4):                # Add powers of 3;
            L.append( (L[k]**(3**b))%MOD );
            EXP.append( EXP[k]*(3**b) );

    for k in range(16):
        for a in range(1,6):
            L.append( (L[k]**(2**a))%MOD );     # Add powers of 2;
            EXP.append( EXP[k]*(2**a) );

    for k in range(1,96):
        if (m0*L[k])%MOD == m0:
            MN.append(EXP[k]);

#    print m0, min(MN), "  "  , MN;

    
    return min(MN);

    
#########################################################
####   Created a list of all the e values to check   ####
#### List contains 1047167 distinct values up to Phi ####

t0  = time();       BADS = zeros(N);    # BADS: number of bad m's for each e
for m in range(2,N):
    if m%10000 == 0:
        print m, time()-t0
    D = FindPeriod(m,N);

    q = 1;
    while q < N:
        BADS[q] += 1;                   # Add a faulty m.
        q += D;

print "Seeded the lot in ",time()-t0;

MIN = 2*N;          NUM = 0;        TOT = 0L;
for e in eLIST:
    if BADS[e] < MIN:
        MIN = BADS[e]; 
for e in eLIST:
    if (BADS[e] == MIN):
        NUM += 1;           TOT += e;

print MIN,"occurs",NUM,"times with sum", TOT


#Seeded the lot in  3908.3670001
#7 occurs 217800 times with sum 399788195976
