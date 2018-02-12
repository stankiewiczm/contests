from random import *
from math import *
from visual.graph import *

N = 1000;
L = 600;
P = [];

def C():
    return (.8*random()+.2, .8*random()+.2, .8*random()+.2);    # not black

def D(i, j):
    return sqrt( (P[i][0]-P[j][0])**2 + (P[i][1] - P[j][1])**2);

def Generate():
    for i in range(N):
        P.append( [L*random(), L*random()] );

def NextPoint():
    last = Seq[-1];
    best = 2*L;
    index = -1;
    
    for i in TODO:
        if D(i, last) < best:
            best = D(i,last);
            index = i;
    return index;

Generate();
print "Generated"
graph1 = gdisplay(width=600, height=600,
             title='Travelling salesman', 
             xmax=600, xmin=0., ymax=600, ymin=0)
g1 = gdots();
for p in P:
    g1.plot(pos=p);

Seq = [0];
TODO = range(1,N);
while len(Seq) < N:
    Seq.append( NextPoint() );
    TODO.remove(Seq[-1]);
print "Path found"

Len = 0;
for i in range(N):
    Len += D(Seq[i], Seq[i-1]);
print N, L, Len;


g = gcurve(dot=True);
for i in Seq:
    rate(10);
    g.color = C();
    g.plot(pos=(P[i][0], P[i][1]));
