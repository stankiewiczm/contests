from Numeric import *

F = [1,1,2,6,24,120,720,5040,40320,362880,3628800];       D = zeros(10);
Z = [2,3,5,7,11,13,17];

ENDS = [53901,52867,57289];

ANS = [1430952867, 4130952867, 1460357289, 4160357289, 1406357289, 4106357289];


def Ok(b):
    for i in arange(len(Z)):
        A = (b/(10**(6-i))) % 1000;
        if (A%Z[i] != 0):
            return 0;
    return 1;
    

for i in arange(3):
    N = ENDS[i]/1000;
    for j in arange(10):
        if ((100*j+N) % 7 == 0):
            print j,ENDS[i];


for i in arange(6):
    print ANS[i], Ok(ANS[i]);

print "\n",sum(ANS);
