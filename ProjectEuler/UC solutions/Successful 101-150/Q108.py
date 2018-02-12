from Numeric import *

#Prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97];
#
#def Rad(N):
#    N0 = N;     M0 = 1;
#    for i in arange(25):
#        if (N0 % Prime[i] == 0):
#            M0 = M0*Prime[i];
#    return M0;


def Sols(n):
    SOL = 0;
    for i in arange(n+1,2*n+1):
        if (i*n)%(i-n) == 0:
            SOL += 1;
    return SOL

LIST = list();  i = 420*11;  MX = 0;
while MX < 1000:
    LIST.append(Sols(i));
    if (LIST[len(LIST)-1] > MX):
        MX = LIST[len(LIST)-1];
        print i,i/420/11, MX;
    i += 420;
    
#    if (i%1000 == 0):
#        print i, max(LIST)

