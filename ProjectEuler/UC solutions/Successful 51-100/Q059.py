from Numeric import *;

N = 0;  LIST = list();  XOR = list();       STR = "";

def XOR(n,key):
    Ans = 0;
    for i in arange(8):
        Ans += (2**i)*(((n/(2**i))%2 + (key/(2**i))%2)%2);
    return Ans;

for line in file("../TXTdata/cipher1.txt"):
    names = (line);

for a in names:
    if (a == ','):
        LIST.append(N);
        N = 0;
    else:
        N = N*10+int(a);
LIST.append(N);

a = 103;        b = 111;        c = 100;

STR = "";

NEWL = zeros(1230);
for i in arange(len(LIST)):
    if (i%3 == 0):
        NEWL[i] = XOR(LIST[i],a);
    if (i%3 == 1):
        NEWL[i] = XOR(LIST[i],b);
    if (i%3 == 2):
        NEWL[i] = XOR(LIST[i],c);
for i in arange(len(NEWL)):
    STR = STR+chr(NEWL[i]);

print STR, sum(NEWL);

print "Done"
