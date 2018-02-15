def gcd(a, b):                   # greatest common divisor of a,b
   if b != 0:                    # Recursive implementation of Euclid's
      return gcd(b, a%b);
   return a


def inverse(a, m):                     # Solves a*x = 1 (mod m)
   if gcd(a,m) != 1:                   # Recursive application of Euclid's
      print 'Not relatively prime';    # Short-short code from Bruce
      return
   a = a%m;
   if a == 1:
      return 1;
   return ( (1-inverse(m,a)*m)/a )%m
