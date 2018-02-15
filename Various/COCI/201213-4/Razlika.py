[N,K] = map(int, raw_input().split());
L = N-K;
V = map(int, raw_input().split());
V.sort()
diff = [0]*(N-1);
for i in range(N-1):
    diff[i] = V[i+1]-V[i];

Seq = diff[0:N-K-1];
Seq.sort();
#print Seq;
Arrm = [Seq[0]];


for i in range(1,K):
    if diff[N-K-1+i] <= Arrm[i-1]:
        Arrm.append ( diff[N-K-1+i] );
    else:
        if diff[i-1] == Arrm[i-1]:
            Arrm.append ( min(diff[i:N-K+i]) );
        else:
            Arrm.append( Arrm[i-1] );
Arrm.append( min(diff[K:N]) );


# Now need to take K consecutive elements -- [0-L-1] up to [K:N-1]
M = 10**6;
m = 10**6;

for i in range(K+1):
    M0 = V[L-1+i]-V[i];
    m0 = min( diff[i:i+N-K] );
#    print m0,
    if M+m > M0+m0:
        M = M0;
        m = m0
#print Arrm

print M+m
