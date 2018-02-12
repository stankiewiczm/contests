from Numeric import *

# solutions == (d(n*n)+1)/2;
# Now d(Prod p_i^{a_i}) = Prod (a_i+1);
# So Prod(2a_i+1) > 2000000


MINa = 3**15;
for a3 in arange(9,0,-1):
    for a5 in arange(9,0,-1):
        for a7 in arange(9,0,-1):
            P = (3**a3 * 5**a5 * 7**a7);
            if (P < MINa) and (P > 8e6):
                print a3,a5,a7, P
                MINa = P;


# This produces 8, 2, 2.
# Hence need 2 numbers cubed, 2 numbers squared, 8 numbers singly;

print 8*27*25*49*11*13*17*19*23*29*31*37
    
"""
Prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47];
Alph = [10,8,7,5,3,2,1,1,1,1,1,1,1,1,1]

Nd = 1;     N = 1;
for i in arange(9):
    Nd *= (2*Alph[i]+1);
    N  *= Prime[i]**Alph[i]
MIN = N;


for P0 in arange(5):
    for P1 in arange(P0+1):
        for P2 in arange(P1+1):
            for P3 in arange(P2+1):
                for P4 in arange(P3+1):
                    for P5 in arange(P4+1):
                        for P6 in arange(P5+1):
                            for P7 in arange(P6+1):
                                for P8 in arange(P7+1):
                                    for P9 in arange(P8+1):
                                        for PA in arange(P9+1):
                                            for PB in arange(PA+1):
                                                for PC in arange(PB+1):
                                                    Nd = (2*P0+1)*(2*P1+1)*(2*P2+1)*(2*P3+1)*(2*PA+1)*(2*PB+1)*(2*PC+1);
                                                    Nd *= (2*P4+1)*(2*P5+1)*(2*P6+1)*(2*P7+1)*(2*P8+1)*(2*P9+1);
                                                    if (Nd > 8e6):
                                                        N  = 2**P0 * 3**P1 * 5**P2 * 7**P3 * 11**P4 * 13**P5 ;
                                                        N *= 17**P6 * 19**P7 * 23**P8 * 29**P9 * 31**PA * 37**PB * 41**PC;
                                                        if N < MIN:
                                                            MIN = N;
                                                            print MIN, Nd;
                                                            print P0,P1,P2,P3,P4,P5,P6,P7,P8,P9,PA,PB,PC;
"""
