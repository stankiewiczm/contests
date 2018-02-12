LIM = 201;

Best = [];          Steps = [100]*LIM;
for k in range(LIM):
    Best.append([]);
Best[1] = [[1]];      Steps[1] = 0;       Steps[0] = 0;

for n in range(2,LIM):              # Do number n
  if n%2 == 0:
    Steps[n] = Steps[n/2]+1;
    for A in Best[n/2]:
      Best[n].append( A+[n] );
  else:
      for i in range(n):              # Check all smaller i
        for AB in Best[i]:
          for a in range(len(AB)):
            for b in range(a+1):
              if AB[a]+AB[b] == n:
                if Steps[n] == Steps[i]+1:
                  Best[n].append( AB+[n] );
                if Steps[n] > Steps[i]+1:
                  Steps[n] = Steps[i]+1;
                  Best[n] = [AB+[n]];

print sum(Steps); 

