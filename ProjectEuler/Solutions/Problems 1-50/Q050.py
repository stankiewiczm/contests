from numpy import *

LIM = 10**6;    P = [];     IsP = ones(LIM+1, bool);        IsP[1] = 0;
for n in range(2,LIM):
    if IsP[n]:
        P.append(n);
        for i in range(n, LIM/n+1):
            IsP[n*i] = False;

print "Generated",len(P),"primes";



MAX = 0;        nMAX = 0;       FIN = False;
S = zeros(601,int);             k = 0;

for k in range(600):
    k += 1;
    S[k] = S[k-1]+P[k-1];


for L in range(546,-1,-1):
    start = 0;
    while (S[L+start]-S[start] < LIM):
        FIN = IsP[S[L+start]-S[start]];
        if FIN:
            print S[L+start]-S[start], L;
            break;
        start += 1;
        
    if FIN:
        break;
    

