from numpy import *

def Per(A,B,C):
    p  = ((A[0]-B[0])**2 + (A[1]-B[1])**2)**0.5
    p += ((B[0]-C[0])**2 + (B[1]-C[1])**2)**0.5
    p += ((C[0]-A[0])**2 + (C[1]-A[1])**2)**0.5
    if p > 10**4:
        print A,B,C,p
    return p;

def Search(R2):
    R = int(R2**0.5)
    if (R*R == R2):
        Ret = [[0,R], [R,0], [-R,0], [0,-R]];
    else:
        Ret = [];
        
    xlim = int((R2/2)**0.5)
    for x in range(1,xlim+1):
        y = int((R2-x**2)**0.5);
        if y*y+x*x == R2:
          for i in [-1,1]:
            for j in [-1,1]:
              Ret.append( [i*x, j*y] )
              Ret.append( [i*y, j*x] )
            
    return Ret


Pairs = [];
def Gen(LIM):
    for i in range(LIM+1):
        Pairs.append([]);

    xlim = int(LIM**0.5);
    for x in range(xlim+1):
        Pairs[x*x].append( [x,0] );
        Pairs[x*x].append( [0,x] );
        Pairs[x*x].append( [-x,0] );
        Pairs[x*x].append( [0,-x] );
        ylim = min(x, int((LIM-x*x)**0.5)+1);
        for y in range(1,ylim):
            rad = x*x+y*y;
            for i in [-1,1]:
                for j in [-1,1]:
                  Pairs[rad].append( [i*x,j*y] );
                  Pairs[rad].append( [i*y,j*x] );
    return
                    

def Tsearch(R2):
    Count = 0;      Perimeter = 0.;
#    List = Search(R2);
    List = Pairs[R2]
    for q in range(len(List)):
        for r in range(q):
            x3 = (5-List[q][0]-List[r][0]);
            y3 = List[q][1]+List[r][1];
            if x3**2+y3**2 == R2:
                s = List.index( [x3,-y3]);
                if (s < r):
#                    print R2, List[q], List[r], [x3,-y3] ;
                    Count += 1;
                    Perimeter += Per(List[q], List[r], List[s] )
    if Count > 0:
        print "\t",  R2, Count
    return Perimeter;    
            

ANS = 0.;       Rlim = 10**7
Gen(Rlim)
for r in range(1,Rlim):
    ANS += Tsearch(r)
print r+1, ANS
