from Numeric import *

P = [2,3,7,11,13,17,19];

Rem = [1,3,7,9,13,27];          Safes = 0;

NLIM = 3*7*13;

for i in arange(NLIM):
    N = 10*i;
    Good = 1;
    for j in arange(6):
        if (Good == 1):
            for k in arange(0,6):
                if ((N*N+Rem[j]) % P[k] == 0):
#                    print N, N*N+Rem[j], P[k];
                    Good = 0;
                    break;
    if (Good == 1):
        print "The case ",N," is good"
        Safes = Safes+1;

print "\n\n",Safes,"/",NLIM,float(Safes)/NLIM;


# Mod 3:   1 or 2       0               eliminated
# Mod 7:   1 or 6       0,2,3,4,5       elliminated
# Mod 11:               2,3,8,9         elliminated
# Mod 13:               0,2,5,6,7,8,11  elliminated
# Mod 17:               3,7,8,9,10,14   elliminated
# Mod 19:               5,8,9,10,11,14  elliminated


