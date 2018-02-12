from numpy import *

P = [2,3,5,7,11,13,17,19,23];

LIM = 10**9;
LIST = [];
ALL = [];

def prod(l):
    R = 1;
    for e in l:
        R *= e;
    return R;


def Generate(base, lst):
    LIST.append([]);
    n = len(lst)-1;

    mult = LIM/base;
    prange = zeros(9, int);
    for k in range(9):
        l = P[k];
        c = 1;
        while (l < mult):
            l *= P[k];
            c += 1;
        if (k > n):
            prange[k] = 1;
        else:
            prange[k] = c;

    print base, prange;

    for a in range(prange[0]):
      for b in range(prange[1]):
        for c in range(prange[2]):
          for d in range(prange[3]):
            for e in range(prange[4]):
              for f in range(prange[5]):
                for g in range(prange[6]):
                  for h in range(prange[7]):
                     N = base *2**a *3**b *5**c *7**d * 11**e *13**f *17**g * 19**h;
                     if (N < LIM):
                         LIST[n].append(N);
                         ALL.append(N);
    return;



def PCheck(prime):
    q = 1;
    while (q*q < prime):
        q += 2;
        if (prime % q == 0):
            return False;
    return True;

for n in range(len(P)):
    part = P[0:n+1];
    base = prod(part);
    Generate(base, part);
Arr = sort(ALL);
print len(Arr);

Plist = [];
Mlist = [];
next = 3;
for i in range(len(Arr)):
    e = Arr[i];
    if (e + 2 > next):
        next = e + 3;
        while not PCheck(next):
            next += 2;
        Plist.append(next);
        M = next - e;
        if M not in Mlist:
            Mlist.append(M);
    print (len(Mlist), len(Plist), i), e, (next, M)
        
print sum(Mlist);
