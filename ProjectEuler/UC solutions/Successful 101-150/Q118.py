from Numeric import *

PANS = list();      MAX = 1000001;      SEQS = [[],[],[],[],[],[],[],[],[],[]];
Prime = [2];    NP = 0;             IsP = ones(MAX);        IsP[1] = 0;
POW = [1,10,100,1000,10000,100000,1000000,10000000,100000000];

################ CREATION OF PANDIGITALS ###################

def PanGenerate():
    TOT = 0;
    for a1 in arange(1,10):
        for a2 in arange(1,10):
            for a3 in arange(1,10):
                for a4 in arange(1,10):

                    if (a1 != a2 != a3 != a4):
                        if (a3 != a1 != a4 != a2):
                            START = 1000*a1+100*a2+10*a3+a4;

                            LIST = [1,2,3,4,5,6,7,8,9];   p = 0;
                            while (p < len(LIST)):
                                if LIST[p] in [a1,a2,a3,a4]:
                                    LIST.pop(p);
                                else:
                                    p += 1;

                            for b1 in LIST:
                                for b2 in LIST:
                                    for b3 in LIST:
                                        for b4 in LIST:
                                            if (b1 != b2 != b3 != b4):
                                                if (b3 != b1 != b4 != b2):
                                                    END = 1000*b1+100*b2+10*b3+b4;
                                                    c = 45-(a1+a2+a3+a4+b1+b2+b3+b4);
                                                    PANS.append(START*100000+END*10+c);
                                                    TOT += 1
    print TOT;               

################ CREATION OF PRIME TABLE ###################

def PrimeGen():
    for i in arange(2,MAX/2):
        IsP[2*i] = 0;
    IsP[0] = 1;
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
        

################# CHECKING FOR PRIMENESS ###################

def CheckP(N0):
    mx = int(sqrt(N0))+2;
    i = 0;
    while (Prime[i]  < mx):
        if N0%Prime[i] == 0:
            return Prime[i];
        i += 1;
    return 0;


def SeqGen():
    for a in arange(10):
        for b in arange(min(a+1,10-a)):
            for c in arange(min(b+1,10-a-b)):
                for d in arange(min(c+1,10-a-b-c)):
                    for e in arange(min(d+1,10-a-b-c-d)):
                        f = 9-a-b-c-d-e;
                        if (f <= e):
#                            print [a,b,c,d,e,f]
                            SEQS[a].append([b,c,d,e,f]);


def NSort(K):
    return True;

NP = PrimeGen();
PanGenerate();
SeqGen();

print "Generated..."

PPs = zeros(6);     REM = 0;    N = 10;          # Perhaps primes
SOLS = 0;       ANS = zeros(9);

for i in arange(len(PANS)):
    pan = PANS[i];
    REM = pan;
    for j in arange(1,9):
        N = 9-j;
        PPs[0] = pan/POW[N];        REM = pan%POW[N];       N = 9-j;

        # AM DOUBLE-COUNTING REM non-sort;
        
        if (CheckP(PPs[0]) == 0) and (NSort(REM)):
            for seq in SEQS[j]:
                N = 9-j;            REM = pan%POW[N];
                
                for t in arange(5):
                    N = N-seq[t];
                    PPs[1+t] = REM/POW[N];
                    REM      = REM%POW[N];

                if (IsP[PPs[1]] and IsP[PPs[2]] and IsP[PPs[3]] and IsP[PPs[4]] and IsP[PPs[5]]):
                    if (PPs[0] >= PPs[1] >= PPs[2] >= PPs[3] >= PPs[4] >= PPs[5]):
                        SOLS += 1;
                        ANS[j] += 1;
            
print SOLS, ANS
        
        
        


