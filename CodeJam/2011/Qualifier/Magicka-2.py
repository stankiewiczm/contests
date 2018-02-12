from numpy import *

filename = "B-sample.txt"
FILE = open(filename, "r")
T = int(FILE.readline())

for i in range(T):
    List = FILE.readline().split()
    
    C = int(List.pop(0))
    c = []
    for j in range(C):
        c.append(List.pop(0))
#        for e in f:
#            c.append(e)
            
    D = int(List.pop(0))
    d = []
    for k in range(D):
        d.append(List.pop(0))
#        for x in F:
#            d.append(x)

    N = int(List.pop(0))
    L= []

    print c, d, List
    for n in List:
        L.append(n);
        if 
    print L

        
'''
    L = []
    for e in List[0]:
        L.append(e)
'''
    
    
    #print C,c, D,d,N, L
'''
    P = [L[0]]
    for l in range(1,N):
        for h in range(len(c)):
            if L[l] == c[h] and (L[l-1] == c[h+1]):
                P[l] = c[h+2]
            if L[l] == c[h] and (L[l-1] == c[h-1]):
                P[l] = c[h+1]
            else:
                P.append(L[l])
    print P
          
        for n in range(len(d)):
            if L[l] == d[n]:
                P = []
            
'''

    
   
#print 'Case #%d: %d'%(k+1, time)

