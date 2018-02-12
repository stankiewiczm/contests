from Numeric import *

def GCD(A,B):
    while (B > 0):
        C = B;
        B = A - (A/B)*B;
        A = C;
    return A;

LIM = int(1e12);      TOT = 0;  
#for b in arange(1,int(sqrt(float(LIM)))+1):
#    L = max( int((b**3)/LIM), 0 )
#    for a in arange(1+L,b):
#        if (b*b)%a == 0:
#            c = (b*b)/a;
#            NEW = a+b*c;
#            if NEW < LIM:
#                if int(sqrt(float(NEW)))**2 == NEW:
#                    TOT += NEW;
#                    print a,'+',b,'*',c,"produce",a+b*c,"=",sqrt(a+b*c),"^2";
#                    G = GCD(b,a);
#                    print "       ratio of ",b/G,"/",a/G;



for a in arange(1,540000):        # Then a+b*c >= 1e6;
    if (a%10000 == 0):
        print "Completed a value of",a;
    for beta in arange(1,int(sqrt(a))+2):
        if (a%(beta**2) == 0):
            SQ1 = a*beta;
            if ( int(sqrt(SQ1))**2 == SQ1 ):
                SQ1 = a*beta;

                LIMalph = int(beta * exp(log(float(LIM/(a*a)))/3.) );
                LIMalph = min(LIMalph, 6*beta)+2;
                
                for alph in arange(beta+1, LIMalph):
                    G = GCD(alph,beta);
                    if (G == 1) or (int(sqrt(G))**2 != G):
                        SQ2 = beta**3 + a*alph**3;
                        if (int(sqrt(float(SQ2)))**2 == SQ2):
                            b = (alph*a)/beta;
                            c = (alph*b)/beta;
                            S = a+b*c;
                            if (S < LIM):
                                print "Got a live one here: ", a,'+',b,'*',c,' = ',S;
                                print "                  ",a,alph,beta
                                TOT += S;

print "Total below",int(LIM),"is",TOT;
