from pylab import*

def E1(x,y):                  # Constant field
   return 100 +x*0, 0;

def E2(x,y):                  # E = (ax, 0)
   return 100*x, 0;

def E3(x,y):                  # E = (ay, 0)
   return 100*y, 0;

def E4(x,y):                  # E = (ay, -ax)
   return 100*y, -100*x;

def E5(x,y):                  # E = (r/a)^2 r outside, 0 inside.
   E = 200.
   a = 2.
   r = sqrt(x**2+y**2) + eps
   F = (r-a+abs(r-a))/(2*(r-a))     # 1 outside, 0 inside
   Ex = E/(r/a)**2 * (x/r) * F 
   Ey = E/(r/a)**2 * (y/r) * F
   return Ex, Ey

S = 5.0
d = 1.0
eps = 1e-12;               # Small 
x = arange((-S+1),S,d)
y = arange((-S+1),S,d)
X, Y = meshgrid(x,y)

Ex1 = 100*ones(len(x))
Ey1 = zeros(len(y))

[Ex1, Ey1] = E1(X,Y)
[Ex2, Ey2] = E2(X,Y)
[Ex3, Ey3] = E3(X,Y)
[Ex4, Ey4] = E4(X,Y)
[Ex5, Ey5] = E5(X,Y)

font1 = 16
font2 = 24

# E1 and E2 on plot 1
subplot(121, aspect ='equal')
title("$(i)$")
xlabel('$x$',fontsize=font1)
ylabel('$y$', fontsize=font1)
quiver(X,Y,Ex1,Ey1)
#
subplot(122, aspect ='equal')
title("$(ii)$")
xlabel('$x$',fontsize=font1)
ylabel('$y$', fontsize=font1)
quiver(X,Y,Ex2,Ey2)

savefig("ps3q3_1.png")
clf()

# E3 and E4 on plot 2
subplot(121, aspect ='equal')
title("$(iii)$", fontsize = font1)
xlabel('$x$',fontsize=font1)
ylabel('$y$', fontsize=font1)
quiver(X,Y,Ex3,Ey3)
#
subplot(122, aspect ='equal')
title("$(iv)$", fontsize = font1)
quiver(X,Y,Ex4,Ey4)
xlabel('$x$',fontsize=font1)
ylabel('$y$', fontsize=font1)
savefig("ps3q3_2.png")
clf()

# E5 on plot 3
quiver(X,Y,Ex5,Ey5)
title('$(v)$', fontsize = font2)
for tick in gca().xaxis.get_major_ticks() + gca().yaxis.get_major_ticks():
   tick.label1.set_fontsize(font1)
xlabel('$x$',fontsize=font2)
ylabel('$y$', fontsize=font2)

savefig("ps3q3_3.png")
clf()

