from Numeric import *

Best = zeros(5000);

Best[1] = 1;    Best[2] = 2;    Best[3] = 3;    Best[4] = 2;    Best[5] = 1;
Best[6] = 2;    Best[7] = 3;    Best[8] = 4;    Best[9] = 2;    Best[10]= 1;

for j in arange(10):
    Best[40+j] = 2+Best[j];
    Best[50+j] = 1+Best[j];
    Best[90+j] = 2+Best[j];
    for i in arange(1,4):
        Best[10*i+j] = Best[j]+i;
    for i in arange(6,9):
        Best[10*i+j] = Best[j]+i-4;

for j in arange(100):
    for k in arange(1,4):
        Best[100*k+j] = Best[j]+k;
    Best[400+j] = Best[j]+2;
    Best[500+j] = Best[j]+1;
    Best[900+j] = Best[j]+2;
    for k in arange(6,9):
        Best[100*k+j] = Best[j]+k-4;

for j in arange(1000):
    for l in arange(1,5):
        Best[1000*l+j] = l+Best[j];
    


SAVE = 0;       LIST = [];      FILE = "../TXTdata/roman.txt"
for line in file(FILE):
    LIST.append(line)
for l in LIST:
    New = [];
    for a in l:
        if (a == 'I'):
            New.append(1)
        if (a == 'V'):
            New.append(5)
        if (a == 'X'):
            New.append(10)
        if (a == 'L'):
            New.append(50)
        if (a == 'C'):
            New.append(100)
        if (a == 'D'):
            New.append(500)
        if (a == 'M'):
            New.append(1000)
    New.append(0);
        
    Val = 0;
    for i in arange(len(New)-1):
        if New[i] < New[i+1]:
            Val -= New[i];
        else:
            Val += New[i];

    SAVE += len(New)-1-Best[Val];

print SAVE;  
