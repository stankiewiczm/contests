from Numeric import *

Ways = list();
for i in arange(60):
    Ways.append(long(0));

Ways[0] = 1;        # Will always add a black block after the reds.
Min = 3;

for i in arange(1,55):
    Ways[i] = Ways[i-1];
    if (i > Min):
        for j in arange(i-Min):
            Ways[i] += Ways[j];


for i in arange(1,52):
    print i-1, Ways[i]
