from visual.graph import *

L = 80000;   Prime = zeros(L);    Prime[0] = 2;   Prime[1] = 3;

NPrime = 2;     N = 3;      IsP = zeros(1001000);   IsP[2] = 1; IsP[3] = 1;


while (N < 1e6-2):
    N = N+2;
    Good = 1;
    for i in arange(min(NPrime,168)):
        if (N % Prime[i] == 0):
            Good = 0;
            break;
    if (Good == 1):
        Prime[NPrime] = N;
        NPrime += 1;
        IsP[N] = 1;

        
print "Total of ",NPrime,"Primes, the last of which is ",Prime[NPrime-1];

Sps = 0;        Max = 0;    Min = 0;    Busy = 1;
while(Sps+Prime[Max] < 1000000):
    Sps = Sps+Prime[Max];
    Max = Max+1;

while (IsP[Sps] == 0):
    print Sps,Min,Max;
    if (Sps+Prime[Max] < 1e6):
        Sps = Sps+Prime[Max];
        Max = Max+1;
    else:
        Sps = Sps-Prime[Min];
        Min = Min+1;

print "Finished on",Sps,"sum of primes from #",Min,"to #",Max,"(",Prime[Min],",",Prime[Max-1],")";
