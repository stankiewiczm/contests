from Numeric import *

Plist = list();     Plist.append(1);

def P(n):
    if (n < 0):
        return 0;
    else:
        return Plist[n];

def Px(N):
    P0 = 0;
    for k in arange(1,N+1):
        P0 += (-1)**(k+1) * ( P(N-(k*(3*k-1))/2) + P(N-(k*(3*k+1))/2) );

    return P0;


i = 0;
while (Plist[i] % 1000000 != 0):
    i += 1;
    Plist.append(Px(i) % 10000000000);

    if (Plist[i] % 10000 == 0):
        print i, Plist[i], (Plist[i]%1000000 == 0)

    if (i % 500 == 0):
        print i," :("
