m = 250
mm = 10 ** 16
x = m * [0]
 
for i in range(1, 250251):
    x[pow(i, i, m)] += 1
 
 
y = [1] + (m - 1) * [0]
 
for i in range(m):
    for j in range(x[i]):
        y = [(y[k] + y[(k-i)%m]) % mm for k in range(m)]
 
print(y[0] - 1)
