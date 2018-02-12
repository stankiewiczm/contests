from Numeric import *

def Rev(N):
    R = 0;      STR = str(N);    
    for i in arange(len(STR)):
        R += 10**(int(i))*int(STR[i])
    return R;


def Lych(n):
    C = 0;
    n = n+Rev(n);
    while (C < 50):
        C = C+1;
        R = Rev(n);
        if (n == R):
            return C;
        else:
            n += R;
    return 0;

LL = list();
for i in arange(10000):
    if (Lych(i) == 0):
        LL.append(i);

print LL, len(LL)
