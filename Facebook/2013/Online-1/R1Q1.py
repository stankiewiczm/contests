import sys
import math
from decimal import Decimal

def main():
    f1 = open('A-card_game.txt', 'rU')
    f2 = open('R1Q1output.txt', 'w')

    mod = 1000000007

    for l in range(int(f1.readline())):
            line1 = [int(s) for s in (f1.readline()).split() if s.isdigit()]
            line2 = [int(s) for s in (f1.readline()).split() if s.isdigit()]

            N = line1[0]
            k = line1[1]

            total = 0
            ind = indinit(k)
            for i in range(nCr(N,k)):
                total = total + hand(ind,line2)
                ind = indices(k,N,ind)

            if k == 1:
                f2.write('Case #%d: %d\n' % ((l+1),sum(line2)%mod))
            else:
                f2.write('Case #%d: %d\n' % ((l+1),total%mod))                
        
    f1.close()
    f2.close()

#def factorial(n):
 #   if n == 0:
  #      return 1
   # else:
    #    return n * factorial(n-1)

def mfactorial(n, _factcache={}):
  if n not in _factcache:
    _factcache[n] = math.factorial(n)
  return _factcache[n]

def nCr(N,k):
    return int(Decimal(mfactorial(N)/(mfactorial(N-k)*mfactorial(k))))

def indices(k,N,ind):
    if ind[k-1] < (N-1):
        ind[k-1] = ind[k-1] + 1
    else:
        a = k
        b = N
        while True:
            a = a-1
            b = b-1

            if a < 1:
                break
            
            if ind[a-1] < (b-1):
                ind[a-1] = ind[a-1] + 1
                for i in range(a,k):
                    ind[i] = ind[i-1] + 1
                break
    return ind

def indinit(k):
    ind = [0]
    for i in range(1,k):
        ind = ind + [i]
    return ind

def hand(ind,cards):
    # selecting the indices of interest and finding their maximum
    return max([i for j, i in enumerate(cards) if j in ind])

if __name__ == '__main__':
    main()
