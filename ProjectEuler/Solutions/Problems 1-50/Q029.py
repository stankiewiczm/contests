from numpy import *

LIST = [];      Num = 0;
for a in range(2,101):
    for b in range(2,101):
        LIST.append(a**b);
LIST=sort(LIST);

for k in range(len(LIST)):
    if LIST[k] != LIST[k-1]:
        Num += 1;

print Num
