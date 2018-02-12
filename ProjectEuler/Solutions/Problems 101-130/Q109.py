Score = [50,25];        Double = [50];
for k in range(1,21):
    Score += [k, 2*k, 3*k];
    Double += [2*k]

Ways = [0]*121;     Ways[0] = 1;     Final = [0]*181;        

for d1 in range(len(Score)):
    Ways[Score[d1]] += 1;
    for d2 in range(d1+1):
        Ways[Score[d1]+Score[d2]] += 1;

# Now finish with a double:
for l in range(181):
    for d in Double:
        if (l >= d) and (l-d <= 120):
            Final[l] += Ways[l-d];

print sum(Final[0:100]);


