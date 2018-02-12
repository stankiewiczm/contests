from Numeric import *;

Days = [31,28,31,30,31,30,31,31,30,31,30,31];

def AddDate(y,m):
    if (y % 4 ==0) and (m == 1):
        return 29;
    else:
        return Days[m];


Firsts = list();    Curr = 366;

for i in arange(1901,2001):
#    print i;
    for j in arange(12):
        Firsts.append(Curr);
        Curr = Curr+AddDate(i,j);

TOT = zeros(7);
for i in Firsts:
    TOT[i%7] = TOT[i%7]+1;
        
print TOT,sum(TOT)#,Firsts;

