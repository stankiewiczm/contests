from Numeric import *

LIM = 12000+1;        MIN = zeros(2*LIM+1);
for k in arange(2,LIM):
    MIN[k] = 2*k

MIN[2] = 4;     MIN[3] = 6;     MIN[4] = 8;     MIN[5] = 8;     MIN[6] = 12;
MIN[7] = 12;    MIN[8] = 12;    MIN[9] = 15;    MIN[10] = 16;   MIN[11] = 16;   MIN[12] = 16;

for a in arange(2,LIM/2+1):
    if a%10 == 0:
        print a;
    for b in arange(1,min(a, LIM/a+1)+1):
        for c in arange(1,min(b, LIM/(a*b)+1)+1):
            for d in arange(1,min(c, LIM/(a*b*c)+1)+1):
                for e in arange(1,d+1):
                    for f in arange(1,e+1):
#                        PRD = a*b*c*d*e*f;
#                        if (PRD < 2*LIM):
#                            Kk = PRD-a-b-c-d-e-f+6;
#                            if Kk == 12:
#                                print a,b,c,d,e,f;
#                            if (PRD < MIN[Kk]):
#                                MIN[Kk] = PRD;
                        if (a*b*c*d*e*f < 2*LIM):
                            for g in arange(1,f+1):
                                for h in arange(1,g+1):
                                    for i in arange(1,h+1):
                                        for j in arange(1,i+1):
                                            for k in arange(1,j+1):
                                                for l in arange(1,k+1):
                                                    for m in arange(1,l+1):
                                                        PRD = a*b*c*d*e*f*g*h*i*j*k*l*m;
                                                        if (PRD < 2*LIM) and (PRD > 12):
                                                            Kk = PRD-a-b-c-d-e-f-g-h-i-j-k-l-m+13;
                                                            if (PRD < MIN[Kk]) and (Kk >= 13) and (Kk < LIM):
                                                                MIN[Kk] = PRD

   
LST = [];
for q in arange(2,LIM):
    if MIN[q] not in LST:
        LST.append(MIN[q]);
print len(LST), sum(LST);
