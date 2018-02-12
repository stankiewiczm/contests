from visual.graph import *

MAX = 1000000;    ARR = ones(MAX+1)+1;  ARR[1] = 1;


for j in arange(2,MAX):
    for i in arange(2,MAX/j+1):
        ARR[j*i] = ARR[j*i]+1;

Tt = 0;
for j in arange(2,MAX):
    if (ARR[j] == ARR[j-1]):
        Tt = Tt + 1;
        if (Tt%1000 == 1):
            print Tt,"found:",j-1,j,"with",ARR[j],"factors"

print Tt;

    
# Answer: 986262
