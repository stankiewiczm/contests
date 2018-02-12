from numpy import *

ST = "hihellolookhavealookatthispalindromexxqwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewqxxsoundsfamiliardoesit"
#ST = "zxcvbnmmnbvcxz"
#Lett = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];

T = [];         LIM = len(ST);
for k in range(LIM):
    T.append(zeros(LIM, long));

for k in range(len(ST)):
    T[k][k] = 1;



def Solve(x0, x1):
    T[x0][x1] = T[x0][x1-1]+1;
    for i in range(x0, x1):
        if ST[i] == ST[x1]:
            T[x0][x1] += 1 + T[i+1][x1-1];
    return 0;



for k in range(1,len(ST)):
    for l in range(len(ST)-k):
        Solve(l, l+k)


print T[0][len(ST)-1]
