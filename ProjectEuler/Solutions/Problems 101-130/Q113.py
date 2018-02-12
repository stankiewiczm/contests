def C(n,r):
    R = 1;
    for k in range(r):
        R = (R*(n-k))/(k+1);
    return R;

print C(109,9) + C(110,10) - 1002;

