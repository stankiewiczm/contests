from Numeric import *

Prime = zeros(2001);    Prime[0] = 2;   Prime[1] = 3;
Pcheck = zeros(17394);  # The 1+prime labelled 2000;

def Generate():
    N = 3;
    NPrime = 2;
    while(NPrime < 2001):
        N = N+2;
        Good = 1;
        for i in arange(NPrime):
            if (N%Prime[i] == 0):
                Good = 0;
                break;
        if (Good == 1):
            Prime[NPrime] = N;
            NPrime = NPrime + 1;

    for i in arange(NPrime):
        Pcheck[Prime[i]] = 1;

  
def List(a,b):
    for n in arange(100):
        Fn = n*n+a*n+b;
        if (Fn < 1):
            return n;
        if (Pcheck[Fn] == 0):
            return n;

Generate();

MAX = 0;    T = 0;  A = 0;  B = 0;
print "Starting"
for i in arange(-999,1000):
    for j in arange(168):    #168 for 1000;
        T = List(i,Prime[j]);
        if (T > MAX):
            MAX = T;
            A = i;
            B = j;

print "Done:", A,Prime[B],MAX;
print "Product",A*Prime[B];
