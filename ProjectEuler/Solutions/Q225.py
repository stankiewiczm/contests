def Check(n0):
    for q in BADL:
        if n0%q == 0:
            return True;
    
    TL = [1,1,1];
    a = 0;
    while (a < 32000):
        N =  (TL[-1]+TL[-2]+TL[-3])%n0 ;
        if (N == 0):
            return False;
        TL.append(N);
        a += 1;
    return True;

#######################################

k = 1;      BADL = [];
while len(BADL) < 124:
    k += 2;
    if Check(k):
        BADL.append(k);

print BADL[123]
