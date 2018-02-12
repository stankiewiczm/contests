from Numeric import *;

Cnt = 0; 
for i in arange(1,10):
    for j in arange(1,25):
        if (j*log10(i)+1 >= j):
            Cnt = Cnt+1;
            print i,j,i**j;
print Cnt;
