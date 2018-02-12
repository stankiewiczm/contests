DATA=[map(int ,line.split())for line in file("vr5y.evp")];

for p in DATA:
    print p[0],p[1],p[2],"\n"
