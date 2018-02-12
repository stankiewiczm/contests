from numpy import *

def Gen(k, l):
    R = 0;
    if (l == 3):
        R = (k*(k+1))/2;
    if (l == 4):
        R = k*k;
    if (l == 5):
        R = (k*(3*k-1))/2;
    if (l == 6):
        R = k*(2*k-1);
    if (l == 7):
        R = (k*(5*k-3))/2;
    if (l == 8):
        R = k*(3*k-2);
    if (R >= 1000) and (R < 10000):
        return R;
    return 0;

Val = [ [], [], [], [], [], [] ];
for c in range(200):
    for d in range(6):
        if Gen(c,d+3) > 0:
            Val[d].append(Gen(c,d+3));


def Solve(a,b,c,d,e):
    for n1 in Val[0]:
      for n2 in Val[a]:
        if (n1%100 == n2/100):
          for n3 in Val[b]:
            if (n2%100 == n3/100):
              for n4 in Val[c]:
                if (n3%100 == n4/100):
                  for n5 in Val[d]:
                    if (n4%100 == n5/100):
                      for n6 in Val[e]:
                        if (n5%100 == n6/100):
                          if (n6%100 == n1/100):
                            print n1, n2, n3, n4, n5, n6, (a,b,c,d,e);
                            print n1+n2+n3+n4+n5+n6

# Has to be a complete loop, 
for a in range(1,6):
  for b in range(1,6):
    for c in range(1,6):
      for d in range(1,6):
        for e in range(1,6):
            if a*b*c*d*e == 120 and a+b+c+d+e == 15:
              Solve(a,b,c,d,e);
