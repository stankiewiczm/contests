def Bin(b):
    r = 0;
    for c in b:
        if c == '0':
            r = 2*r;
        else:
            r = 2*r+1;
    print chr(r),# r;


Fpi = open('L1.txt','r');

for line in Fpi:
    Bin(line[:-1]);


#947012399  9103 104033
