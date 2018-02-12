def Solve(r):
    R2 = r*r;
    Psum = 0;
    for x in range(1,2*r):
        alpha = (x+0.)/r;
        ylim = int(2.*r/alpha+r+1)
        for y in range(x,ylim):
            if (x*y > R2):
                if ((x+y)*R2)%(x*y-R2) == 0:
                    z = ((x+y)*R2)/(x*y-R2)
                    if z >= y:
                        Psum += 2*(x+y+z);
    return Psum                


LIM = 1000;
TotalP = 0;
for r in range(1,LIM+1):
    TotalP += Solve(2*r)
    print r, TotalP

# 28038042525570324
