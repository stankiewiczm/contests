from Numeric import *

MAX = 1000000;    ARR = ones(MAX+1);  ARR[1] = 1;

for j in arange(2,MAX):
    for i in arange(2,MAX/j+1):
        ARR[j*i] = ARR[j*i]+j;


def Check():
    Tot = 0;
    for i in arange(1,MAX):
        Len = 1;
        I = ARR[i];
        LIST = list([0]);     LIST.append(1);
        while (I != i) and (I < MAX) and (I not in LIST):
            LIST.append(I);
            I = ARR[I];
            Len += 1;
        if (LEN > 20):
            if (I == i):
                print i, Len;


print ARR[220];
Check()
