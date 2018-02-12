def FindR(a):
    n = 1;      Max = 2*a;      A2 = a**2; 
    while (n < a):
        n += 1;
        k = (2*n*a)%A2;
        if k > Max:
            Max = k;
#    print a, Max/a, Max%a;
    return Max;

Sum = 0;
for a in range(3,1001):
    Sum += FindR(a);
print Sum
