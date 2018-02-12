from numpy import *
from RandomArray import *

# Exact solution
# DP each score after each throw.

def Evaluate(q):
    Prob = [];
    for i in range(51):
        Prob.append( [0.]*51 );
    Prob[0][0] = 1.;

    for throw in range(1,51):
        succ = 1-throw/q;

        Prob[throw][0] = Prob[throw-1][0]*(1-succ);
        for score in range(1,50):
            Prob[throw][score] = Prob[throw-1][score]*(1-succ) + Prob[throw-1][score-1]*succ;

    return Prob[50][20];        

def Test(q, lim):
    run = 0;        Twenty = 0.;
    Prob = zeros(50);
    for x in range(50):
        Prob[x] = 1-(x+1.)/q;
    while (run < lim):
        run += 1;
        if sum( random(50) < Prob) == 20:
            Twenty += 1;
        
    return Twenty/run;

Low = 50.;       High = 55.;
print Low, Evaluate(Low);
print High,Evaluate(High);

while (High-Low > 1e-10):
    Mid = (Low+High)/2;
    Eval = Evaluate(Mid);
    print Mid, Eval;
    if Eval > 0.02:
        Low = Mid;
    else:
        High = Mid
    
