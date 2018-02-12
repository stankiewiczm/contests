from Numeric import *

Data=[map(int ,line.split())for line in file("gfs_drf.evp")]

Xmin = Data[0][0];      Ymin = Data[0][1];
Xmax = Data[0][0];      Ymax = Data[0][1];

for p in Data:
    if p[0] < Xmin:
        Xmin = p[0];
    if p[0] > Xmax:
        Xmax = p[0];
    if p[1] < Ymin:
        Ymin = p[1];
    if p[1] > Ymax:
        Ymax = p[1];

#print "Make a box in ranges",Xmin, Xmax, "    ", Ymin, Ymax;
N = len(Data);

Bucket = [];        Grid = 32;
for a in arange(Grid):
    Bucket.append(zeros(Grid));

Xgrid = (Xmax-Xmin)/Grid+1;       Ygrid = (Ymax-Ymin)/Grid+1;

for p in Data:
    buckX = (p[0]-Xmin)/Xgrid;
    buckY = (p[1]-Ymin)/Ygrid;
    Bucket[buckX][buckY] += 1;

LIMIT = N/(Grid*Grid*10);
#print "Limit for events per bucket is ",LIMIT;

for p in Data:
    buckX = (p[0]-Xmin)/Xgrid;
    buckY = (p[1]-Ymin)/Ygrid;
    if (Bucket[buckX][buckY] <= LIMIT):    
        print p[0], p[1], p[2];
