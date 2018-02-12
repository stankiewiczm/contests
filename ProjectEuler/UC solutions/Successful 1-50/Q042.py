from Numeric import *;

WScore = 0;     Tot = list();

words = [];
for line in file("../TXTdata/words.txt"):
    words.append(line);

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
for i in arange(len(words[0])):
    Lst.append(zeros(10))



Cnt = 0;  
for a in words[0]:
    if (a == ','):
        Tot.append(WScore);
        Cnt += 1;
        WScore = 0;     
    if ((a != '"') and (a != ',')):
        WScore = WScore + V(a);

Tot.append(WScore);

Cnt = 0;
for i in Tot:
    Vl = sqrt(2.*i+0.25)-0.5;
    if (abs(Vl - round(Vl)) < 1e-6):
        Cnt += 1;
print Cnt;
