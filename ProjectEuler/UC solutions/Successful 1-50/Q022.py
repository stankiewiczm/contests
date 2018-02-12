from Numeric import *;

NScore = 0;       NAlf = 0.;    Tot = list();

names = [];
for line in file("../TXTdata/names.txt"):
    names.append(line);

print len(names[0]);


def V(char):
    if (char == 'A'):   return 1;
    if (char == 'B'):   return 2;
    if (char == 'C'):   return 3;
    if (char == 'D'):   return 4;
    if (char == 'E'):   return 5;
    if (char == 'F'):   return 6;
    if (char == 'G'):   return 7;
    if (char == 'H'):   return 8;
    if (char == 'I'):   return 9;
    if (char == 'J'):   return 10;
    if (char == 'K'):   return 11;
    if (char == 'L'):   return 12;
    if (char == 'M'):   return 13;
    if (char == 'N'):   return 14;
    if (char == 'O'):   return 15;
    if (char == 'P'):   return 16;
    if (char == 'Q'):   return 17;
    if (char == 'R'):   return 18;
    if (char == 'S'):   return 19;
    if (char == 'T'):   return 20;
    if (char == 'U'):   return 21;
    if (char == 'V'):   return 22;
    if (char == 'W'):   return 23;
    if (char == 'X'):   return 24;
    if (char == 'Y'):   return 25;
    if (char == 'Z'):   return 26;
    return 0;

Lst = list();
for i in arange(len(names[0])):
    Lst.append(zeros(10));



Cnt = 0;    Lett = 0;
for a in names[0]:
    if (a == ','):
        Tot.append(1000*long(NAlf*10**15)+NScore);
#        print NScore[Cnt],NAlf[Cnt],Tot[Cnt],Tot[Cnt]%1000;
        Cnt += 1;
        NScore = 0;     NAlf = 0.;        Lett = 0;
    if ((a != '"') and (a != ',')):
        NScore = NScore + V(a);
        Lett = Lett+1;
        NAlf = NAlf + float(V(a))/(30.**Lett);

#Tot[Cnt] = 200*int(10000000*NAlf)+NScore;
Tot.append(1000*long(NAlf*10**15)+NScore);
Cnt += 1;
                        
print Cnt;
Tot = sort(Tot);
#print Tot;


Sum = 0;
for a in arange(Cnt):
    Sum = Sum + (a+1)*(Tot[a]%1000);
#    print (a+1), Tot[a]%200, (a+1)*(Tot[a]%200), Sum;
print Sum;

