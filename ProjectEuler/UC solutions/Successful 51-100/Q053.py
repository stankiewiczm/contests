from Numeric import *;

Facts = zeros(101,Float);

for i in arange(1,101):
    Facts[i] = Facts[i-1]+log10(i);

Cnt = 0;
for i in arange(101):
    for j in arange(i+1):
        if (Facts[i]-Facts[j]-Facts[i-j] > 6):
            Cnt = Cnt+1;
print Cnt;
