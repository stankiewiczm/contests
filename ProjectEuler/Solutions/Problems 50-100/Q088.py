from numpy import *

kLim = 12000+1;             nLim = 2*kLim-1;
MIN = zeros(kLim,int);      Val = [];           

def prod(l):
    R = 1;
    for e in l:
        R *= e;
    return R;


def EvalProd():
    for k in range(15):
        Val.append([]);
    for k in range(2,kLim):
        MIN[k] = 10**6;

    for a in range(2,156):
        b = a*a;    
        while (b <= nLim):
            Val[2].append([a,b/a]);
            b += a;

    print 2, len(Val[2]);
    for n in range(3,15):
        print n, ;
        for e in Val[n-1]:
            p = prod(e);        l = e[-1];
            while (p*l < nLim):
                Val[n].append(e+[l]);
                l += 1;
        print len(Val[n]);


def FillMinima():
    for n in range(2,15):
        for e in Val[n]:
            p = prod(e);        
            kLen = p-sum(e)+n;        # Total number of elements
            if (kLen < kLim):
                if MIN[kLen] > p:
                    MIN[kLen] = p;
    return
    

def FindAns():
    SET = zeros(nLim,int);
    for m in range(2,kLim):
        SET[MIN[m]] = MIN[m];
    return sum(SET);

    
EvalProd();         
FillMinima();       
print FindAns();
