from numpy import *

def Fit2(a,b):
    R = [a+b, a-b, b-a, a*b];
    if a != 0 and b != 0:
        R.append(a/b);
        R.append(b/a);
    return R;

def Fit3(a,b,c):
    R3 = [];        OUT = [];
    BC = Fit2(b,c);     AC = Fit2(a,c);     AB = Fit2(a,b);
    for k in BC:
        R3 += Fit2(a,k);
    for k in AC:
        R3 += Fit2(b,k);
    for k in AB:
        R3 += Fit2(c,k);
    R3 = sort(R3);
    for e in R3:
        if e not in OUT:
            OUT.append(e);
    return OUT


def Fit4(A,B,C,D):
    R4 = [];        OUT = [];       
    for k in range(4):
        M = [A+0.,B+0.,C+0.,D+0.];
        a = M.pop(k);       BCD = Fit3( M[0], M[1], M[2] );
        for e in BCD:
            R4 += Fit2(a,e);
    for e in sort(R4):
        if e not in OUT:
            OUT.append(e);
    return OUT


def Counter(LIST):
    n = 1;      IList = map
    while (n in LIST):
        n += 1;
    return n-1;


for q in range(1,7):
  for r in range(q+1, 8):
    for s in range(r+1, 9):
      for t in range(s+1, 10):
        if Counter(Fit4(q,r,s,t)) > 50:
          print (q,r,s,t), Counter(Fit4(q,r,s,t))#, Fit4(q,r,s,t);
#print Counter(Fit4(1,2,3,7))

