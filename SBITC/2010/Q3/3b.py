#from numpy import *

def zeros(k):
    return [0]*k;
# Shortest paths....
# 3a)

def Solve(Case, Ints, Roads):
    Delays = [];
    #print "Case", Case, Ints, Roads
    Time = [];
    for k in range(Ints+2):
        Delays.append([]);
        Time.append(zeros(Ints+2));
        for l in range(Ints+2):
            Delays[k].append([-1,-1]);
        
    Min = zeros(Ints+2);
    for k in range(2,Ints+2):
        Min[k] = 9999999999;
    Road = [];
    for k in range(Ints+2):
        Road.append([]);

    for k in range(Roads):
        line = raw_input();
        token= line.split();
        X = int(token[0]);      Y = int(token[1]);      M = int(token[2]);
        DelS = int(token[3]);   DelF = int(token[4]);

        Road[X].append(Y);
        Time[X][Y] = M;
        Delays[X][Y] = [DelS, DelF];

    # Now implement Dijkstra    
    TODO = [1];

    while len(TODO) > 0:
        I1 = TODO[0];
#        print TODO, I1, Road[I1];
        for I2 in Road[I1]:
            TimeToI2 = Min[I1]+Time[I1][I2];
            if (Min[I1] < Delays[I1][I2][1]):       # Start travel before roadworks finish
                if (TimeToI2 > Delays[I1][I2][0]):  # Finish travel after they start
                    if (Min[I1] > Delays[I1][I2][0]):
                        TimeToI2 += Delays[I1][I2][1] - Min[I1];
                    else:
                        TimeToI2 += Delays[I1][I2][1] - Delays[I1][I2][0];  # Traffic
            
            if (Min[I2] > TimeToI2):
                Min[I2] = TimeToI2;
                if (I2) not in TODO:
                    TODO.append(I2);
        TODO.pop(0);

    print "Case #%d: %d" % (Case, Min[Ints]);
#    print Min;


Tcases = input();
for T in range(1,Tcases+1):
    L1 = raw_input();
    L2 = L1.split();
    I = int(L2[0]);     R = int(L2[1]);

    Solve(T, I, R);

