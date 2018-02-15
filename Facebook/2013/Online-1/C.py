from numpy import *

# Question 3 of facebook hacker cup round 1

def Adjust(goods, p1, p2):      # Remove interval [p1,p2] from list of good points
    ret = [];
#    print goods
    for pair in goods:
        if pair[1] < p1:
          ret.append(pair);   # All good;
        else:
          if pair[0] > p2:
            ret.append(pair);
          else:                 # Not all good
            if (pair[0] < p1) and (pair[1] > p2):
              ret.append( [pair[0], p1-1] );            # Remove middle
              ret.append( [p2+1, pair[1]] );
            else:
              if (pair[0] < p1) and (pair[1] <= p2):
                ret.append( [pair[0], p1-1] );
              if (pair[0] >= p1) and (pair[1] > p2):
                ret.append( [p2+1, pair[1]] );
    return ret;
        
        
def AND( good1, good2 ):
    ret = [];
    l1 = len(good1);        l2 = len(good2);
    i1 = 0;                 i2 = 0;
    while (i1 < l1) and (i2 < l2):      # Not finished yet
        [x0, x1] = good1[i1];
        [y0, y1] = good2[i2];
        
        if x1 < y0:
            i1 += 1;
        else:
          if x0 > y1:
            i2 += 1;
        # Therefore there is some overlap
          else:
            if x0 < y0:
              if x1 <= y1:
                ret.append( [y0, x1] );
                i1 += 1;
              else:
                ret.append( [y0, y1] );
                i2 += 1;
            else:
                # x0 >= y0
                if x1 >= y1:
                  ret.append( [x0, y1] );
                  i2 += 1;
                else:
                  ret.append( [x0, x1] );
                  i1 += 1;
    return ret


def Eval(V):
    ans = 0;
    for pair in V:
        ans += pair[1]-pair[0]+1;
    return ans;



T = int(raw_input());
for q in range(1, T+1):

    [W, H, P, Q, N, X, Y, a, b, c, d] = map(int, raw_input().split());
    x = [0]*N;
    y = [0]*N;
    x[0] = X;
    y[0] = Y;
    for i in range(1,N):
        x[i] = (x[i-1]*a + y[i-1]*b + 1) % W;
        y[i] = (x[i-1]*c + y[i-1]*d + 1) % H;

    # Allowed position for top-left corner of picture:
    # 0 to W-P      0 to H-Q
    #
    # If a pixel at (x,y) is blocked, it blocks all top-left corners
    # from (x-P+1, y-Q+1) to (x,y)

    # First, make a map of legal starting positions for each row
    # taking into account only that row
    Row = [];
    for i in range(H):
        Row.append( [[0, W-P]] );
    for i in range(N):
        Row[y[i]] = Adjust(Row[y[i]], x[i]-P+1, x[i]);

    # For the actual blocks, will need to intersect H consecutive rows
    # For Q blocks, with H-Q possibilities, that will be Q*(H-Q) 'ANDs'
    # Which for these limits is too much

    ANS = 0;
    for h in range(H-Q+1):
        V = Row[h];                 #
        for i in range(1,Q):        # Inefficient way of calculating ANDS
            V = AND(V, Row[h+i]);   # 
        ANS += Eval(V)
            
    print 'Case #%i: %i ' % (q, ANS)
        
