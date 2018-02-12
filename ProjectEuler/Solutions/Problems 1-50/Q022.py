from numpy import *

Tot = [];     names = [];     

for line in file("../TXTdata/names.txt"):
    names.append(line);                     # All gets stored in names[0];


NScore = 0;     NAlf = 0.;    Lett = 0;
for a in names[0]:
    if (a == ','):
        Tot.append(1000*long(NAlf*10**15)+NScore);
        NScore = 0;     NAlf = 0.;        Lett = 0;

    if ((a != '"') and (a != ',')):
        V = ord(a)-64;
        NScore += V;
        Lett += 1;
        NAlf += V/(30.**Lett);

Tot.append(1000*long(NAlf*10**15)+NScore);

Tot = sort(Tot);        Sum = 0;
for a in range(len(Tot)):
    Sum = Sum + (a+1)*(Tot[a]%1000);
print Sum;

