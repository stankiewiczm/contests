from pylab import *

def Line(a,b,c,d):
    if (a == c) and (b == d):
        return False;

    if (a == c) or (b == d):
        return True;

    if (2*(d-b)%(c-a) != 0):
        return False;
        
    S2 = (2*(d-b))/(c-a);
    if (abs(S2) == 2) and ((a-b)%2 == 0):
        return True;

    if (S2 == 4) and ((b==2*a) or (b == 2*a-8)):
        return True;

    if (S2 == -4) and ((b+2*a==8) or (b+2*a == 16)):
        return True;

    if (S2 == 1) and ((2*b==a) or (2*b==a+8)):
        return True;

    if (S2 == -1) and ((a+2*b==8) or (a+2*b == 16)):
        return True;

    return False;
    

def NotOneLine(x1,y1,x2,y2,x3,y3):
    return (y2-y1)*(x3-x2) != (y3-y2)*(x2-x1);


TOTAL = 0;      M = 9;
for x1 in range(M):
  for y1 in range(M):
    for x2 in range(M):
      for y2 in range(M):
        if Line(x1,y1,x2,y2):
#           print (x1,y1),(x2,y2);      # Two points
          for x3 in range(M):
            for y3 in range(M):
              if Line(x1,y1,x3,y3):
                if Line(x2,y2,x3,y3):

                    if NotOneLine(x1,y1,x2,y2,x3,y3):
                      TOTAL += 1; 
                
print TOTAL, TOTAL/6;
