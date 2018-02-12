from visual import *

def A(th):
    return vector(-sin(th),cos(th),0)/M;

def Thrust(th):
    return vector(cos(th),sin(th),0)

# Initialize variables
c = 0.7;        M = 3.2;
R = 0.87;       F = 3.4;        I = c*M*R*R;
theta = -pi/2;  omega = 0;         # relative position of thruster
d = 0.1;

D = cylinder(pos=(0,0,0), vel=vector(0,0,0), color=color.red, radius=R, axis=(0,0,-d));
T = box( pos=R*Thrust(theta), size=(d,d,d), color=color.green )

Dt = curve(pos=D.pos, color=D.color, radius=0.05)
Tt = curve(pos=T.pos, color=T.color, radius=0.05)

# Simulate the physics
t = 0.;         dt = 1e-4;

while t < 10:       # Main loop
    t += dt;
    omega += F*R/I * dt;                # Disc update: rotation
    theta += omega * dt;
    D.vel += A(theta) * dt;             # Disc update: traslation
    D.pos += D.vel * dt;
    T.pos = D.pos + Thrust(theta)*R;

    Dt.append(pos = D.pos)
    Tt.append(pos = T.pos)

