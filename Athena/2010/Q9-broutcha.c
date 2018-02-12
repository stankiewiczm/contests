#include <stdio.h>
typedef long long ll;
 
// fact[x] = smallest prime factor of x (1 if x is prime)
long *fact;
 
// Euler's Totient function
long phi(long x) {
  if(x <= 1) return 1;
  long f = fact[x];
  if(f == 1) return x-1;
  long p = 1, fp = 1;
  while((x /= f) % f == 0) { p++; fp *= f; }
  return phi(x)*(f-1)*fp;
}
 
int main() {
  long M = 100000001;
  // Compute fact[]
  fact = new long[M];
  for(long i=0; i<M; i++) fact[i]=1;
  for(long i=2; i<M; i++) if(fact[i]==1) {
    for(long k=i+i; k<M; k+=i) if(fact[k]==1) fact[k]=i;
  }
 
  // Sum phi(2) .. phi(M)
  ll s = 0;
  ll s2 = 0;
  ll loop = 0;
  for(long i=2; i<M; i++) 
  {
	  s2 = s;
	  s += phi(i);
	  if (s2 > s) loop++;
  };
  printf("%lld %lld\n", s, loop);
  return 0;
}