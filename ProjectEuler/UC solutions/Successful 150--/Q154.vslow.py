from Numeric import *

LIM = 200000;     Fs = zeros(LIM+1);      Ts = zeros(LIM+1);      TGT = 12;

def Fill():
    for i in arange(LIM+1):
        N = i;      R = 0;
        while N > 0:
            N = N/5;
            R += N;
        Fs[i] = R;

        N = i;      R = 0;
        while N > 0:
            N = N/2;
            R += N;
        Ts[i] = R;


def C(n,i,j,k):
    return Fs[n]-Fs[i]-Fs[j]-Fs[k]


def Zers(n,I,J,K):
    V = 1;
    for a in arange(I):
        V = (n-a)*V / (a+1);
    for a in arange(J):
        V = (n-I-a)*V / (a+1);
    print V%(1000**5);
    if (V%1000000 == 0):
        return 1;
    return 0


def Pyram(N):
    GD = long(0);
    for i in arange((N/3+1),N+1):
        for j in arange((N+1-i)/2, min((N+1-i),i)+1):
            k = N-i-j
            if (i >= j >= k):
                Fives = Fs[N]-Fs[i]-Fs[j]-Fs[k];
                Twos  = Ts[N]-Ts[i]-Ts[j]-Ts[k]
                if (Fives >= TGT):
                    if (Twos >= TGT):
#                        Zers(N,i,j,k)
                        if (i == j) or (i == k) or (j == k):
                            GD += 3;
                        else:
                            GD += 6;
#                        print N, i, j, k, "    ",Fives, Twos, "   ", GD

        if (i % 1000 == 0):
            print "Done i =",i, "subtotal",GD
        
    return GD;


Fill()
print Pyram(LIM);
