from visual.graph import *

Prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97];
MX = 150000;
NFs = zeros(MX+3);


def NFacts(N):
    Pow = zeros(25);
    NFct = 0;
    for i in arange(25):
        if (N%Prime[i] == 0):
            while (N%Prime[i] == 0):
                N = N/Prime[i];
            NFct = NFct+1;
    if (N != 1):
        NFct = NFct+1;
    return NFct;


for j in arange(1,MX+3):
    NFs[j] = NFacts(j);

for j in arange(100,MX):
    if (NFs[j] == 4) and (NFs[j+1] == 4) and (NFs[j+2] == 4) and (NFs[j+3] == 4):
        print j, j+1, j+2, j+3;
    

print "All done";
