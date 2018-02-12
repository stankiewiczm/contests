from numpy import *

S = 52735727364727372;
T = 2889221271829121;

s1 = 343*79
s2 = 4*22051
s3 = 22064569

t1 = T%s1;
t2 = T%s2;
t3 = T%s3;

n1 = 1;     n2 = 1;     n3 = 1;
while (n1*t1)%s1 != 1:
    n1 += 1;
while (n2*t2)%s2 != 1:
    n2 += 1;
while (n3*t3)%s3 != 1:
    n3 += 1;

print n1, s1
print n2, s2
print n3, s3

V1 = s1*s2;
T1 = T%V1;          
while (n1*T1)%V1 != 1:
    n1 += s1;
print n1, V1
while (n1*t3)%s3 != 1:
    n1 += V1;
print n1



#Min = T;        Best = 1;
#while (Min != 1):
#    print Best, Min;
#    P = S/Min + 1;
#    Best = (P*Best)%S;#(Min*S)/T + 1;
#    Min = (Best*T)%S;

#print Best%S, (Best);

