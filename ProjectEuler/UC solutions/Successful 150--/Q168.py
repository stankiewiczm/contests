from Numeric import *

def CountNs(End, Mult):
    LEN = 100;
    
    ARR = zeros(LEN+1);
    Carry = zeros(LEN+1);
    ARR[0] = End;
    RET = 0;
    
    for i in arange(LEN):
        ARR[i+1] = (ARR[i]*Mult+Carry[i])%10;
        Carry[i+1] = (ARR[i]*Mult+Carry[i])/10;

        if (ARR[i+1] == End) and (Carry[i+1] == 0) and (ARR[i] != 0) and (i > 0):
            RT = 0;
            for i in arange(min(i,4)+1):
                RT += 10**i*ARR[i]

            RET += RT;
    return RET;

TOT = 0
for I in arange(1,10):          # Multiplier
    for J in arange(1,10):      # Last digit
        TOT += CountNs(J,I);
print TOT%100000;
