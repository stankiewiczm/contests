FIB = [1,1];        SUM = 0;
while FIB[-1] < 4000000:
    FIB.append(FIB[-1]+FIB[-2]);
    if FIB[-1]%2 == 0:
        SUM += FIB[-1];

print SUM;
