from numpy import *

LIM = 2200;

def CheckP(pn):
    f = 0.5+sqrt(6*pn+0.25);
#    print f/3, int(f)/3, ;
    return abs(f/3-int(f)/3) < 1e-6;


def GiveP(n):
    return (n*(3*n-1))/2;


for n1 in range(1,LIM):
    P1 = GiveP(n1);
    for n2 in range(n1+1, LIM):
        P2 = GiveP(n2);
        
        if CheckP(P2-P1):
            if CheckP(P1+P2):
                print (n1, n2), P1, P2, P2-P1;
                print "FIN";
