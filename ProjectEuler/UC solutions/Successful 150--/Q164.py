from Numeric import *

Pass = list();
for i in arange(21):
    Pass.append(list());
    for j in arange(100):
        Pass[i].append(long(0))

for a in arange(1,10):
    for b in arange(10):
        for c in arange(10):
            if (a+b+c < 10):
                Pass[3][10*b+c] += 1;

for i in arange(4,21):
    # Creating 4th, 5th, ... digits;
    for d in arange(10):            # Digit just added;
        for b in arange(10):        # Digit before it
            for a in arange(10):    # Digit before that
                if (a+b+d < 10):
                    Pass[i][10*b+d] += Pass[i-1][10*a+b];

print sum(Pass[20]);
            
        
    
