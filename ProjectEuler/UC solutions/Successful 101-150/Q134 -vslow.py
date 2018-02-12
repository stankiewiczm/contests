from Numeric import *

MAX = 1000090;    Prime = list();    Prime.append(2);    NP = 0;  
IsP = ones(MAX);        IsP[1] = 0;      

def Gen():
    for i in arange(2,MAX/2):
        IsP[2*i] = 0;
    n = 3;
    NIsP = 1;
    while (n < MAX):
        if (IsP[n] == 1):
            Prime.append(n);
            NIsP += 1;
            for i in arange(2,(MAX-1)/n+1):
                IsP[n*i] = 0;
        n = n+2;
    return NIsP;


def FindS(idx):
    P1 = Prime[idx];
    P2 = Prime[idx+1];
    
    Hull = 10**int(ceil(log10(P1)));    H  = Hull%P2; 
    Del = P2-P1;        Q = (H)%P2;     n = 1;

    TGT = Hull%P2-Del;
    if (TGT <= 0):
        TGT += P2;
        
    Bet = 1;        TR = (Hull-P2)%Hull;
    
    if (P2 < Hull):
        while ( TR != Del ):
            if (TR < Del):
                if (Del % TR == 0):
                    Bet = Bet*(Del/TR);
                    Bet = Bet%Hull
                    return (Bet+1)*P2;
            
            if (TR > P2):
                Bet +=  (TR/P2)
                TR   =  TR-(TR/P2)*P2;
            else:
                TR = TR+Hull-P2;
                Bet += 1;
#            if (TR != (-Bet*P2)%Hull):
#                print "oops", idx, Bet, (-Bet*P2)%Hull, TR

        Bet = Bet%Hull;
        return (Bet+1)*P2;


    while (Q != Del):
        if (Q < Del):
            n += 1;
            Q = (Q+H);
        else:
            n += P2/H;
            Q = (Q+(P2/H)*H)-P2;
    
    return n*Hull+P1        
        
    
NP = Gen();
print "Generated",NP,"primes up to",Prime[NP-1];


Pn = 2;         TOT = long(0);
while (Prime[Pn] <= 1000000):
    TOT += FindS(Pn);
    if (Pn%250 == 0):
        print Pn, Prime[Pn],TOT;
    Pn += 1;
print TOT;
