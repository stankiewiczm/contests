from visual.graph import *
from RandomArray import *

a = 1;      dx = 0.01;      V0 = -15;   k = 1.;

def V(x):
    if (abs(x) < a):
        return V0;
    else:
        return 0;

def f(E):
    x = -a-k+dx;
    psi = [0, 1e-9];
    while (x < a+k):
        psi.append(2*psi[-1]-psi[-2] + (dx)*(dx)*(V(x)-E)*psi[-1]);
        x += dx;
    return psi[-1];


def Plot(E):
    OUT = gcurve(color=random(3));
    x = -a-k+dx;      psi = [0, 1e-9];        I = 0.;
    while (x < a+k):
        psi.append(2*psi[-1]-psi[-2] + (dx)*(dx)*(V(x)-E)*psi[-1]);
        x += dx;
        I += (dx)*(psi[-1]**2);
        
    x = -a-k+dx;      PSI = [0, (1e-9)/sqrt(I)];   I2 = 0.;     
    while (x < a+k):
        PSI.append(2*PSI[-1]-PSI[-2] + (dx)*(dx)*(V(x)-E)*PSI[-1]);
        x += dx;
        I2 += (dx)*(PSI[-1]**2);
        OUT.plot(pos = (x, PSI[-1]));

    print E;
    return ;


def BinSearch(E1, E2):
    while (E2-E1 > 1e-9):
        V1 = f(E1);     V2 = f(E2);     Vm = f((E1+E2)/2.);
        if (V1*Vm > 0):
            E1 = (E1+E2)/2.;
        else:
            E2 = (E1+E2)/2.;
    return (E1+E2)/2;



for q in range(V0, -1):
    if (f(q)*f(q+1) < 0):
        Plot(BinSearch(q, q+1));
