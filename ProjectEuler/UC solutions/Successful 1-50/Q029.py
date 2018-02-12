from Numeric import *;

LIM = 100;

P = zeros(4*LIM+1);
for i in arange(2,101):
    P[i] = 1;       P[2*i] = 1;     P[3*i] = 1;   P[4*i] = 1;

Q = zeros(6*LIM+1);
for i in arange(2,101):
    Q[i] = 1;   Q[2*i] = 1;     Q[3*i] = 1;
    Q[4*i] = 1;     Q[5*i] = 1;     Q[6*i] = 1;

print 81*99 + 4*149 + sum(P) + sum(Q), 99*99;

# There are 6 powers of 2, 4 powers of 3, and 4 pairs or powers (5,6,9,10);
# Then, there are 81 normal numbers.

