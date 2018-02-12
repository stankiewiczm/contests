B = [3];        R = [1];
while (B[-1]+R[-1] < 1e12):
    R.append(2*B[-1]+R[-1]-1);
    B.append(2*R[-1]+B[-1]);
print B[-1];
