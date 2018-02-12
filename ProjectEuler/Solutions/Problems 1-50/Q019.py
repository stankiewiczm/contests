Days=[31,28,31,30,31,30,31,31,30,31,30,31]
Occ =[0,0,0,0,0,0,0];

D = 2;      # 1 Jan 1901 == Tuesday

for Y in range(1901, 2001):
    for M in range(12):
        Occ[D] += 1;
        if (M == 1) and (Y%4 == 0):
            D += 1;
        D = (D + Days[M])%7;

print Occ[0], sum(Occ)
