L = [5,17];         P = 3*sum(L);       LIM = 1e9;      

while (3*L[-1] < LIM):
    L.append( 4*L[-1]-L[-2]+2 );
    if (3*L[-1] < LIM):
        P += 3*L[-1]+1;

    L.append( 4*L[-1]-L[-2]-2 );
    if (3*L[-1] < LIM):
        P += 3*L[-1]-1;

print P
