from Numeric import *

def Check(Pan):
    Arr = zeros(10);
    for a in str(Pan):
        Arr[int(a)] = 1;
    if (sum(Arr) == 9) and (Arr[0] == 0):
        return 1;
    return 0;


for i in arange(9001,9999):
    if (Check(100002*i) == 1):
        print i,2*i,100002*i

print "All done"
