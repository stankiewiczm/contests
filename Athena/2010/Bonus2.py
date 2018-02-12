from numpy import *

L1 = 230500000000;          # need i and (i+1)/2 to be prime;
L2 = 230700000000;          # so 
#L2 = 230500200000;
   
Probs = [];         Final = [];

def Generate(MAX):
    IsP = ones(MAX+1);        IsP[1] = 0;     NP = 0;
    for i in range(2,MAX/2+1):
        IsP[2*i] = 0;
    for i in range(3, MAX):
        if IsP[i] == 1:
            Prime.append(i);        NP += 1;
            for j in range(i, MAX/i+1):
                IsP[i*j] = 0;

    print "Generated",NP,"primes up to",MAX;
    return NP;


def Check(n1, LIST):
    if n1%4 == 0:
        return False;
    for p in Prime:
        if (n1%p <= 1):
            return False;

    LIST.append(n1-1);        
    return True;


def Check2(n1, LIST):
    for p in Prime:
        if (n1%p <= 1):
            return False;

    LIST.append(n1-1);        
    if len(LIST)%1000 == 0:
        print n1-1, len(LIST);
    return True;

#################################################
Prime = [];         np1 = Generate(25000);
k = L1;
while k < L2:
    Check(k+1+1, Probs);
    Check(k+3+1, Probs);
    Check(k+7+1, Probs);
    k += 10;
    if (k%10**6 == 0):
        print '.',
print "\nFirst pass, 200000000 limit, left with ", len(Probs);

Prime = [];         Generate(480313);
Prime = Prime[np1:len(Prime)];

for k in Probs:
    Check2(k+1, Final);
print "Final pass,",len(Probs),"cases to check, left with", len(Final);

FILE = open("Bonus2.txt","w");
for n in Final:
    s = str(n);
    FILE.write(s[0:len(s)]+"\n");
FILE.close();
