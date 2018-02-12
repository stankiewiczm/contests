from Numeric import *;

def Func(a,b,mult):
    return b,a+mult*b;


N = long(1);
D = long(1);
print N,D

for f in arange(98,0,-1):
    if (f%3 == 2):
        (N,D) = Func(N,D,2*(f+1)/3);
    else:
        (N,D) = Func(N,D,1)
print 2*D+N,D

N = 2*D+N;      S = 0;

while ( N > 0 ):
    S = S+N%10;
    N = N/10;

print S;

    
