from Numeric import *

WaysR = list();     WaysG = list();     WaysB = list();
for i in arange(60):
    WaysR.append(long(0));
    WaysG.append(long(0));
    WaysB.append(long(0));

WaysR[0] = 1;   WaysR[1] = 1;   WaysR[2] = 2;   WaysR[3] = 3;
WaysG[0] = 1;   WaysG[1] = 1;   WaysG[2] = 1;   WaysG[3] = 2;
WaysB[0] = 1;   WaysB[1] = 1;   WaysB[2] = 1;   WaysB[3] = 1;

for i in arange(4,55):
    WaysR[i] = WaysR[i-1]+WaysR[i-2];
    WaysG[i] = WaysG[i-1]+WaysG[i-3];
    WaysB[i] = WaysB[i-1]+WaysB[i-4];
    
for i in arange(1,53):
    print i, WaysR[i]+WaysG[i]+WaysB[i]-3;
