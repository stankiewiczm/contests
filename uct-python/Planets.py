from visual import *
from random import *

def Normalize():
    Pcm = vector(0,0,0);        Mcm = 0;
    for p in Body:
        print p, p.M, p.v, p.pos
        Pcm += p.M*p.v;         Mcm += p.M
    Vcm = Pcm/Mcm;
    for p in Body:
        p.v -= Vcm;
    

def Planet(i):
    angle = random()*2*pi;
    Mass  = M[i];
    Speed = 2*pi*R[i]/T[i];
    Pos   = R[i] * vector(cos(angle), sin(angle), 0);
    Vel   = Speed* vector(-sin(angle), cos(angle),0);
    return [sphere( pos=Pos, radius=r[i]*1e3, color=C[i], M=Mass, v=Vel )]

    
SiD = 60*60*24;         SiY = 365.25*SiD;
AU  = 1.5e11;           ME  = 6e24;                 G   = 6.67e-11;
t   = 0;                dt = 60*60*24;

M = [2e30   , 0.55*ME, 0.82*ME, 1.00*ME, 0.11*ME, 318.*ME, 95.2*ME, 14.5*ME, 17.1*ME, 2.1e-3*ME ];
R = [0      , 0.39*AU, 0.72*AU, 1.00*AU, 1.52*AU, 5.20*AU, 9.54*AU, 19.2*AU, 30.0*AU, 39.482*AU ];
T = [1      , 88.*SiD, 224*SiD, 1.0*SiY, 687*SiD, 12.*SiY, 29.*SiY, 84.*SiY, 165*SiY, 247.7*SiY ];
C = [(1,1,0), (1,0,0), (1,1,0), (0,0,1), (1,0,0), (1,.4,0),(1,.8,0),(0,.5,1),(0,0,1),  (1,1,1)  ];
r = [ 1.5e7 ,  2.44e6,  6.05e6,  6.35e6,  3.39e6,  7.99e7,  5.82e7,  2.53e7,  2.46e7,  1.20e6   ];                   

Body = [];      Trail = [];     Nbody = len(M);     F = [0]*Nbody;
for i in range(len(M)):
    Body  += Planet(i);             # Add planetary bodies       for j in range(Nbody):
    Trail += [ curve(pos=Body[-1].pos, color=Body[i].color) ]
scene.autoscale = 0;
Normalize()                         # Shift to CoM frame

while t < 100*SiY:
    for i in range(Nbody):
        F[i] = vector(0,0,0);
    
    for i in range(Nbody):
        for j in range(Nbody):
            if i != j:
                dR = Body[i].pos - Body[j].pos;
                F[i] += -G*Body[i].M*Body[j].M*dR/mag(dR)**3;

    for i in range(Nbody):
        Body[i].v   += (F[i]/Body[i].M) * dt;
        Body[i].pos += Body[i].v * dt;
        Trail[i].append( Body[i].pos );
    t += dt;
