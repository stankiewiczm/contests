from numpy import *

FILE = open("C-large.in","r");

def Solve(x,y,data):
    Best = 0;
    Bads = [];
    for a in range(y):
        for b in range(x):
            if data[a][b] == 1:
                Bads.append([a,b]);
#    print x,y
#    Print (data);

    for y0 in range(y):
        for y1 in range(y0,y):
            GoodX = range(x);
            for b in Bads:
                if y0 <= b[0] <= y1 and b[1] in GoodX:
                    GoodX.remove(b[1]);

            good = (y1-y0+1)*cont(GoodX);
            if good > Best:
                Best = good;
 #               print y0, y1, GoodX, good
    print Best;
    return;


def Print(field):
    print 
    for line in field:
        for e in line:
            print e,
        print "  ";
    

def cont(List):
    if len(List) == 0:
        return 0
    C = 1;      B = 1;
    for e in range(1,len(List)):
        if List[e] == List[e-1]+1:
            C += 1;
            if C > B:
                B += 1;
        else:
            C = 1;
    return B;


N = int(FILE.readline());
for k in range(N):          # Each of the N cases:
    print "Case #%d:" %(k+1),
    [X,Y] = map( int, FILE.readline().split() );
    Field = [];
    for i in range(Y):
        Field.append([]);
        S = FILE.readline();
        for s in S:
            if s in ['G','S']:
                Field[i].append(0);
            if s in ['R','T','W']:
                Field[i].append(1);
#    Print (Field);                

    Solve(X,Y,Field);
#    Solve(Red, Blue);
