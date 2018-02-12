from numpy import *
from RandomArray import *

Happy = zeros(60);
for k in range(1,60):
    n = k;
    for l in range(100):
        n = (n%10)**2 + ((n/10)%10)**2 + (n/100)**2;
    if n == 1:
        Happy[k] = 1;


F = [1,1,2,6,24,120,720,5040,40320,362880,3628800,39916800];

def Iterate():
    HITS= zeros(60,int);
    DIG = [1,2,3,4,5,6,7,8,9,10,11,12];
    n = zeros(12, int);
    for k in range(12):
        R = random();
        n[k] = DIG.pop( int((12-k)*R) );
    
    HITS[n[0]] += 1;
    HITS[n[1]+n[2]+n[3]+n[4]+n[5]] += 1;
    HITS[n[6]+n[7]+n[8]+n[9]] += 1;
    HITS[n[10]+n[11]] += 1;

    HITS[n[1]+n[6]] += 1;
    HITS[n[0]+n[2]+n[7]+n[10]] += 1
    HITS[n[3]+n[8]+n[11]] += 1;
    HITS[n[4]+n[9]] += 1;
    HITS[n[5]] += 1;

    TOT = HITS[1]+HITS[7]+HITS[10]+HITS[13]+HITS[19]+HITS[23]+HITS[28]+HITS[31]+HITS[32]+HITS[44]+HITS[49];
    if (TOT >= 2):
        return 1;
    return 0;

TOTAL = 0;
for cnt in range(1,50000000+1):
    TOTAL += Iterate();
    if cnt%25000 == 0:
        print cnt, TOTAL, "  ", float(TOTAL)/cnt
    
