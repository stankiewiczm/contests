from Numeric import *

LEN = 25001;    Prime = zeros(LEN);   Prime[0] = 2;   Prime[1] = 3;

N = 3;          NPrime = 2;     Rem = long(0);  P = long(0);    Tar = 1e9;
                                                        

while(NPrime < LEN):
    N = N+2;
    Good = 1;
    for i in arange(min(NPrime,100)):
        if (N%Prime[i] == 0):
            Good = 0;
            break;
    if (Good == 1):
        Prime[NPrime] = N;
        NPrime = NPrime + 1;

    if (NPrime%2==1):       # So odd numbered prime/exponent
        P = Prime[NPrime-1]
        Rem = ((2*(NPrime))%(P))*P
        if Rem > Tar:
            print NPrime,P,Rem;
            Tar = Tar+1e9;
        
            

Generate();
print Prime[LEN-1];
