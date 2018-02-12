LIM = 2*4000000;                                    Best = 10**100;             
P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47];     P2 = P[5:len(P)];

def Prod(seq):
    R = 1;
    for n in seq:
        R *= n;
    return R


def Eval(As):
    N = 1;      D = 1;
    for k in range(len(As)):
        N *= P[k]**(As[k]);
        D *= (2*As[k]+1)
    return [N,D];


## It is a fair guess that only the first 5 primes will be repeated...

for a in range(1,10):
  for b in range(1,a+1):
    for c in range(1,b+1):
      for d in range(1,c+1):
        for e in range(1,d+1):
          [Lead, Sols] = Eval([a,b,c,d,e]);
          MoreP = 0L;
          while (Sols*3**MoreP < LIM):
              MoreP += 1;
          N = Lead*Prod(P2[0:MoreP]);
          S = Sols*3**MoreP;
          if (N < Best):
              Best = N;

print Best
