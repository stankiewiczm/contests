L = int(raw_input());
N = int(raw_input());
People = []
Expect = []
Get    = [];
Log = [1]*(L+1)
for i in range(N):
    [P,K] = map(int, raw_input().split());
    Expect.append( K-P+1 );
    Get.append( sum(Log[P:K]) );
    for i in range(P, K+1):
        Log[i] = 0;

print Expect.index(max(Expect))+1,'\n', Get.index(max(Get))+1;
