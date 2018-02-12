from numpy import *

FILE = open("B-small-2.in","r");


def Solve2(DATA):
   Diff = abs(DATA[0]-DATA[1]);
   ANS = [D];
   ANS.append(max(0,Diff-M));
   if (M > 0):
       if ((Diff-1)/M >= 0):
           ANS.append(I*((Diff-2)/M+1));
   return min(ANS);
        

def Solve3(DATA):
    D01 = Solve2([DATA[0], DATA[1]]);
    D02 = Solve2([DATA[0], DATA[2]]);
    D12 = Solve2([DATA[1], DATA[2]]);
    return min( D02 + D, D01+D12 );#, D02+D01, D02+D12);


T = int(FILE.readline());
for k in range(T):          # Each of the N cases:
    print "Case #%d:" %(k+1),
    [D,I,M,N] = map( int, FILE.readline().split() );
    DATA = map(int, FILE.readline().split());

#    print (D,I,M), DATA,
    if (N == 1):
        print 0;

    if (N == 2):
        print Solve2(DATA);

    if (N == 3):
        print Solve3(DATA);
        
