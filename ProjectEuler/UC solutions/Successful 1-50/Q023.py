from Numeric import *

Prime = zeros(200);    Prime[0] = 2;   Prime[1] = 3; AMAX = 10000;
Abund = zeros(AMAX);  CanDo = zeros(30000);     Cants = [];    

def Generate():
    N = 3;
    NPrime = 2;
    while(NPrime < 200):
        N = N+2;
        Good = 1;
        for i in arange(NPrime):
            if (N%Prime[i] == 0):
                Good = 0;
                break;
        if (Good == 1):
            Prime[NPrime] = N;
            NPrime = NPrime + 1;
    return 0;
            

def CheckAbund(N):
    N0 = N;     P = 1;      Facts = ones(200);
    
    for i in arange(200):
        Cnt = 0;
        while (N%Prime[i] == 0):
            N = N/Prime[i];
            Cnt += 1;
            Facts[i] += Prime[i]**Cnt;
    for i in arange(200):
        P = P*Facts[i];
            
    return P;


def GenAbunds():
    NAbund = 0;
    for i in arange(1,30000):
        if (CheckAbund(i) > 2*i):
            Abund[NAbund] = i;
            NAbund += 1;
    print "There are this many abundants",NAbund;
    return NAbund;


def Check(NA):
    for i in arange(NA):
        for j in arange(NA):
            Nim = Abund[i] + Abund[j];
            if ( Nim < 30000):
                CanDo[Nim] = Nim;
            else:
                break;

    Bads = 0;   Sum = 0;
    for i in arange(30000):
        if (CanDo[i] == 0):
            Cants.append(i);
    print "There are ",len(Cants),"unatainables, with sum",sum(Cants);

Generate();
Check(GenAbunds());
