from numpy import *

MAX = 10**6;                    Prime = [2];     
IsP = ones(MAX);                IsP[1] = 0;

Plim = 1229;        Friends = [];

def Gen():
    for i in range(2,MAX/2):
        IsP[2*i] = 0;
    n = 3;
    while (n < MAX):
        if (IsP[n] == 1):
            Prime.append(n);
            for i in arange(2,(MAX-1)/n+1):
                IsP[n*i] = 0;
        n += 2;
    return len(Prime);


def Check(p):
    if (p < MAX):
        return IsP[p];

    for k in Prime:
        if (p%k == 0):
            return 0;
        if (p < k*k):
            return 1;

def Gen2():
    for k in range(Plim):
        if (k%100 == 99):
            print k+1
        Friends.append(zeros(Plim, int));

        for l in range(k):
            s1 = str(Prime[l]);
            s2 = str(Prime[k]);
            if Check(int(s1+s2)) and Check(int(s2+s1)):
                Friends[k][l] = 1;
                Friends[l][k] = 1;
                        
#############################

print "Starting"
NP = Gen();
print "Generated",NP,"primes up to",Prime[NP-1];
Gen2();
print "Friend list made"

for i in range(Plim):
  for j in range(i):
    if Friends[i][j]:
      for k in range(j):
        if Friends[i][k] and Friends[j][k]:
          for l in range(k):
            if Friends[i][l] and Friends[j][l] and Friends[k][l]:
              for m in range(l):
                if Friends[i][m] and Friends[j][m] and Friends[k][m] and Friends[l][m]:
                  print "Solution:", (i,j,k,l,m), Prime[i], Prime[j], Prime[k], Prime[l], Prime[m];
                  print "Answer:", Prime[i]+Prime[j]+Prime[k]+Prime[l]+Prime[m];
