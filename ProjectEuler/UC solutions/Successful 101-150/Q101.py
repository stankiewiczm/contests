from Numeric import *

def F(n):
#    return n**3;
    return (n**11+1)/(n+1)


def NewF(N,Pnts):
    Fnext = 0.;
    
    for xi in arange(1,Pnts+1):
        FPart = float(F(xi));
        for xj in arange(1,Pnts+1):
            if (xi != xj):
                FPart = (FPart * (N-xj))/(0.+xi-xj);
        Fnext += FPart;

    return (Fnext);


def PolFit(deg, DATA):
    NewARR = list();
    
    for i in arange(1,deg+2):
        NewARR.append(NewF(i,deg));
        
    if (abs(NewARR[deg] - F(deg+1)) > 1e-6):
        print "Fitting a ",deg-1," degree polynomial, stumbled and got ",NewARR[deg];
        return NewARR[deg];
    else:
        print "Polynomial value predicted correctly"
        return 0;


LIST = [[]];
TOT = 0;
for i in arange(1,11):
    LIST.append(list());
    for j in arange(1,i+1):
        LIST[i].append(F(j));
    TOT += PolFit(i,LIST[i]);
    print "Current total",TOT, "after ",i,"'th appromation\n"
    
print TOT;
