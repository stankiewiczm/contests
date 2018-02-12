from Numeric import *

Mx = 1000001;     Lens = zeros(Mx);

def Itr(n):
    if (n%2 == 0):
        return n/2;
    else:
        return 3*n+1;

def Collatz(N):
    Cnt = 1;
    N0 = N;
    while (N >= N0):
        N = Itr(N);
        Cnt = Cnt+1;
    Cnt = Cnt + Lens[N]-1;
    return Cnt;

Moi = 0;    Mox = 0;

Lens[1] = 1;     Lens[2] = 2;
for i in arange(3,Mx):
    Lens[i] = Collatz(i);
    if Lens[i] > Mox:
        Mox = Lens[i];
        Moi = i;
print max(Lens), Mox, Moi;
        
