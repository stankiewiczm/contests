from numpy import *

P = [5];

n = 9;
while (n < 100):
    if (n%3)*(n%5)*(n%7)*(n%11) != 0:
        P.append(n);
    n += 4;
    
LIST = [1];
for k in range(len(P)):
    for l in range(2**k):
        LIST.append( LIST[l]*P[k] );
        
print P
LIST = sort(LIST);

###############################################

TOTSum = 0;
for e in LIST:
#    print e;
    Sum = 0;
    aMax = int(sqrt(e*0.5));
    bMin = aMax+1;
    bMax = int(sqrt(e*1.0));

    for b in range(bMax, bMin-1, -1):
        a2 = e-b*b;
        a = int(sqrt(a2));
        if (a*a == a2):
            Sum += a;
    TOTSum += Sum

print TOTSum
