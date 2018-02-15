# anti-clockwise spiral



N = int(raw_input());
boss = [0] + map(int, raw_input().split());
for i in range(N):
    boss[i] -= 1;
money = [0] * N;

lackey = [0]*N;
for i in range(1, N):
    lackey[ boss[i] ] += 1;
    
serfs = [];
for i in range(N):
    if lackey[i] == 0:
        serfs.append(i);

while len(serfs) > 0:
    serf = serfs.pop(0);

    lackey[boss[serf]] -= 1;        # immediatelly quit
    if lackey[boss[serf]] == 0:
        serfs.append(boss[serf]);

    reward = 1;
    money[serf] += reward;
    while (boss[serf] != -1):
        reward += 1;
        serf = boss[serf];
        money[serf] += reward;

for m in money:
    print m,
print
