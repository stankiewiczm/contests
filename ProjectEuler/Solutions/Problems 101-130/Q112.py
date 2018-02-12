def BCheck(n):
    Inc = False;      Dec = False;
    ns = str(n);
    for i in range(1,len(ns)):
        if ns[i] > ns[i-1]:
            Inc = True;
        if ns[i] < ns[i-1]:
            Dec = True;
    return (Inc and Dec)


NBounce = 0;        NTot = 100;
while (99*NTot != 100*NBounce):
    NTot += 1;
    NBounce += BCheck(NTot);
print NTot #, NBounce
