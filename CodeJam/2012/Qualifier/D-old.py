from math import *

def GCD(x,y):
   while (x*y > 0):
      if (x > y):
         x -= (x/y)*y
      else:
         y -= (y/x)*x;
   return (x+y);
   

def GetDir(d):
   d2 = d*d;
   Ret = [ [0,1], [1,0], [0,-1], [-1,0] ];
   Ret = [ ];
   for x in range(1, d+1):
      for y in range(1, d+1):
         if GCD(x,y) == 1:
            if 0 < x**2 + y**2 <= d2:
               r = (x**2+y**2)**0.5
               Ret.append( [ x/r, y/r] );
               Ret.append( [ x/r,-y/r] );
               Ret.append( [-x/r, y/r] );
               Ret.append( [-x/r,-y/r] );
   return Ret



T = int(raw_input());
for case in range(T):
   Xx = 0;     Xy = 0;     Ans = 0;

   [H, W, D] = map(int, raw_input().split());
   Ws = [];
   for i in range(H):
      Ws += raw_input().split();
      if 'X' in Ws[-1]:
         Xy = i;
         Xx = Ws[-1].find('X');

   Wall = [];
   for i in range(len(Ws[0])):
      Wall.append( [] );
   for i in range(len(Ws)):
      for j in range(len(Ws[0])):
         Wall[j].append( Ws[i][j] );

   print Wall
   X0 = Xx;    Y0 = Xy;

   # First do cardinal directions
   xi = X0;    yi = Y0;
   while Wall[xi][yi] != '#':
      xi += 1;
   if 2*(xi-X0)-1 <= D:
      Ans += 1;
   xi = X0;    yi = Y0;
   while Wall[xi][yi] != '#':
      xi -= 1;
   if 2*(X0-xi)-1 <= D:
      Ans += 1;
   xi = X0;    yi = Y0;
   while Wall[xi][yi] != '#':
      yi += 1;
   if 2*(yi-Y0)-1 <= D:
      Ans += 1;
   xi = X0;    yi = Y0;
   while Wall[xi][yi] != '#':
      yi -= 1;
   if 2*(Y0-yi)-1 <= D:
      Ans += 1;

   # Now do the difficult directions.
   Directions = GetDir(D);
   for Dir in Directions:
      xi = X0+0.5;             # Instantenous x position
      yi = Y0+0.5;             # Instantenous y position
      Xc = X0;                
      Yc = Y0;                # current square
      dx = Dir[0];
      dy = Dir[1];            # Directions
      t = 0.;                 # Time/distance travelled
      Done = False;           # Simulation terminated

      print Dir, dx, dy;
      
      while (t < D) and (not Done):


         if (dx > 0):
            tx = (int(xi)-xi+1)/dx;
         else:
            tx = (xi-int(xi))/abs(dx);
         if (dy > 0):
            ty = (int(yi)-yi+1)/dy;
         else:
            ty = (yi-int(yi))/abs(dy);

         if ty < 1e-5:
            ty = 0.01;
         if tx < 1e-5:
            tx = 0.01

         print (t, (xi, yi)), (dx, dy),'\n'
         
         if abs(tx-ty) < 1e-6:         # Heading into a corner
            t += tx;
            xi = int(round(xi+dx*tx));
            yi = int(round(yi+dy*ty));
            DX = int( dx/abs(dx));
            DY = int( dy/abs(dy));
            if Wall[Xc+DX][Yc] == Wall[Xc+DX][Yc+DY] == Wall[Xc][Yc+DY] == '#':
               Corner = True;
               if D+1e-6 > 2*t:
                  Ans += 1;
                  print 'sucesss', t
               Done = True;
            else:
               if Wall[Xc+DX][Yc] == Wall[Xc+DX][Yc+DY] == '#':
                  dx *= -1;
                  Yc += DY;
               else:
                  if Wall[Xc][Yc+DY] == Wall[Xc+DX][Yc+DY] == '#':
                     dy *= -1;
                     Xc += DX;
                  else:
                     if Wall[Xc+DX][Yc+DY] == '#':
                        Done = True;
                     else:
                        Xc += DX;
                        Yc += DY;


               
         else:                         # Hitting a normal edge
            if tx < ty:
               t += tx;
               xi = int(round(xi+dx*tx));
               yi = yi+dy*tx;
               DX = int( dx/abs(dx));
               print (Xc, Yc), (dx, dy), 'x', DX
               if Wall[Xc+DX][Yc] == '#':
                  Xc += DX;
               else:
                  dx *= -1;
            if ty < tx:
               t += ty;
               yi = int(round(yi+dy*ty));
               xi = xi+dx*ty;
               DY = int( dy/abs(dy));
               print (Xc, Yc), (dx, dy), 'y', DY
               if Wall[Xc][Yc+DY] == '#':
                  Yc += DY;
               else:
                  dy *= -1;
                  

         if (Xc == X0) and (Yc == Y0) and (not Done):
            finX = (xi - X0)/dx;
            finY = (yi - Y0)/dy;
            if (finX > 0) and (finY > 0) and ( abs(finX-finY) < 1e-5 ):
               t += finX;
               if t < D + 1e-5:
                  print "Sukces!!!";
                  Ans += 1
                  Done = True



   print "Case #%d:" % (case+1),;
   print Ans;
