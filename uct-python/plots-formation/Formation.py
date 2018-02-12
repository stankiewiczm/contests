from pylab import *
#import matplotlib.pyplot as plt;

light1 = (1, .8, .8);
light2 = (.8, .8, 1);

def S(i):
    if i < 10:
        return '0'+str(i);
    return str(i);

def Symbol(i):
    if i < 4 and i%2 == 0:
        return 'ro';
    if i < 4 and i%2 == 1:
        return 'rs';
    if i >= 4 and i%2 == 0:
        return 'bo';
    if i >= 4 and i%2 == 1:
        return 'bs'

def ArrC(index):
    if index < 4:
        return light1;
    return light2;

def CircX(iList):
    return 2 * cos(2 * pi * array(iList)/8);

def CircY(iList):
    return 2 * sin(2 * pi * array(iList)/8);

L = 4;
def MakePlot(index):
    subplot(111, aspect='equal');

    fig = figure(1, figsize=(5,5));
    fig.clf();
    ax = fig.add_subplot(111);

    title('#'+str(index+1)+': ' + Titles[index]);
    ax.set_aspect(1);
    plot( [0, 0], [-5, 5], 'k--');
    plot( [-5, 5], [0, 0], 'k--');

    plot([PosX[index][0], PosX[index][2]], [PosY[index][0], PosY[index][2]], 's', color=(1,0,0));
    plot([PosX[index][1], PosX[index][3]], [PosY[index][1], PosY[index][3]], 's', color=(1,.4,0));
    plot([PosX[index][4], PosX[index][6]], [PosY[index][4], PosY[index][6]], 's', color=(0,.6,1));
    plot([PosX[index][5], PosX[index][7]], [PosY[index][5], PosY[index][7]], 's', color=(0,0,1));

    if (index > 0):
        plot(PosX[index-1][:4], PosY[index-1][:4], 's', color=light1);
        plot(PosX[index-1][4:], PosY[index-1][4:], 's', color=light2);
        for j in range(8):
            ax.annotate('', xy=(PosX[index][j], PosY[index][j]+1e-3),
                        xytext=(PosX[index-1][j], PosY[index-1][j]),
                        arrowprops=dict(facecolor=ArrC(j), width=0));
        print 'position', index;

    if index == 17:
        t = arange(0, 2*pi, 0.001);
        x = 2*cos(t);
        y = 2*sin(t);
        plot(x, y, color=(0.7, 0.7, 0.7));

    ax.set_xlim(-L, L);
    ax.set_ylim(-L, L);
    
    savefig('position' + S(index+1) + '.png');
    return;


Titles = [];
PosX = [];
PosY = [];

Titles.append("Starting position");
PosX.append([-1, -2, 0, -1, 0, 1, 2, 1]);
PosY.append([ 1,  0, 0, -1, 2, 1, 0, -1]);

Titles.append("Slow waltz - couples opening");
PosX.append([-3.25, -2.75, -2.25, -1.75,  -1.25, -0.75, -0.25, 0.25]);
PosY.append([  0.5, -0.5,  -1.5 , -2.5 ,  1.5,  0.5,  -0.5 , -1.5]);

Titles.append("Waltz parallel lines (pre-whisk)");
PosX.append([-1.50, -1.50, -1.50, -1.50,  1.50, 1.50, 1.50, 1.50]);
PosY.append([  1.0,  0.0,  -1.0 , -2.0 ,  1.5,  0.5,  -0.5 , -1.5]);

Titles.append("End of slow waltz (open for Viennese)");
PosX.append([ 1.50,  1.50,  1.50,  1.50, -1.50, -1.50, -1.50, -1.50]);
PosY.append([  1.0,  0.0,  -1.0 , -2.0 ,  1.5,   0.5,  -0.50, -1.50]);

Titles.append("End of open Viennese waltz (hold for diamonds)");
PosX.append([-1.50, -1.50, -1.50, -1.50,  1.50, 1.50, 1.50, 1.50]);
PosY.append([  1.0,  0.0,  -1.0 , -2.0 ,  1.5,  0.5,  -0.5 , -1.5]);

Titles.append("Diamonds - first quarter");
PosX.append([-2.0, -1.0, -2.0,  -1.0,    1.00, 2.00, 1.00, 2.00]);
PosY.append([ 0.5,  0.5, -1.5 , -1.5,    1.0,  1.0,  -1.0 , -1.0]);
Titles.append("Diamonds - second quarter");
PosX.append([-1.50, -1.50, -1.5,  -1.5,   1.50, 1.50, 1.50, 1.50]);
PosY.append([  0.0,  1.0,  -2.0 , -1.0,   0.5,  1.5,  -1.5 , -0.5]);
Titles.append("Diamonds - third quarter");
PosX.append([-1.00, -2.0, -1.0,  -2.0,   2.00, 1.00, 2.00, 1.00]);
PosY.append([  0.5,  0.5,  -1.5 , -1.5,   1.0,  1.0,  -1.0 , -1.0]);
Titles.append("Diamonds - fourth quarter");
PosX.append([-1.50, -1.50, -1.5,  -1.5,   1.50, 1.50, 1.50, 1.50]);
PosY.append([  1.0,  0.0,  -1.0 , -2.0,   1.5,  0.5,  -0.5 , -1.5]);

Titles.append("Viennese - to the middle");
PosX.append([  0.0,  0.0,   0.0,   0.0,   0.0,  0.0,  0.0,  0.0]);
PosY.append([  1.0,  0.0,  -1.0 , -2.0,   1.5,  0.5,  -0.5 , -1.5]);

Titles.append("Viennese - middle diamonds 1");
PosX.append([  0.35,  0.35,   0.35,   0.35,  -0.35, -0.35,  -0.35,  -0.35]);
PosY.append([  1.25,  0.25,  -0.75 , -1.75,   1.25,  0.25,  -0.75 , -1.75]);
Titles.append("Viennese - middle diamonds 2");
PosX.append([  0.0,  0.0,   0.0,   0.0,   0.0,  0.0,  0.0,  0.0]);
PosY.append([  1.5,  0.5,  -0.5 , -1.5,   1.0,  0.0,  -1.0 , -2.0]);
Titles.append("Viennese - middle diamonds 3");
PosX.append([  -0.35,  -0.35,   -0.35,   -0.35,  0.35, 0.35,  0.35,  0.35]);
PosY.append([  1.25,  0.25,  -0.75 , -1.75,   1.25,  0.25,  -0.75 , -1.75]);
Titles.append("Viennese - middle diamonds 4");
PosX.append([  0.0,  0.0,   0.0,   0.0,   0.0,  0.0,  0.0,  0.0]);
PosY.append([  1.0,  0.0,  -1.0 , -2.0,   1.5,  0.5,  -0.5 , -1.5]);

Titles.append("Viennese - out and turn around partners");
PosX.append([  1.5,  1.5,   1.5,   1.5,  -1.5, -1.5, -1.5, -1.5]);
PosY.append([  1.0,  0.0,  -1.0 , -2.0,   1.5,  0.5, -0.5, -1.5]);

Titles.append("Viennese - move to diagonals and OPEN");
PosX.append([  -1.0,  0.0,   1.0,   2.0,  -2.0, -1.0, -0.0, 1.0]);
PosY.append([  1.25,  0.25,  -0.75 , -1.75,   1.25,  0.25, -0.75, -1.75]);

Titles.append("Twirl and dip (also, untwirl and retwirl)");
PosX.append([  -0.75,  0.25,   1.25,   2.25,  -1.75, -0.75, 0.25, 1.25]);
PosY.append([  1.25,  0.25,  -0.75 , -1.75,   1.25,  0.25, -0.75, -1.75]);

ordering = [2, 1, 0, 7, 3, 4, 5, 6]
Titles.append("Circle for the walks and 'chair' hop");
PosX.append( CircX(ordering) );
PosY.append( CircY(ordering) );


#x = arange((-L+1), L, d)
#y = arange((-L+1), L, d)
#X, Y = meshgrid(x,y);

#[Ex1, Ey1] = E1(X,Y);

for i in range(len(Titles)):
    MakePlot(i);
#MakePlot(1);
