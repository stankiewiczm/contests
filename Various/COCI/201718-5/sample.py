N = int(raw_input());
M = int(raw_input());
K = int(raw_input());
Lights = [-K];
for i in range(M):
    Lights.append(int(raw_input()));
Lights.append(N+K+1);

Ans = 0;
print N, Lights;
for i in range(1, M+2):
    interval = Lights[i] - Lights[i-1]
    if (interval > 2*K+1):
        Ans += (interval-2*K-1)/(2*K+1)+1
print Ans;
