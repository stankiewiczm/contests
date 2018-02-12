from numpy import *

names = [];     Sum = 0;        Ans = 0;
TRI = [1,3,6,10,15,21,28,36,45,55,66,78,91,105,120,136,153,171,190,210];

for line in file("../TXTdata/words.txt"):
    names.append(line);                     # All gets stored in names[0];

for a in names[0]:
    if (a == ','):
        if Sum in TRI:
            Ans += 1;
        Sum = 0;

    if ((a != '"') and (a != ',')):
        Sum += ord(a)-64;

print Ans;
