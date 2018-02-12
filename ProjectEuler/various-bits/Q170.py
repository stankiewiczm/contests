from Numeric import *

PANS = list();      MAX = 1000001;      SEQS = [[],[],[],[],[],[],[],[],[],[]];
Prime = [2];    NP = 0;             IsP = ones(MAX);        IsP[1] = 0;
POW = [1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000];

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



def Verify(N, SQNC):
    seq = SQNC;
    Mseq = [];
    for i in arange(len(seq)):
        Mseq.append(N*seq[i]);

    D = zeros(10);      MD = zeros(10);
    while N > 0:
        D[N%10] += 1;
        N = N/10;

    for i in arange(len(seq)):
        while (seq[i] > 0):
            D[seq[i]%10] += 1;
            seq[i] = seq[i]/10;

    if (sum(D) != 10) or (max(D) != 1):
        return False
    
    for i in arange(len(Mseq)):
        while (Mseq[i] > 0):
            MD[Mseq[i]%10] += 1;
            Mseq[i] = Mseq[i]/10;

    if (sum(MD) != 10) or (max(MD) != 1):
        return False
                
    return True;

#NP = PrimeGen();
PanGenerate();

print "Generated..."

