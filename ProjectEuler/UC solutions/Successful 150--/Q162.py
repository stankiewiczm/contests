from Numeric import *

# Use the convention WAY[dig][bin]
# bin will be a binary encoding of (0,1,A), i.e. are the digits present

WAY = [];
for a in arange(17):
    WAY.append([]);
    for b in arange(8):
        WAY[a].append(0L);
WAY[0][0] = 1;
WAY[1][0] = 13;     WAY[1][2] = 1;      WAY[1][4] = 1;

for dig in arange(2,17):        # Add a digit out front
    WAY[dig][0] = 13*WAY[dig-1][0];
    WAY[dig][1] = 14*WAY[dig-1][1] + WAY[dig-1][0];       # 0, not 1,A
    WAY[dig][2] = 14*WAY[dig-1][2] + WAY[dig-1][0];       # 1, not 0,A
    WAY[dig][3] = 15*WAY[dig-1][3] + WAY[dig-1][2] + WAY[dig-1][1];
    WAY[dig][4] = 14*WAY[dig-1][4] + WAY[dig-1][0];       # 1, not 0,A
    WAY[dig][5] = 15*WAY[dig-1][5] + WAY[dig-1][4] + WAY[dig-1][1];
    WAY[dig][6] = 15*WAY[dig-1][6] + WAY[dig-1][4] + WAY[dig-1][2];
    WAY[dig][7] = 16*WAY[dig-1][7] + WAY[dig-1][3] + WAY[dig-1][5] + WAY[dig-1][6];
    
TOT = 0L
for dig in arange(1,17):
    TOT += WAY[dig][7]

print "To reverse and hex: ",
while TOT > 0:
    print TOT%16,
    TOT = TOT/16;
print "\nComes to 3D58725572C62302"
