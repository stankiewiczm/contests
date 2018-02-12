from Numeric import *

C = [[],[(1,1)]];            LIM = 18;       ARR = 4200
for a in arange(LIM-1):
    C.append([]);

#C[1] = [(1,1)];
#TABLE = [];
#for q in arange(ARR):
#    TABLE.append(zeros(ARR));
#TABLE[1][1] = 1;
HASH = zeros(ARR*ARR);      HASH[ARR+1] = 1;        LEN = 1;

def GCD(n1, n2):
    while (n1*n2 != 0):
        if (n1 > n2):
            n1 = n1-(n1/n2)*n2;
        else:
            n2 = n2-(n2/n1)*n1;
    return (n1+n2);

for caps in arange(2,LIM+1):
#    for K in C[caps-1]:
#        C[caps].append(K);
    
    for a in arange(1,caps/2+1):
        for can1 in C[a]:
            for can2 in C[caps-a]:
                N1n = can1[0]*can2[1] + can1[1]*can2[0];
                N1d = can1[1]*can2[1];      GC1 = GCD(N1n, N1d);        
                N1n /= GC1;                 N1d /= GC1;
                
                N2d = can1[0]*can2[1] + can1[1]*can2[0];
                N2n = can1[0]*can2[0];      GC2 = GCD(N2n, N2d);
                N2n /= GC2;                 N2d /= GC2;

                F1 = ARR*N1n + N1d;
                F2 = ARR*N2n + N2d;

#                if TABLE[N1d][N1n] == 0:
#                    TABLE[N1d][N1n] = 1;
                if HASH[F1] == 0:
                    C[caps].append((N1n, N1d));
                    HASH[F1] = 1;
                    LEN += 1;
#                if TABLE[N2d][N2n] == 0:
#                    TABLE[N2d][N2n] = 1;
                if HASH[F2] == 0:
                    C[caps].append((N2n, N2d));
                    HASH[F2] = 1;
                    LEN += 1;
    print caps, len(C[caps]);

print LEN,
print sum(HASH)

#LEN = 0;
#for q in arange(len(TABLE)):
#    LEN += sum(TABLE[q]);
#print LEN;
