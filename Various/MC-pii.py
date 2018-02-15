from math import *
from random import *
from time import *

def Run(n):
    Start = time();
    Hit = 0;
    for i in range(n):
        theta = random()*pi/2
        x = random();
        y = x+cos(theta);
        Hit += int(y)-int(x);
    print Hit,'/',n
    print n/float(Hit), pi/2;
    print time()-Start
    
