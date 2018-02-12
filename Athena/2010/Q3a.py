from numpy import *

#Fname = "Primes.out";
#FILE = open(Fname,"r");

Tot = 0;        Sum = 0;
for line in file("Primes.out"):
    n = int(line);
    Tot += 1;
    Sum += (n%9 == 8)

    if (Tot % 1000000 == 0):
        print Sum, Tot, n;

print Sum, Tot

#7514470 45086079

