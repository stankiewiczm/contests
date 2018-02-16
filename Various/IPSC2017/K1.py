from random import *

s = raw_input();
print len(s);


for C in s[:1000]:
    Ord = ord(C)-33;
    a = Ord/27;
    b = (Ord%27)/9
    c = (Ord%9)/3;
    d = (Ord%3);

    print a,b,c,d,
    


#s = raw_input();
#print len(s);
