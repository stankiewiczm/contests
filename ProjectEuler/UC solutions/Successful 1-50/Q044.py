from Numeric import *

Pent = zeros(4001);

for i in arange(1,4001):
    Pent[i] = i*(3*i-1)/2;
print Pent[4000]


def Pcheck(Nn):
    Rt = sqrt(2.*Nn/3.+1./36.)+1./6.;
    if abs(Rt-round(Rt)) < 1e-6:
        return 1;
    else:
        return 0;


for i in arange(1,4000):
    if (i%100 == 0):
        print i;
    for j in arange(1,i):
        if Pcheck(Pent[i]+Pent[j]):
            if Pcheck(Pent[i]-Pent[j]):
                print Pent[i],"-",Pent[j],"=",Pent[i]-Pent[j],"with i,j=",i,j;


"""
        if ((Pent[i]-Pent[j]) in Pent):
            if ((Pent[i]+Pent[j]) in Pent):
                print "Pents",Pent[i],Pent[j], "numbered",i,j;
"""
