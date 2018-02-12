Data = [];
Hits = [];
Dig = [];
Poss = [];

Fin = open("NMind",'r');
for line in Fin:                                # Read Data
    Data.append( line.split()[0] );
    Hits.append( int(line.split()[1][1]) );

for i in range(16):
    Dig.append( [0]*10 );
for s in Data:
    for j in range(len(s)):                     # See which digits are used
        Dig[j][int(s[j])] = 1;

for q in range(16):
    Poss.append( [] );
    for j in range(10):                         # Map of digit possibilities
        if (Dig[q][j] == 1) or (sum(Dig[q])) > 8:
            Poss[q] += [j];

for j in range(15,-1,-1):
    if Hits[j] == 0:                            # Remove zero hit words
        row = Data[j]
        for i in range(16):
            if int(row[i]) in Poss[i]:
                Poss[i].remove(int(row[i]))
        Hits.pop(j);
        Data.pop(j)
        
for i in range(len(Dig)):
    print Dig[i], Poss[i]

R = 1;
for i in range(16):
    R *= len(Poss[i]);
    print i+1, R

#print Data
#print Hits
