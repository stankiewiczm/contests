def Rebase(n,base, case):
    Var = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a','b','c','d','e','f'];
    Ret = '';
    SN = 0;
    while n > 0:
        SN += n%base;
        c = Var[n%base];
        Ret = c + Ret;
        n /= base;
    if case:
        return SN    
    return Ret


#def Check(mod, base):
#    MOD = base**mod;
#    for i in range(MOD/base, MOD):
#        if i*(i-1)%MOD == 0:
#            print (mod, base), i, Rebase(i, base);

def Ver(n, mod):
    return n*(n-1)%mod == 0;


L = [7,8];      base = 14;      mod = 1;      TOT = sum(L)+1

for n in range(2,10001):
    if (n%100 == 0):
        print n
    next = base**(n-1);     MOD = base**n;
    for q in range(len(L)):
        for d in range(base):
            e = L[q];
            if Ver(next*d+e, MOD):
                L[q] += next*d
                if d != 0:
                    TOT += Rebase(next*d+e, base, True)

print Rebase(TOT,14, False)
