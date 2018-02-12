from visual.graph import *

Prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97];

def Facts(N):
    Pow = zeros(25);
    Fct = 1;
    for i in arange(25):
        while(N%Prime[i] == 0):
            N = N/Prime[i];
            Pow[i] = Pow[i]+1;
        Fct = Fct * (Pow[i]+1);
    if (N != 1):
        Fct = Fct*2;
    return Fct;


for j in arange(1,12500,2):
    f1 = Facts((j+1)/2);
    k1 = Facts(j)*f1;
    k2 = f1*Facts(j+2);
    if (k1 > 500):
        print j,k1;
    if (k2 > 500):
        print j+1,k2;

print "All done";
