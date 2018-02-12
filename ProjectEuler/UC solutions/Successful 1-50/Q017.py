from Numeric import *;

Digs = zeros(1001);
Digs[1] = 3;    Digs[2] = 3;    Digs[3] = 5;    Digs[4] = 4;    Digs[5] = 4;
Digs[6] = 3;    Digs[7] = 5;    Digs[8] = 5;    Digs[9] = 4;    Digs[10]= 3;
Digs[11]= 6;    Digs[12]= 6;    Digs[13]= 8;    Digs[14]= 8;    Digs[15]= 7;
Digs[16]= 7;    Digs[17]= 9;    Digs[18]= 8;    Digs[19]= 8;

Digs[20]= 6;    Digs[30]= 6;    Digs[40]= 5;    Digs[50]= 5;
Digs[60]= 5;    Digs[70]= 7;    Digs[80]= 6;    Digs[90]= 6;

for i in arange(1,10):
    Digs[i*100] = Digs[i]+7;      # Basics set;

for i in arange(21,100):
    Digs[i] = Digs[i%10] + Digs[i-i%10];

for i in arange(101,1000):
    if (i % 100 != 0):
        Digs[i] = Digs[i%100] + 3 + Digs[i-i%100];

Digs[1000] = 11;

print Digs[115];
print Digs[342];
print sum(Digs);
                                    
