from numpy import *

hit = [0]*32;

def check2(a,b):
    hit = [0]*32;
    hit[0] = 1;             hit[1] = 1;             
    hit[2+a/16] += 1;       hit[4+a/8] += 1;        hit[8+a/4] += 1;
    hit[16+a/2] += 1;       hit[a] += 1;            hit[b] += 1;
    hit[2*(a%16)+b/16] += 1;                    hit[4*(a%8)+b/8] += 1;
    hit[8*(a%4)+b/4] += 1;                      hit[16*(a%2) + b/2] += 1;
    if max(hit) == 1:
        return True;
    return False;


def Check(a,b,c,d,e):
    hit = [0]*32;
    hit[0] = 1;     hit[1] = 1;     hit[16] = 1;
    hit[a] += 1;    hit[b] += 1;    hit[c] += 1;    hit[d] += 1;    hit[e] += 1;
    hit[2+a/16] += 1;       hit[4+a/8] += 1;
    hit[8+a/4] += 1;        hit[16+a/2] += 1;       


    hit[2*(a%16)+b/16] += 1;    hit[4*(a%8)+b/8] += 1;    hit[8*(a%4)+b/4] += 1;        hit[16*(a%2) + b/2] += 1;
    hit[2*(b%16)+c/16] += 1;    hit[4*(b%8)+c/8] += 1;    hit[8*(b%4)+c/4] += 1;        hit[16*(b%2) + c/2] += 1;
    hit[2*(c%16)+d/16] += 1;    hit[4*(c%8)+d/8] += 1;    hit[8*(c%4)+d/4] += 1;        hit[16*(c%2) + d/2] += 1;
    hit[2*(d%16)+e/16] += 1;    hit[4*(d%8)+e/8] += 1;    hit[8*(d%4)+e/4] += 1;        hit[16*(d%2) + e/2] += 1;

    hit[2*(e%16)+1] += 1;       hit[4*(e%8)+2] += 1;      hit[8*(e%4)+4] += 1;          hit[16*(e%2)+8] += 1;

    if (max(hit) == 1):
        RET = 1 + 2*(e + 32*d + 1024*c + 32768*b + 1048576*a + 33554432);
#        print (a,b,c,d,e), RET;
        return RET
    return 0;    


SUM = 0L;
for a in range(1,32):
    for b in range(1,32):
        if check2(a,b):
            print (a,b),;
            for c in range(1,32):
                for d in range(1,32):
                    for e in range(1,32):
                       SUM += Check(a,b,c,d,e);
            print SUM

# 209110240768
