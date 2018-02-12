F = [1,1];
while F[-1] < 10**999:
    F.append(F[-1]+F[-2]);
print len(F);
