from visual.graph import *

L = 80000;   Prime = zeros(L);    Prime[0] = 2;   Prime[1] = 3;

def Generate():
    NPrime = 2; 
    Sum = zeros(50);    Sum[0] = 5;
    act = 0;
    N = 3;
    while (N < 1e6-2):
        if ((N-1) % 2e4 == 0):
            print "Gone past  ",N-1,"Partial sum:",Sum[act]," Total primes:",NPrime;
            act=act+1;
        N = N+2;
        Good = 1;
        for i in arange(min(NPrime,168)):
            if (N % Prime[i] == 0):
                Good = 0;
                break;
        if (Good == 1):
            Prime[NPrime] = N;
            Sum[act] = Sum[act]+N;
            NPrime += 1;

    print "We reached",N+1,"Partial sum:",Sum[act]," Total primes:",NPrime;

    Ends= (Sum % 1000000);
    Sum = (Sum + zeros(50,Float))/1e6;
    print "Total of ",NPrime,"Primes, the last of which is ",Prime[NPrime-1];
    print "Sum of primes below a million is ",sum(Prime), "ends", sum(Ends)%1e6;
    print "Miscelleneous sums: ",sum(Sum);
        
Generate();
