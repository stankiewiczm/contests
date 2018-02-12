from Numeric import *


def FindMax(a1,a2,a3,a4):
    LIST = [];

    LIST.append(a1+a2+a3+a4);
    LIST.append(a1+a2+a3-a4);
    LIST.append(a1+a2-a3-a4);
    LIST.append(a1+a2-a3+a4);
    LIST.append(a1-a2+a3-a4);
    LIST.append(a1-a2-a3-a4);
    LIST.append(a1-a2-a3+a4);
    LIST.append(a1-a2+a3+a4);

    LIST.append( (a1*a2)+a3+a4 );
    LIST.append( (a1*a2)-a3+a4 );
    LIST.append( (a1*a2)+a3-a4 );
    LIST.append( (a1*a2)-a3-a4 );
    LIST.append( (a1*a3)+a2+a4 );
    LIST.append( (a1*a3)-a2+a4 );
    LIST.append( (a1*a3)+a2-a4 );
    LIST.append( (a1*a3)-a2-a4 );
    LIST.append( (a1*a4)+a3+a2 );
    LIST.append( (a1*a4)-a3+a2 );
    LIST.append( (a1*a4)+a3-a2 );
    LIST.append( (a1*a4)-a3-a2 );

    LIST.append( (a3*a2)+a1+a4 );
    LIST.append( (a3*a2)-a1+a4 );
    LIST.append( (a3*a2)+a1-a4 );
    LIST.append( (a3*a2)-a1-a4 );
    LIST.append( (a4*a3)+a2+a1 );
    LIST.append( (a4*a3)-a2+a1 );
    LIST.append( (a4*a3)+a2-a1 );
    LIST.append( (a4*a3)-a2-a1 );
    LIST.append( (a2*a4)+a3+a1 );
    LIST.append( (a2*a4)-a3+a1 );
    LIST.append( (a2*a4)+a3-a1 );
    LIST.append( (a2*a4)-a3-a1 );

    LIST.append( a1*a4 - a2*a3 );
    LIST.append( a1*a3 - a2*a4 );
    LIST.append( a1*a2 - a4*a3 );
    LIST.append( a1*a4 + a2*a3 );
    LIST.append( a1*a3 + a2*a4 );
    LIST.append( a1*a2 + a4*a3 );

    LIST.append( a1*a2*a3 + a4)
    LIST.append( a1*a2*a4 + a3)
    LIST.append( a1*a3*a4 + a2)
    LIST.append( a2*a3*a4 + a1)
    LIST.append( a1*a2*a3 - a4)
    LIST.append( a1*a2*a4 - a3)
    LIST.append( a1*a3*a4 - a2)
    LIST.append( a2*a3*a4 - a1)

    LIST.append( a1*(a2*a3-a4) );
    LIST.append( a1*(a2*a3+a4) );
    LIST.append( a1*(a2*a4-a3) );
    LIST.append( a1*(a2*a4+a3) );
    LIST.append( a1*(a4*a3-a2) );
    LIST.append( a1*(a4*a3+a2) );
    LIST.append( a2*(a1*a3-a4) );
    LIST.append( a2*(a1*a3+a4) );
    LIST.append( a2*(a1*a4-a3) );
    LIST.append( a2*(a1*a4+a3) );
    LIST.append( a2*(a4*a3-a1) );
    LIST.append( a2*(a4*a3+a1) );
    LIST.append( a3*(a1*a2-a4) );
    LIST.append( a3*(a1*a2+a4) );
    LIST.append( a3*(a1*a4-a2) );
    LIST.append( a3*(a1*a4+a2) );
    LIST.append( a3*(a4*a2-a1) );
    LIST.append( a3*(a4*a2+a1) );
    LIST.append( a4*(a1*a2-a3) );
    LIST.append( a4*(a1*a2+a3) );
    LIST.append( a4*(a1*a3-a2) );
    LIST.append( a4*(a1*a3+a2) );
    LIST.append( a4*(a3*a2-a1) );
    LIST.append( a4*(a3*a2+a1) );



    LIST.append( (a1+a2)*(a3+a4) );
    LIST.append( (a1+a3)*(a2+a4) );
    LIST.append( (a1+a4)*(a3+a2) );

    LIST.append( (a1+a2)*(a3-a4) );
    LIST.append( (a1+a3)*(a2-a4) );
    LIST.append( (a1+a4)*(a3-a2) );
    LIST.append( (a1+a2)*(a4-a3) );
    LIST.append( (a1+a3)*(a4-a2) );
    LIST.append( (a1+a4)*(a2-a3) );

    LIST.append( (a1+a2)*a3*a4 ) 
    LIST.append( (a1+a3)*a2*a4 ) 
    LIST.append( (a1+a4)*a3*a2 ) 
    LIST.append( (a2+a3)*a1*a4 ) 
    LIST.append( (a2+a4)*a3*a1 ) 
    LIST.append( (a3+a4)*a2*a1 )

    LIST.append( (-a1+a2)*a3*a4 ) 
    LIST.append( (-a1+a3)*a2*a4 ) 
    LIST.append( (-a1+a4)*a3*a2 ) 
    LIST.append( (-a2+a3)*a1*a4 ) 
    LIST.append( (-a2+a4)*a3*a1 ) 
    LIST.append( (-a3+a4)*a2*a1 )


    LIST.append(a1*a2*a4*a4);
    LIST.append( (a1*a2)/(a3*a4) );
    LIST.append( (a1*a3)/(a2*a4) );
    LIST.append( (a1*a4)/(a2*a3) );
    LIST.append( (a3*a2)/(a1*a4) );
    LIST.append( (a4*a3)/(a2*a1) );
    LIST.append( (a2*a4)/(a1*a3) );

    LIST.append( a1*(a2+a3) + a4 );
    LIST.append( a1*(a2+a3) - a4 );
    LIST.append( a2*(a1+a3) + a4 );
    LIST.append( a2*(a1+a3) - a4 );
    LIST.append( a3*(a2+a1) + a4 );
    LIST.append( a3*(a2+a1) - a4 );
    LIST.append( a1*(a2+a3) / a4 );
    LIST.append( a2*(a1+a3) / a4 );
    LIST.append( a3*(a2+a1) / a4 );
    LIST.append( a1*(a2+a3+ a4) );
    LIST.append( a1*(a2+a3- a4) );
    LIST.append( a2*(a1+a3+ a4) );
    LIST.append( a2*(a1+a3- a4) );
    LIST.append( a3*(a2+a1+ a4) );
    LIST.append( a3*(a2+a1- a4) );

    LIST.append( a1*(a2+a4) + a3 );
    LIST.append( a1*(a2+a4) - a3 );
    LIST.append( a2*(a1+a4) + a3 );
    LIST.append( a2*(a1+a4) - a3 );
    LIST.append( a4*(a2+a1) + a3 );
    LIST.append( a4*(a2+a1) - a3 );
    LIST.append( a1*(a2+a4) / a3 );
    LIST.append( a2*(a1+a4) / a3 );
    LIST.append( a4*(a2+a1) / a3 );
    LIST.append( a1*(a2+a4 + a3) );
    LIST.append( a1*(a2+a4 - a3) );
    LIST.append( a2*(a1+a4 + a3) );
    LIST.append( a2*(a1+a4 - a3) );
    LIST.append( a4*(a2+a1 + a3) );
    LIST.append( a4*(a2+a1 - a3) );

    LIST.append( a1*(a4+a3) + a2 );
    LIST.append( a1*(a4+a3) - a2 );
    LIST.append( a4*(a1+a3) + a2 );
    LIST.append( a4*(a1+a3) - a2 );
    LIST.append( a3*(a4+a1) + a2 );
    LIST.append( a3*(a4+a1) - a2 );
    LIST.append( a1*(a4+a3) / a2 );
    LIST.append( a4*(a1+a3) / a2 );
    LIST.append( a3*(a4+a1) / a2 );
    LIST.append( a1*(a4+a3 + a2) );
    LIST.append( a1*(a4+a3 - a2) );
    LIST.append( a4*(a1+a3 + a2) );
    LIST.append( a4*(a1+a3 - a2) );
    LIST.append( a3*(a4+a1 + a2) );
    LIST.append( a3*(a4+a1 - a2) );

    LIST.append( a4*(a2+a3) + a1 );
    LIST.append( a4*(a2+a3) - a1 );
    LIST.append( a2*(a4+a3) + a1 );
    LIST.append( a2*(a4+a3) - a1 );
    LIST.append( a3*(a2+a4) + a1 );
    LIST.append( a3*(a2+a4) - a1 );
    LIST.append( a4*(a2+a3) / a1 );
    LIST.append( a2*(a4+a3) / a1 );
    LIST.append( a3*(a2+a4) / a1 );
    LIST.append( a4*(a2+a3 + a1) );
    LIST.append( a4*(a2+a3 - a1) );
    LIST.append( a2*(a4+a3 + a1) );
    LIST.append( a2*(a4+a3 - a1) );
    LIST.append( a3*(a2+a4 + a1) );
    LIST.append( a3*(a2+a4 - a1) );

    LIST.append( a1*a2*a3/a4 );
    LIST.append( a1*a2*a4/a3 );
    LIST.append( a1*a3*a4/a2 );
    LIST.append( a4*a2*a3/a1 );

    LIST.append( (a1*a2+a3)/a4 );
    LIST.append( (a1*a3+a2)/a4 );
    LIST.append( (a3*a2+a1)/a4 );
    LIST.append( (a1*a2+a4)/a3 );
    LIST.append( (a1*a4+a2)/a3 );
    LIST.append( (a4*a2+a1)/a3 );
    LIST.append( (a1*a4+a3)/a2 );
    LIST.append( (a1*a3+a4)/a2 );
    LIST.append( (a3*a4+a1)/a2 );
    LIST.append( (a4*a2+a3)/a1 );
    LIST.append( (a4*a3+a2)/a1 );
    LIST.append( (a3*a4+a1)/a1 );

    LIST.append( (a1*a2)/a3 + a4);
    LIST.append( (a1*a2)/a4 + a3);
    LIST.append( (a1*a3)/a2 + a4);
    LIST.append( (a1*a3)/a4 + a2);
    LIST.append( (a1*a4)/a3 + a2);
    LIST.append( (a1*a4)/a2 + a3);

    LIST.append( (a3*a2)/a1 + a4);
    LIST.append( (a3*a2)/a4 + a1);
    LIST.append( (a4*a3)/a2 + a1);
    LIST.append( (a4*a3)/a1 + a2);
    LIST.append( (a2*a4)/a3 + a2);
    LIST.append( (a2*a4)/a1 + a3);


#    print sort(LIST)
    CANDO = zeros(50);
    for n in sort(LIST):
        if abs(n-round(n)) < 1e-6:
            if (n > 0) and (n < 50):
                CANDO[int(n)] = 1;

    for i in arange(1,50):
        if (CANDO[i] == 0):
            return i;
    return 50;
    


    

TOT = 0;
for a in arange(1,10):
    for b in arange(a+1,10):
        for c in arange(b+1,10):
            for d in arange(c+1,10):
                a;
                if (FindMax(float(d),float(c),float(b),float(a)) > 30):
                    TOT += 1;
                    print [a,b,c,d]

print FindMax(5.,4.,2.,1.);
print FindMax(8.,5.,2.,1.);

