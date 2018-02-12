from Numeric import *

Prods = zeros(100000);

def CheckProd(A,B):
    Chck = zeros(10);
    for a in str(A)+str(B)+str(A*B):
        Chck[int(a)] = 1;
    if ((sum(Chck) == 9) and (Chck[0] == 0)):
        print A,'*',B,'=',A*B;
        return A*B;
    else:
        return 0;

for i in arange(1,100):
    for j in arange(1000/i,10000/i):
        Ans = CheckProd(i,j);
        Prods[Ans] = Ans;

print "Sum of products is",sum(Prods);

#Case 1: Digits (2*3 = 4):
