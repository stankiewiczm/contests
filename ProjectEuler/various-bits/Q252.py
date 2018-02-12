from numpy import *

L = [290797L];      Pnt = [];
while (len(L) < 1000):
    L.append((L[-1]**2)%50515093);

for k in range(100):
    Pnt.append( (int(L[2*k+1]%2000-1000), int(L[2*k+2]%2000-1000)) );

    if (Pnt[k][1] < -400) and (Pnt[k][0] < 400):
        print Pnt[k][0], Pnt[k][1]


T = 0L;     MAX = 0.;
for k in range(100):
    for l in range(k):
        for m in range(l):
            S1 = sqrt((Pnt[k][0]-Pnt[l][0])**2 + (Pnt[k][1]-Pnt[l][1])**2);
            S2 = sqrt((Pnt[m][0]-Pnt[k][0])**2 + (Pnt[m][1]-Pnt[k][1])**2);
            S3 = sqrt((Pnt[l][0]-Pnt[m][0])**2 + (Pnt[l][1]-Pnt[m][1])**2);

            A = sqrt( (S1+S2+S3)*(S1+S2-S3)*(S1+S3-S2)*(S2+S3-S1))/4;
            if (A > 1e6):
                T += 1;
print T;
