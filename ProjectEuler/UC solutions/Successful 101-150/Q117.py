from Numeric import *

Ways = list();     
for i in arange(60):
    Ways.append(long(0));

Ways[0] = 1;   Ways[1] = 1;   Ways[2] = 2;   Ways[3] = 4;

for i in arange(4,55):
    Ways[i] = Ways[i-1] + Ways[i-2] + Ways[i-3] + Ways[i-4]
    
for i in arange(1,53):
    print i, Ways[i];
