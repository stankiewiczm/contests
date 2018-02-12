from Numeric import *

# Have to include 2 and 3:
# Target is 1/2-1/4-1/9 = 5/36;

LIST = list();
for i in arange(100):
    LIST.append([]);

LIST[3].append(0);
LIM = 5040;     TARGET = 5*(LIM*LIM)/36;
print LIM, TARGET;


WAYS = zeros(TARGET+1);
WAYS[0] = 1;        WAYS[(LIM/12)**2] = 1;       LIST = [0, (LIM/12)**2];

for i in arange(80,3,-1):
    if (len(LIST) < 1e3):
        if LIM%i == 0:
            BIT = (LIM/i)**2;
            Ll = len(LIST);
            for j in arange(Ll):
                WAYS[LIST[j]+BIT] += WAYS[LIST[j]];
                if (LIST[j]+BIT) not in LIST:
                    LIST.append(LIST[j]+BIT);
                else:
                    BIT;
                    
            print i, BIT, WAYS[TARGET], Ll, len(LIST)

    else:
        if 5040%i == 0:
            BLOCK = (LIM/i);
            BIT = BLOCK**2;
            for j in arange(TARGET,BIT-1,-1):
                WAYS[j] += WAYS[j-BIT];

            print i, BIT, WAYS[TARGET]

print WAYS[TARGET]

        
    

