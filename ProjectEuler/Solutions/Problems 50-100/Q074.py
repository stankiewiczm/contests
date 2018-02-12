from numpy import *

F = [1,1,2,6,24,120,720,5040,40320,362880];     LIM = 10**6;
FIN = [];

def SF(n):
    R = 0;      SN = str(n);
    for c in SN:
        R += F[int(c)];
    return R;

def Meth1(n):
    k = SF(n);      c = 2;      l = [n,k];
    while (SF(k) not in l):
        k = SF(k);
        l.append(k);
        c += 1;
    if SF(k) not in FIN:
        FIN.append(SF(k));
    return c;

def Meth3(n0):
    c = 0;      n = n0;     TODO = [];
    while (Uq[n] == 0):
        TODO.append(n);
        n = SF(n);
        c += 1;
    Val = Uq[n];
    while (len(TODO) != 0):
        Uq[TODO[-1]] = Val+1;
        Val += 1;
        TODO.remove(TODO[-1]);
    return;


ANS = 0;        Uq = zeros(2200000,int);
Uq[1] = 1;      Uq[2] = 1;          Uq[145] = 1;    Uq[40585] = 1;
Uq[169] = 3;    Uq[363601] = 3;     Uq[1454] = 3;   
Uq[871] = 2;    Uq[45361] = 2;      Uq[872] = 2;    Uq[45362] = 2;

for n in range(1,LIM+1):
    if Uq[n] == 0:
        Meth3(n);

print sum(Uq[0:LIM] == 60)
