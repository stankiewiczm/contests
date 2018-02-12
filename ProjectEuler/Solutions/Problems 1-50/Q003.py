N = 600851475143;
p = 3;
while (N != 1):
    while (N%p == 0):
        print p;
        N = N/p;
    else:
        p += 2;
        
