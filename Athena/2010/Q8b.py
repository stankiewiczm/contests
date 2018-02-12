from numpy import *

ST = "hihellolookhavealookatthispalindromexxqwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewqxxsoundsfamiliardoesit"
ST = "zxcvbnmmnbvcxz"
Lett = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];

Data = [];
for k in ST:
    Data.append( ord(k)-97 );

def Recurse(PArr):
    if len(PArr) == 0:
        return 0;
        
    Pos = [];
    for k in range(26):
        Pos.append([]);
    for l in range(len(PArr)):
        Pos[ PArr[l] ].append(l);
#    for l in range(len(ST)):
#        Pos[ord(ST[l])-97].append(l);

    count = 0;
    for n1 in range(26):
        for a in Pos[n1]:
           for b in Pos[n1]:
                if (a <= b):
#                   print PArr, a, b, n1
                   count += 1
                   count += Recurse(PArr[a+1:b]);
    #               print PArr
    return count;
    
##################################################



print Recurse(Data);
