from Numeric import *

F = zeros(30);  F[0] = 1;   F[1] = 1;   S = 0;

for i in arange(2,30):
    F[i] = F[i-1]+F[i-2]
    if (F[i]%2 == 0):
        S = S+F[i];
print S;
    
