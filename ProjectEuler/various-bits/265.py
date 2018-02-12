from numpy import *

N = 5;
# We have 2^k digits, including 3 consecutive 0's, bracketed by 1s
# So need place the remaining f(k)=2^k-k-2 points
# f(3) = 3, f(4) = 10, f(5) = 25
#

Bin5 = [ [0,0,0,0,0], [0,0,0,0,1], [0,0,0,1,0], [0,0,0,1,1], 
        [0,0,1,0,0], [0,0,1,0,1], [0,0,1,1,0], [0,0,1,1,1], 
        [0,1,0,0,0], [0,1,0,0,1], [0,1,0,1,0], [0,1,0,1,1],     
        [0,1,1,0,0], [0,1,1,0,1], [0,1,1,1,0], [0,1,1,1,1], 
        [1,0,0,0,0], [1,0,0,0,1], [1,0,0,1,0], [1,0,0,1,1],     
        [1,0,1,0,0], [1,0,1,0,1], [1,0,1,1,0], [1,0,1,1,1],     
        [1,1,0,0,0], [1,1,0,0,1], [1,1,0,1,0], [1,1,0,1,1], 
        [1,1,1,0,0], [1,1,1,0,1], [1,1,1,1,0], [1,1,1,1,1] ];

Bin3 = [ [0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1]];


def val(l):
    R = 0;
    for k in range(N-1, -1, -1):
        R += l[k]*2**k;
    return R;

def Check(nums):
    Start = [0]*N+[1];          End = [1]+[0]*N;

    Data = Start;
    for e in nums:
        Data += Bin5[e];
    Data += End;

    Hits = [0]*2**N;
    for e in range(len(Data)-2*N):
        Hits[ val(Data[e:e+N]) ] += 1;

    if max(Hits) == 1:
        if (len(nums) == 5):
            print nums,
            Hits = [0]*2**N;
            for e in range(2**N):
                Hits[ val(Data[e:e+N]) ] += 1;
            print max(Hits) == 1,;
            print Data[0:2**N];
#            print Data[0:2**N];
        return 1;
    return 0;

for a in range(32):
    for b in range(32):
        if Check([a,b]) >= 1:
            for c in range(32):
                for d in range(32):
                    for e in range(32):
                        Check([a,b,c,d,e]);
