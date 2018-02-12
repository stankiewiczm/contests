from numpy import *

def Rev(n):
    s = str(n);     s2 = '';
    for k in range(len(s)-1,-1,-1):
        s2 += s[k];
    return int(s2);


def IsLych(n):
    for i in range(100):
        n += Rev(n);
        if (n == Rev(n)):
            return 0;
        
    return 1;

ANS = 0;
for q in range(10000):
    ANS += IsLych(q);
print ANS;
