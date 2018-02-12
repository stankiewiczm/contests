from Numeric import *

def Check(N):
    m = N*N;
    if (m/100)%10 == 8:
        if (m/10000)%10 == 7:
            if (m/1000000)%10 == 6:
                if (m/100000000)%10 == 5:
                    if (m/10000000000)%10 == 4:
                        if (m/1000000000000)%10 == 3:
                            print N*10, m*100;


N0 = 101010103;
N = N0;
while N < 138902662:
    Check(N);
    N += 4;
    Check(N);
    N += 6;
