from numpy import *

def Sort(n):
    R = 0;      L = [];
    while (n > 0):
        L.append(n%10);     n /= 10;
    L = sort(L);
    for k in range(len(L)):
        R = 10*R+L[k];
    return R;

    
def Best(n1, n2):
    L3 = [];        Target = [];

    for n in range(n1, n2+1):
        L3.append(Sort(n**3));
    L3 = sort(L3);
    for i in range(4, len(L3)):
        if L3[i] == L3[i-4]:
            Target.append(L3[i]);

#    print Target
    for n in range(n1, n2):
        if Sort(n**3) in Target:
             print n, n**3;
             return n;
    
    return -1;
        


ND = 8;
while (ND < 18):
    nlow = int((10**ND/10)**(1./3))+1;
    nhigh= int((10**ND)**(1./3));
    if Best(nlow, nhigh) >= 0:
        break;
    ND += 1;
