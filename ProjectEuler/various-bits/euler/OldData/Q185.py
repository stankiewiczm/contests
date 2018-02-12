from Numeric import *

s1 = [9,0,3,4,2];   R1 = 2;
s2 = [7,0,7,9,4];   R2 = 0;
s3 = [3,9,4,5,8];   R3 = 2;
s4 = [3,4,1,0,9];   R4 = 1;
s5 = [5,1,5,4,5];   R5 = 2;
s6 = [1,2,5,3,1];   R6 = 1;

#######################################
LIST = [5616185650518293 , 3847439647293047 , 5855462940810587 ,
        9742855507068353 , 4296849643607543 , 3174248439465858 ,
        4513559094146117 , 7890971548908067 , 8157356344118483 ,
        2615250744386899 , 8690095851526254 , 6375711915077050 ,
        6913859173121360 , 6442889055042768 , 2321386104303845 ,
        2326509471271448 , 5251583379644322 , 1748270476758276 ,
        4895722652190306 , 3041631117224635 , 1841236454324589 , 2659862637316867 ]

CORS = [2,1,3,3,3,1,2,3,1,2,3,1,1,2,0,2,2,3,1,3,3,2];
########################################

S = list();
for i in arange(22):            
    S.append([]);
    while LIST[i] > 0:
        Pow = 10**(22-i)
        S[i].append(int(LIST[i]%Pow));
        LIST[i] = LIST[i] - Pow*S[i][len(S[i])-1];
        


def CheckW(S1, S2):
    RT = 0;
    for q in arange(len(S1)):
        if S1[q] == S2[q]:
            RT += 1;
    return RT;


def Verified(seq):
    if (Check(seq,s1) == R1) and (Check(seq,s2) == R2):
        if (Check(seq,s3) == R3) and (Check(seq,s4) == R4):
            if (Check(seq,s5) == R5) and (Check(seq,s6) == R6):
                return True;
    return False


for a in arange(10):
    for b in arange(10):
        for c in arange(10):
            for d in arange(10):
                for e in arange(10):
                    for f in arange(10):
                        for g in arange(10):
                            for h in arange(10):
                                N = [a,b,c,d,e];

                            if Verified(N):
                                print "A hint of a solution",N
