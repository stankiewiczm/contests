# anti-clockwise spiral
def Spiral(dx, dy):
    if (dx == dy == 0):
        return 1;
    dist = max(abs(dx), abs(dy));
    base = (2*dist-1)**2;
    if (dx == -dist):   # far right
        return base + 6*dist + (dist + dy);
    if (dy == -dist):
        return base + 4*dist + (dist - dx);
        return '.';
    if (dx == dist):    # far to the left
        return base + 2*dist + (dist-dy);    
    if (dy == dist):
        return base + (dist + dx);

[N, M, K] = map(int, raw_input().split());
spirals = [];
for i in range(K):
    spirals.append(map(int, raw_input().split()));

for y in range(1, N+1):
    for x in range(1, M+1):
        D = [];
        for spr in spirals:
            if (spr[2] == 0):
                D.append( Spiral(x-spr[1], spr[0]-y) );
            else:
                D.append( Spiral(spr[1]-x, spr[0]-y) );
            
        print min(D),
    print;
