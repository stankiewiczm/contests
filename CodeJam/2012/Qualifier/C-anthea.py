from numpy import*

## code jam 2012, question C.

filename = "C-large.in"
FILE = open(filename, "r")
N = int(FILE.readline())

for k in range(N):
    T = map(int, FILE.readline().split())
    A = T[0]
    B = T[1]
    pairs = []
    for n in range(A,B+1):
        N = str(n)
        Bs = str(B)
        for i in range(1,len(str(A))):
            m = str(n)
            #print m
            m = m[i:]+m[:i]
            #print m
            if (m > N)&(m <= Bs):
                possible = 1
                for l in pairs:
                    if (m == l[1])&(n == l[0]):
                        possible = 0
                if possible == 1:
                    pairs.append([n,m])
    print "Case #%d: %d"%(k+1, len(pairs))
